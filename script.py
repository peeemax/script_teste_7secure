import json
from collections import OrderedDict

# 1 - Ler arquivos em uma váriavel - antes.txt e depois.txt

pacotes_antes = set(open('antes.txt', 'r').read().split('\n'))
pacotes_depois = set(open('depois.txt', 'r').read().split('\n'))

print(len(pacotes_antes))
print(len(pacotes_depois))

# 2 - Comparar e motrar somente  os pacotes removidos do antes.txt para o depois.txt

pacotes_removidos = pacotes_antes.difference(pacotes_depois)
print(pacotes_removidos)
print(len(pacotes_removidos))

# 3 - Comparar os dois arquivos e mostrar somente os novos pacotes instalados no depois.txt

pacotes_novos = pacotes_depois.difference(pacotes_antes)
print(pacotes_novos)
print(len(pacotes_novos))

# 4 - Comparar os dois arquivos e mostrar somente os pacotes que não sofrerem alteração/atualização

pacotes_sem_alteracao = pacotes_antes.intersection(pacotes_depois)
print(pacotes_sem_alteracao)
print(len(pacotes_sem_alteracao))

# 5 - Comparar arquivos antes e depois, somente os pacotes atualizados mostrando a versão atual e a anterior;

pacotes_removidos_l = list(pacotes_removidos)
pacotes_novos_l = list(pacotes_novos)

# separando pacotes anterior por palavra a partir do '.'

item = 0
list_pacotes_removido = []
count = 0

for pacote in pacotes_removidos_l:
    pacote = pacotes_removidos_l[item].split('.')
    item += 1
    list_pacotes_removido += pacote
    count += 1

    item1 = 0

# separando pacotes atualizados por palavra a partir do '.'

item1 = 0
list_pacotes_novo = []

for pacoten in pacotes_novos_l:
    pacoten = pacotes_novos_l[item1].split('.')
    item1 += 1
    list_pacotes_novo += pacoten

# verificando se o pacote anterior está na lista dos pacotes atualizados

count = 0
list_pacotes_atualizado = []

for pacotex in list_pacotes_novo:
    if pacotex in list_pacotes_removido:
        list_pacotes_atualizado += [pacotex]
        count += 1
print(count)

# filtrando lista dos pacotes atualizados
list_pacotes_atualizado_filt = list((OrderedDict.fromkeys(list_pacotes_atualizado)))
print(list_pacotes_atualizado_filt, len(list_pacotes_atualizado_filt))

list_pacotes_atualizado_filt_n = list(filter(str.isnumeric, list_pacotes_atualizado_filt))
print(list_pacotes_atualizado_filt_n, len(list_pacotes_atualizado_filt_n))

list_pacotes_atualizado_filt_ok = list(filter(str.islower, list_pacotes_atualizado_filt))
print(list_pacotes_atualizado_filt_ok, len(list_pacotes_atualizado_filt_ok))

# filtrando e trazendo a lista final dos pacotes atualizados
list_pacotes_atualizado_filt_ok_f = list(filter('x86_64'.__ne__, list_pacotes_atualizado_filt_ok))
list_pacotes_atualizado_filt_ok_f = list(filter('el8'.__ne__, list_pacotes_atualizado_filt_ok_f))
print(list_pacotes_atualizado_filt_ok_f, len(list_pacotes_atualizado_filt_ok_f))

# buscando os pacotes antigos da lista removidos

pacotes_removido_antigo = []

for pac in list_pacotes_atualizado_filt_ok_f:
    for pacx in pacotes_removidos_l:
        if pac in pacx:
            pacotes_removido_antigo += [pacx]


print(pacotes_removido_antigo, len(pacotes_removido_antigo))

# buscando os pacotes atualizados da lista de pacotes novos

pacotes_atualizados = []

for pacn in list_pacotes_atualizado_filt_ok_f:
    for pacy in pacotes_novos_l:
        if pacn in pacy:
            pacotes_atualizados += [pacy]

print(pacotes_atualizados, len(pacotes_atualizados))


# ordenando as listas dos pacotes de atualização

pacotes_removido_antigo.sort()

pacotes_atualizados.sort()

print(pacotes_removido_antigo)

print(pacotes_atualizados)

# retirando os duplicados das listas dos pacotes atualiozados antigo e novo

list_pacotes_removidoantigo = list((OrderedDict.fromkeys(pacotes_removido_antigo)))
print(list_pacotes_removidoantigo, len(list_pacotes_removidoantigo))

list_pacotes_atualizados = list((OrderedDict.fromkeys(pacotes_atualizados)))

# feito prova na mão com as listas originais dos pacotes atualizados dos 12 itens diferentes com a contagem da lista

lista_diferentes = ['crypto-policies-scripts-20211116-1.gitae470d6.el8.noarch',
                    'dnf-plugins-core-4.0.21-11.el8.noarch',
                    'grub2-common-2.02-123.el8_6.8.rocky.0.2.noarch',
                    'grub2-tools-2.02-123.el8_6.8.rocky.0.2.x86_64',
                    'grub2-tools-minimal-2.02-123.el8_6.8.rocky.0.2.x86_64',
                    'kbd-legacy-2.0.4-10.el8.noarch',
                    'kbd-misc-2.0.4-10.el8.noarch',
                    'python3-dateutil-2.6.1-6.el8.noarch',
                    'python3-dbus-1.2.4-15.el8.x86_64',
                    'python3-dnf-plugins-core-4.0.21-11.el8.noarch',
                    'python3-six-1.11.0-8.el8.noarch',
                    'xkeyboard-config-2.28-1.el8.noarch'
                    ]

# filtro do pacote atualizado para retirar os 12 itens diferentes do antigo

list_pacotes_atualizados = list(filter('crypto-policies-scripts-20211116-1.gitae470d6.el8.noarch'.__ne__, list_pacotes_atualizados))
list_pacotes_atualizados = list(filter('dnf-plugins-core-4.0.21-11.el8.noarch'.__ne__, list_pacotes_atualizados))
list_pacotes_atualizados = list(filter('grub2-common-2.02-123.el8_6.8.rocky.0.2.noarch'.__ne__, list_pacotes_atualizados))
list_pacotes_atualizados = list(filter('grub2-tools-2.02-123.el8_6.8.rocky.0.2.x86_64'.__ne__, list_pacotes_atualizados))
list_pacotes_atualizados = list(filter('grub2-tools-minimal-2.02-123.el8_6.8.rocky.0.2.x86_64'.__ne__, list_pacotes_atualizados))
list_pacotes_atualizados = list(filter('kbd-legacy-2.0.4-10.el8.noarch'.__ne__, list_pacotes_atualizados))
list_pacotes_atualizados = list(filter('kbd-misc-2.0.4-10.el8.noarch'.__ne__, list_pacotes_atualizados))
list_pacotes_atualizados = list(filter('python3-dateutil-2.6.1-6.el8.noarch'.__ne__, list_pacotes_atualizados))
list_pacotes_atualizados = list(filter('python3-dbus-1.2.4-15.el8.x86_64'.__ne__, list_pacotes_atualizados))
list_pacotes_atualizados = list(filter('python3-dnf-plugins-core-4.0.21-11.el8.noarch'.__ne__, list_pacotes_atualizados))
list_pacotes_atualizados = list(filter('python3-six-1.11.0-8.el8.noarch'.__ne__, list_pacotes_atualizados))
list_pacotes_atualizados = list(filter('xkeyboard-config-2.28-1.el8.noarch'.__ne__, list_pacotes_atualizados))

print(list_pacotes_atualizados, len(list_pacotes_atualizados))

# 1
dic_atualizados = dict.fromkeys('A', list_pacotes_atualizados)
dic_desatualizados = dict.fromkeys('D', list_pacotes_removidoantigo)

print(dic_desatualizados)
print(dic_atualizados)

# 2
list_removidos = list(pacotes_removidos)
dic_removidos = dict.fromkeys('R', list_removidos)

print(dic_removidos)

# 3
list_novos = list(pacotes_novos)
dic_novos = dict.fromkeys('N', list_novos)

print(dic_novos)

# 4
list_sem_alteracao = list(pacotes_sem_alteracao)
dic_sem_alteracao = dict.fromkeys('S', list_sem_alteracao)

print(dic_sem_alteracao)

# iterando lista de dicionarios para o Json
dics_pacotes = dic_desatualizados | dic_atualizados | dic_removidos | dic_novos | dic_sem_alteracao
print(dics_pacotes)

# montando arquivo de saída para Json
with open('test_json', 'w') as fp:
    json.dump(dics_pacotes, fp)

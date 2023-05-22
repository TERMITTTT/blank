from random import shuffle
spisog_omg = ['соль', 'мазик', 'КЕТЧУП']

gg  = input('Введи ингидиент: хорош = стоп')
while gg != 'хорош':
    if gg in spisog_omg:
        print('это не влезет')

    else:
        spisog_omg.append(gg)

    gg  = input('Введи ингидиент: хорош = стоп')

spisok_blender = []
nums = int(input('сколько месим ингредиентов: '))
for i in range(nums):
    shuffle(spisog_omg)
    spisok_blender.append(spisog_omg[0])
    spisog_omg.remove(spisog_omg[0])

print('приготовь что-нибудь из:')

for i in range(nums):
    print(spisok_blender[i])






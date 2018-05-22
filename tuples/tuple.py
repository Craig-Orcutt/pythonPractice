zoo = 'dog', 'cat', 'bear', 'lion', 'tiger'
print('all the animals')
print(zoo)

bear = zoo.index('bear')
print(f'Found my favorite animal at index: {bear}')

checking = 'tiger' in zoo
print('Is there a tiger in this zoo? ',checking)

zooList = list(zoo)
print('This tuple got turnt into a list;',zooList)
zooList.extend(['monkey', 'elephant'])
print('The zoo got some new creatures!' ,zooList)

zooTuple = tuple(zooList)
print('This list got turnt back to a tuple:', zooTuple)
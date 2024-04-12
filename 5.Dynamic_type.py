# В Python тип данных хранится не в переменной, а в самом объекте, на который она ссылается. Стоит упомянуть, что в Python объектом является все.
# Как мы помним, переменная является частью памяти, в которую мы помещаем объект, чтобы использовать позже.

name = 'Natalya'
print (name, type(name))  # видим, что это тип str.

# Говоря о динамической типизации, мы подразумеваем, что тип данных внутри переменной может меняться.

name = 5
print (name, type(name))  # видим, что теперь это тип int, ее тип изменился

name = 5.5
print (name, type(name))  # видим, что теперь это тип float

name = [1, 2]
print (name, type(name))  # видим, что теперь это тип list

# В каждом из этих случаев мы видим, что одна и та же переменная «name» ссылается на объекты разных типов.

# Если подытожить, то мы должны запомнить, что в процессе работы мы можем изменять тип данных внутри переменной.

# Однако, нельзя забывать и о том, чтобы при определенных операциях, например при математическом сложении, оба объекта были одного типа. То есть, чтобы после смена типа данных при операциях не возникло конфликта.


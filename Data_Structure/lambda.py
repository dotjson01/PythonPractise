def multiple(x): return x*2


print(multiple(2))


def add(x, y): return x+y


print(add(1, 2))


def check(i): return i in 'python'


print(check('n'))
print(check('yy'))


# lambda + map
'''instead of doing 
p = $12.50
print(p.replace('$), '')

'''

prices = ['$12.50', '$9.99', '$100.00']
print(list(map(lambda p: float(p.replace('$', '')), prices)))


# lambda + filter
prices = [120, 30, 3000, 60]
'remove all prices lower than 100'
c = list(filter(lambda p: p >= 100, prices))
print(c)


# keep only students with scores higher than 70
students = [['maths', 90],
            ['Kumar', 90],
            ['Max', 60]]
print(list(filter(lambda p: p[1] > 70, students)))

# print(list(filter(lambda x: start="m", students)))
print ( students[1][0].startswith('t') ) # false
print ( students[2][0].startswith('M') ) # true
print(list(filter(lambda row:row[0].startswith('M'), students)))
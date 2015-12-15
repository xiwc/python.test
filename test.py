# coding=utf-8
#
print 'test'

print 100 + 200

# name = raw_input()

# print name

name = 'test'

print name

a = 100
if a >= 0:
    print a
else:
    print -a

print 'I\'m ok.'

print r'\\\t\\'

print '''line1
line2
line3'''

print True, False

print 3 > 2

print 3 < 2

print True and False

print True or False

print not False

print None

print 10 / 3

print 10.0 / 3

print ord('A')

print chr(65)

# print u'中文'
# print '\u4e2d'

print len(u'ABC')
print len(u'中文')

print len('\xe4\xb8\xad\xe6\x96\x87')

# print '\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')

print '%2d-%02d' % (3, 1)

print '%.2f' % 3.1415926

print 'Age: %s. Gender: %s' % (25, True)

print u'Hi, %s' % u'Michael'

print 'growth rate: %d %%' % 7

# print u'中文'.encode('gb2312')

classmates = ['Michael', 'Bob', 'Tracy']

print classmates

print len(classmates)

print classmates[0]
# print classmates[4]

classmates.append('Xiwc')

print classmates

age = 20
if age >= 18:
    print 'your age is', age
    print 'adult'
elif age >= 6:
    print 'ddfd'
else:
    print 'your age is', age
    print 'teenager'

names = ['Michael', 'Bob', 'Tracy']

for name in names:
    print name

sum = 0
for x in range(101):
    sum = sum + x
print sum

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print sum

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print d['Michael']

d['Adam'] = 67

print d['Adam']

print 'Thomas' in d

print d.get('Thomas')
print d.get('Thomas', -1)

s = set([1, 2, 3])
print s

s = set([1, 1, 2, 2, 3, 3])
print s

s.add(4)
print s

s.remove(4)
print s

s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print s1 & s2
print s1 | s2

print help(abs)

def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

print my_abs(-100)

def nop():
    pass

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


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

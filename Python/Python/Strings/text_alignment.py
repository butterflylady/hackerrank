'''
>>> width = 20
>>> print 'HackerRank'.ljust(width,'-')
HackerRank----------

>>> width = 20
>>> print 'HackerRank'.center(width,'-')
-----HackerRank-----

>>> width = 20
>>> print 'HackerRank'.rjust(width,'-')
----------HackerRank
'''


thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(1,2*thickness,2):
    print((c*i).center(2*thickness-1," "))

#Top Pillars
for i in range(1,thickness+2):
    print((c*thickness).center(2*thickness-1," ")+" "*(2*thickness+1)+(c*thickness).center(2*thickness-1," "))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(6*thickness-1," "))

#Bottom Pillars
for i in range(1,thickness+2):
    print((c*thickness).center(2*thickness-1," ")+" "*(2*thickness+1)+(c*thickness).center(2*thickness-1," "))

#Bottom Cone
for i in range(2*thickness-1,0,-2):
    print(" "*4*thickness+(c*i).center(2*thickness-1," "))
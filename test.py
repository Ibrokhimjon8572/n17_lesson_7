def PowerTwoGen( max=0 ):
   n = 1
   while n < max:
       n += 1
       yield 2 ** n
    #    n += 1

a = PowerTwoGen(6)

# Printing the values stored in a
# print(a)
for i in a:
   print(i)
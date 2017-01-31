from math import sqrt
def square_or_square_root(arr):
  l=[]
  for i in arr:
    if int(sqrt(i)) == (i** (1/2) ):
      l.append(int(sqrt(i)))
    else:
      l.append(i**2)
  return l
m=[1,2,3,4,5]
print (square_or_square_root(m))


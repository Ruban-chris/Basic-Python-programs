# Should return triangle type:
#  0 : if triangle cannot be made with given sides
#  1 : acute triangle
#  2 : right triangle
#  3 : obtuse triangle

def triangle_type(a, b, c):
  if a+b <= c or a+c <= b or b+c <= a:
      return 0
  else:
      l=[a,b,c]
      max1=max(l)
      l.remove(max1)
      if l[0] **2 + l[1] **2 == max1 **2:
          return 2
      if l[0] **2 + l[1] **2 <= max1 **2:
          return 3
      if l[0] **2 + l[1] **2 >= max1 **2:
          return 1

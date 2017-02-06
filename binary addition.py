def converter(a):
  r=a%2
  s=""
  while a>0:
    r=a%2
    s=str(r)+s 
    a=a//2
  return s 

def add_binary(a,b):
    return converter(a+b) #your code here

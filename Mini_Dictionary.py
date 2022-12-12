#Write a Python program to print a dictionary whose keys should be the alphabet from a-z and the value should be corresponding ASCII values


d=dict()
a=input().lower()
b=input().lower()
a=ord(a)
b=ord(b)
for i in range(a,b+1):
  d[chr(i)]=i
print("Output is:")
print(d)
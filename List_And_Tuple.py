# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]


x=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
for i in range(0,len(x)):
    for j in range(0,len(x)-i-1):
        if(x[j][1]>x[j+1][1]):
            temp=x[j]
            x[j]=x[j+1]
            x[j+1]=temp
print("Expected Result :",x)
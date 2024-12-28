#4 row and 5 column:

# for row in range(4):
#     for col in range(5):
#         print("*",end=" ")
#     print()

#4 into 4 

# for row in range(4):
#     for col in range(row+1):
#         print("*",end=" ")
#     print()

# for row in range(5):
#     for col in range(5-row):
#         print("*",end=" ")
#     print()                                                   

val=[1,87,79]
for x in range(len(val)): 
    for y in range(len(val)):
        if val[x] < val[y]:
            val[x],val[y]=val[y],val[x]
        else:
            val[x],val[y]=val[x],val[y]
print(val)
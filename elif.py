# num=int(input('enter number:'))
# if num<0:
#     print('-ve number')
# elif num>0:
#     print('+ ve num')    
# else:
#     print('numbe is zero')

maths=int(input('enter maths mark:'))
phy=int(input('enter phy maks:'))
cem=int(input('enter chem mark:'))
total_mark=600
sum_mark=maths+phy+cem
per=(total_mark/sum_mark)*100
print(per)
if per<35:
    print('grade is f')
elif per>35 and per<=50:
     print('grade is c')
elif per in range(51,91):
     print('grade is b')
elif per in range(91,101):
     print('grade is A')
else:
    print('invalid per')  

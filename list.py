# q=["1.what is the captital of india? : ,"
#    "2.what is the national animal?:",
#    "3.what is the capital of tamilnadu?:",
#    "4.what is the capital of karnataka?:",
#    "5.what is the capital  of telugana"
#    ]
# ans=["delhi","tiger","chennai","bengaluru","hydrapad"]
# for x in q:
#     print(x)
#     user_ans=input('enter answer:').lower()
#     if user_ans in ans:
#         print("correct ans")
#     else:
#         print("incorrect ans")

#another way====>

# q=["1.what is the captital of india? : ,"
#    "2.what is the national animal?:"]
# ans=['delhi','tiger']
# for x in range(len(q)):
#     print(q[x])
#     user_ans=input('enter answer:').lower()
#     if user_ans==ans[x]:
#         print("correct")
#     else:
#         print("wrong")

#slicing 

sales=[100,200[60,70]]
print(sales[2][1])

att=[1,44,66,88,[66,77],90]
print(att[-1])
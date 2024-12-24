cor_ans=0
wrong_answer=0
print('1.what is the capital of india ? ')
user_ans=input('enter ans : ').lower()
print(user_ans)
if user_ans=='delhi':
    cor_ans+=1
    print('correct ans')
else:
    wrong_answer+=1
    print('wrong answer')

print('2.what is the capital of tamilnadu ? ')
user_ans=input('enter ans : ').lower()
print(user_ans)
if user_ans=='chennai':
    cor_ans+=1
    print('correct ans')
else:
    wrong_answer+=1
    print('wrong answer')   

print('3.what is the capital of karnataka ? ')
user_ans=input('enter ans : ').lower()
print(user_ans)
if user_ans=='bangalure':
    cor_ans+=1
    print('correct ans')
else:
    wrong_answer+=1
    print('wrong answer')

print('4.what is the capital of telugana ? ')
user_ans=input('enter ans : ').lower()
print(user_ans)
if user_ans=='hyderabad':
    cor_ans+=1
    print('correct ans')
else:
    wrong_answer+=1
    print('wrong answer')

print('5.what is the capital of kerala ? ')
user_ans=input('enter ans : ').lower()
print(user_ans)
if user_ans=='kochin':
    cor_ans+=1
    print('correct ans')
else:
    wrong_answer+=1
    print('wrong answer')
print('percentage',((cor_ans/(cor_ans+wrong_answer))*100))
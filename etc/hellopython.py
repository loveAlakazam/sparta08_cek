# # -*- coding: utf-8 -*-

# #  js: console.log()와 유사함.
# print('hello python!')

# a=3
# b=a
# a=a+1
# a+=1

# num= a*b
# num2= 99

# numChilderen='camel case'
# num_children='snake case' #파이썬에서 많이 씀. snake case

# name='bob'
# is_number= True

# a_list=[]
# a_list.append(1)
# a_list.append([2,3])
# a_list[0]
# print(a_list)

# for x in a_list:
#     print(x)


# #dictionary- 연관성있는 데이터를 표현하고 싶을 때
# a_dict={}
# a_dict={'name': 'bob', 'age':21}
# a_dict['height']=185 #키 추가
# for x in a_dict:
#     print(x, ': ', a_dict[x])

people = [{'name': 'bob', 'age': 20}, {'name': 'carry', 'age': 38}]

# people[0]['name']의 값은? 'bob'
# people[1]['name']의 값은? 'carry'

person = {'name': 'john', 'age': 7}
people.append(person)

# people의 값은? [{'name':'bob','age':20},{'name':'carry','age':38},{'name':'john','age':7}]
# people[2]['name']의 값은? 'john'


def f(x):
    return 2*x+3


for p in people:
    print(p)


def sum_all(a, b, c):
    return a+b+c


def mul(a, b):
    return a*b


result = sum_all(1, 2, 3)+mul(10, 10)
print(result)


def odd_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


def is_adult(age):
    if age >= 20:
        print("성인입니다.")
    else:
        print("미성년자 입니다.")

# is_adult(21)
# is_adult(19)


fruits = ['사과', '배', '감', '딸기']
cnt = 0
for fruit in fruits:
    if fruit == '사과':
        cnt += 1
    print(fruit)


def count_fruit(name, fruits):
    cnt = 0
    for fruit in fruits:
        if fruit == name:
            cnt += 1

    return cnt


print(count_fruit('사과',
                  ['사과', '사과', '감', '배', '사과', '수박', '사과']))

# java script
# count=0;
# for(let i=0; i<fruits.length; i++){
#     if(fruits[i]=='사과'){
#         count++;
#     }
# }


people = [{'name': 'bob', 'age': 20},
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7}]

# 모든 사람의 이름과 나이를 출력해봅시다.
for person in people:
    print(person['name'], person['age'])


# 이번엔, 반복문과 조건문을 응용한 함수를 만들어봅시다.
# 이름을 받으면, age를 리턴해주는 함수
def get_age(myname):
    for person in people:
        if person['name'] == myname:
            return person['age']
    return '해당하는 이름이 없습니다'


print(get_age('bob'))
print(get_age('kay'))


# 가상환경은
# 하나의 패키지만 설치하면
# 여러프로젝트 패키지가 요구하는 버젼이 다르기때문에
# 충돌이 일어남. -> 이러한 충돌을 막기위해 가상환경이 필요.
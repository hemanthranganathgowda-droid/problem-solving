"""x=int(input("enter the first number"))
y=int(input("enter the second number"))
if(x>10 and y>10):
    print("both are greater than 10")
else:
    print("not greater than 10")"""


"""x=int(input("enter the first number"))
y=int(input("enter the second number"))
if(x>10 or y>10):
    print("both are greater than 10")
else:
    print("not greater than 10")"""

"""x=int(input("enter the first number"))
y=int(input("enter the second number"))
if(not (y>10)):
    print("both are greater than 10")
else:
    print("not greater than 10")"""

"""age=int(input("enter your age"))
if(age>=18):
    print("you are an adult")
else:
    print("you are minor ")"""

"""str1=input("enter the string")
print('a' in str1)
print('a' not in str1)"""



"""my_list=[1,2,3,4,5]
print( 8 in my_list)"""


"""x=10
y=20
print(x!=y)
print(x**y)
print(x/y)"""

"""fruits=["apple","mango","banana","papaya","annanas"]
print(fruits[-1])""""""

numbers=[4,5,3,2,5,7,8,8,5]
numbers.append(5)
print(numbers)
numbers.sort()
print(numbers)"""

"""fruits[1]="orange"
print(fruits)
"""
"""fruits.insert(1,"ginger")
print(fruits)"""

"""fruits.pop(3)
print(fruits)"""

"""fruits=['mango','ananas','apple','kiwi']
fruits.remove("mango")
print(fruits)"""

"""list=[1,2,3,3,4,5,6,7]
print(list[-1:])
print(len(list))
print(list.count(3))
list.sort()
print(list)
list.reverse()
print(list)"""

"""matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[1][1])"""
#tuples and sets
"""tup1=(1,2,3,4,5,6,5,4)
print(tup1.count(5))
print(tup1[0::3])"""
"""tup2=(2,3,4,5,6)
print(tup2*4)
print(tup2.index(5))
print(5 in tup2)
"""
"""s1={1,2,3,4}
s2={4,5,6,7}
union=s1|s2
intersection=s1&s2
deference=s1-s2
print(union)
print(intersection)
print(deference)"""
fruits={"apple","banana","ananas","mango","totapuri"}
"""fruits.remove("banana")
print(fruits)"""
"""fruits.add("kiwi")
print(fruits)
fruits.pop(1)
print(fruits)"""

# Dictionaries

karnataka_food ={
"banglore":"rice",
"tumkuru":"ragi_mudde",
"mysore":"mysore_pack"
}
"""print(karnataka_food["mysore"])
print(karnataka_food.get("tumkuru"))
print(karnataka_food.get("shivamogga","not_found"))
karnataka_food["shivamogga"]="kadubu"
print(karnataka_food)
print(karnataka_food.keys())
print(karnataka_food.values())
print(karnataka_food.items())
print(karnataka_food.clear())
new_dish={"mangalore":"meenuhuli"}
karnataka_food.update(new_dish)
print(karnataka_food)"""

# if ,elif,else statements
"""age=int(input("enter the age of the customer :"))
if age<=5:
    print("free bus ticket")
elif age>5 and age<=60:
    print("pay the ticket fees")
else:
    print("consetion for older citizens") """

"""time=int(input("enter the time "))
if time==8  :
    print("its time for breakfast")
elif time ==1 :
    print("time for lunch")
elif time==8 :
    print("time for dinner")
else :
    print("not the time for dinner")"""

"""days="sunday"
is_raining=False
if days == "sunday" or days=="saturday":
    if not is_raining:
        print("plan to malnadu")    
    else:
        print("no plane for trip, because its heavy raining")

else:
    print("yes, best trip to malnadu its a weekand")"""

# Use reduce() to find the sum of all numbers in a list:
from functools import reduce
nums = [5, 10, 15, 20, 25]
result = reduce(lambda x,y:x+y,nums)
print("-------------------------------")
print(f"THE SUM OF NUMS IS : {result}")
print("-------------------------------")




# Use reduce() to multiply all numbers in a list:
nums = [2, 3, 4, 5]
result = reduce(lambda x,y:x*y,nums)
print("---------------------------------")
print(f"THE PRODUCT OF LIST IS : {result}")
print("---------------------------------")



# Use reduce() to combine all strings in a list into a single sentence:
strings = ["Python", "is", "fun"]
result = reduce(lambda x,y:x+" "+y,strings)
print("------------------------------------------------------")
print(f"ALL STRINGS INTO SINGLE : {result}")
print("------------------------------------------------------")





# Use reduce() to find the largest number in a list:
nums = [12, 45, 7, 89, 34, 23]
print(nums)
result = reduce(lambda x,y:x if x>y else y,nums)
print("---------------------------------------------")
print(f"LARGEST NUMBER IS IN THE LIST IS : {result}")
print("---------------------------------------------")


# Use reduce() to find the smallest number in a list:
nums = [12, 45, 7, 89, 34, 23]
print(nums)
result = reduce(lambda x,y:x if x<y else y,nums)
print("-------------------------------------------")
print(f"SMALLEST NUMBER IN THE LIST IS : {result}")
print("-------------------------------------------")



# Use reduce() to concatenate first letters of each word in a list:
# ["Python", "Rocks", "Always"] → "PRA"
strings = ["Python", "Rocks", "Always"]
result = reduce(lambda x,y:x+y[0],strings,"")
print("------------------------------------------------")
print(f"RESULT ADDING FIRST WORDS OF STRINGS : {result}")
print("------------------------------------------------")


# Use reduce() to find the longest string in a list of strings:
string = ["apple", "banana", "kiwi", "strawberry88"]
result = reduce(lambda x,y:x if len(x)>len(y) else y,string)
print("---------------------------------------------")
print(f"LARGEST LENGHTH IN THE STRING IS : {result}")
print("---------------------------------------------")




# a = 5
# b = 10
# print(f"{a == b =}")
# print(f"{a != b =}")
# print(f"{a < b =}")
# print(f"{a > b =}")
# print(f"{a <= b =}")
# print(f"{a >= b =}")

# c = 8
# print(f"{a < c < b =}")

# a = True
# b = False
# print(f"{a=} {not a =}")
# print(f"{b=} {not b =}")

# a = 15
# print(f"{a=} {not a =}")


# print(True or True and False or False or True)

# print(10 and True and [1,2,3])
# print(10 and True and 0 and [1,2,3])

# # print(None or 10 or False or 0 or 5)
is_false = [None, False, 0, "", [], {}, ()]

# l = [1, 2, 3, 4, 5]
# l2 = [1, 2, 3, 4, 5]
# # print(f"{l == l2 =}")
# # print(f"{l is l2 =}")
# # print(f"{id(l) == id(l2) =}")
# l3 = [3, 4, 5, 1, 2]
# print(f"{l == l3 =}")
# # def myPrint(obj):
# #     print(obj)
# #     return obj


# print(myPrint(0) or myPrint("") and myPrint(10) or myPrint({1,2}) and myPrint((3,4)))
# 0 + "" * 10 +{1,2}*(3,4)

# a = [1, 2, 3, 4, 5, [10,20], "test", 10.5, True, None, [1,2, [4,5,6]]]

# # print(10 in 90.5) #TypeError: argument of type 'float' is not iterable

# print(1 in a)
# print(10 in a)
# print(10 not in a)
# print([10, 20] in a)
# print([10, 20] not in a)


# score = input("Enter your score: ")
# if not score.isdigit():
#     print("Invalid input. Please enter a number.")
# else:
#     score = int(score)

#     if score >= 90:
#         print("You got an A")
#         print("Congratulations!")


# print("You did not get an A")


# age = int(input("Enter your age: "))
# if age < 12:
#     print("You are a child.")
# else:
#     if age < 18:
#         print("You are a teenager.")
#     else:
#         if age < 65:
#             print("You are an adult.")
#         else:
#             print("You are a senior citizen.")

# if age < 12:
#     print("You are a child.")
# elif age < 18:
#     print("You are a teenager.")
# elif age < 65:
#     print("You are an adult.")
# else:
#     print("You are a senior citizen.")


# text = input("Enter some text: ")
# result = ""
# if len(text) > 10:
#     result = text[:10]
# else:
#     result = text

# print(f"Result: {result}")

# result = text[:10] if len(text) > 10 else text
# # result = len(text) > 10 ? text[:10] : text

# text = "0123456789abcdefg"

# print(text[:10])
# print(text[2:10])
# print(text[5:])
# print(text[5::3])
# print(text[5:-3:3])
# # print(text[start:end:step])

def f(a):
    print(f"f({a}) called")
    return a
print(f(10) and f("20aaa") or f(30) and f(40) or f(50))
print(f(0) and f(20) and f(30) or f(40) and f([1,2,3]))

l = []
if l:
    print("List is not empty")
else:
    print("List is empty")


l = [1,2,3]
if l:
    print("List is not empty")
else:
    print("List is empty")
    

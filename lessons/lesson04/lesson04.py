# n  = int(input("Enter a number: "))

# while n < 0:
#     print("Please enter a non-negative number.")
#     n = int(input("Enter a number: "))

# print(f"You entered a valid number: {n}")

# while n> 0:
#     print(f"Current value of n: {n}")
#     n -= 1


# l = [1, 2, 3, 4, 5]
# while l:
#     print(f"Current value of l: {l}")
#     l = l[1:]  # Remove the first element from the list

# print("Loop finished. The list is now empty.", l)

# n = 5
# # while n:
# #     print(f"Current value of n: {n}")
# #     n -= 1  # Decrement n by 1
# while n:
#     print(f"Current value of n: {n}")
#     n -= 2  # Decrement n by 1



# l = [1, 2, "test", 4.5, [10, 20], True, None, [1, 2, [4, 5, 6]]]
# for i in l:
#     print(f"Current item: {i}")
#     if isinstance(i, list):
#         print(f"\tFound a list: {i}")
#     elif isinstance(i, str):
#         print(f"\tFound a string: {i}")
#     elif isinstance(i, (int, float)):
#         print(f"\tFound a number: {i}")
#     elif isinstance(i, bool):
#         print(f"\tFound a boolean: {i}")
#     elif i is None:
#         print("\tFound None")
#     else:
#         print(f"\tFound an unknown type: {i}")


# for i in "text":
#     print(f"Current character: {i}")

# for i in 10: TypeError: 'int' object is not iterable
#     print(f"Current number: {i}")

# print(range(10))
# print(list(range(10)))

# for i in range(5):
#     i = 10**i
#     print(f"Current number: {i}")
#     r = range(i)
#     print(f"{r} size:\t{r.__sizeof__()}bytes")
#     l = list(r)
#     print(f"list size:\t{l.__sizeof__()}bytes")

# r = range(10)
# print(f"Range object: {r} {list(r)}")
# r = range(-10)
# print(f"Range object: {r} {list(r)}")
# # r = range[-10] # TypeError: 'range' object is not subscriptable

# r = range(1, 10)
# print(f"Range object: {r} {list(r)}")
# r = range(-11, 10)
# print(f"Range object: {r} {list(r)}")
# # r = range(-11, 10.5) TypeError: 'float' object cannot be interpreted as an integer
# r = range(1, 10, 2)
# print(f"Range object: {r} {list(r)}")
# r = range(1, 10, -2)
# print(f"Range object: {r} {list(r)}")
# r = range(1, -10, -2)
# print(f"Range object: {r} {list(r)}")


# for i in range(1, 10):
#     if i % 2 == 0:
#         print(f"{i} is even")
#     else:
#         print(f"{i} is odd")


# l = [1, 2, 3, 4, 5]
# for i in l:
#     print(f"Current item: {i}")
#     l.append(l[-1]+1)


# l = [1, 2, 3, 4, 5, [1,2], [1,2,3,4]]
# for i in l:
#     print(f"Current item: {i}", end=" => ")
#     if type(i) in [int, float]:
#         i = i**i
#     elif type(i) is list and len(i) <=2:
#         i = i * 3
#     else:
#         i.append(999)
#     print(i)
# print(l)

# l = [1, 2, 3, 4, 5, [1,2], [1,2,3,4]]
# for i in range(len(l)):
#     print(f"l[{i}]={l[i]}" , end=" => ")
#     if type(l[i]) in [int, float]:
#         l[i] = l[i]**l[i]
#     elif type(l[i]) is list and len(l[i]) <=2:
#         l[i] = l[i] * 3
#     else:
#         l[i].append(999)
#     print(l[i])
# print(l)

# value = "my game"
# e = enumerate(value)
# print(e, list(e))
# for elemnt in enumerate(value):
#     print(f"elemnt: {elemnt}")


# a, b, c = 1, 2, 3
# print(a, b, c)
# for index, val in enumerate(value):
#     print(f"value[{index}]={val}")

# from random import randint
# l = [randint(-10, 10) for i in range(10)]
# print(l)
# s = 0
# for element in l:
#     print(f"{element}")
#     if element<=0:
#         continue
#     print(f"sum s={s}=>", end="")
#     s += element
#     print(s)
#     if s>10:
#         break
# print(s)
# s = 0
# while s<10:
#     text = input("text:")
#     if text == "exit":
#         print("break")
#         break
#     if not text.isdigit():
#         continue
#     print(f"\ts {s} => ", end="")
#     s +=int(text)
#     print(s)
# else:
#     print(f"sum: {s}")
# print("end program")

# for i in range(10):
#     pass
#     #ToDo порахувати кількість елеметнів

# def f():
#     line = input()
#     if line.isdigit():
#         return int(line)
#     return True


# while f():
# #     print("text")
# list_name = ["dsvds", "buhdbs"]
# for element in list_name:
#     index = list_name.index(element)
#     print(f"list_name[{index}]={list_name[index]}")

# print(len(list_name))
# print(list_name.__len__())


# for i in range(3):
#     print(f"\ti={i}")
#     for j in range(i):
#         print(f"\t\tj={j}")
#         for k in range(j, i):
#             print("\t\t\t", k)


# l = []
# for i in range(5):
#     i += 1
#     l.append(i)
# print(l)

# l = [i+1 for i in range(5)]
# print(l)

# l = input("list: ").split()
# print(l)
# for e in l:
#     if e.isdigit():
#         s = 0
#         for i in e:
#             s += int(i)
#         else:
#             print(s)

# l = [1, ... ,2]
# print(l)

# f = open("zen.txt")
# print(f.readline())
# print()
# print(f.readlines())
# print()
# f.seek(0)
# f.close()
# with open("zen.txt") as f:
#     print(f.read())
# print(f.read())
# f.seek(0)

# for line in f:
#     print(line)

# 2,
# цикл 1:
#     цикл 2:
#          цикл 3:
#              …

# спочатку найбільш вкладений - цикл 3,
#  який повністю проходить по циклу 2, і все це разом - по циклу 1

for i in range(1, 4):
    print(f"{i=}")
    for j in range(10,40, 10):
        print(f"\t{j=}")
        for k in range(100, 400, 100):
            print(f"\t\t{k=}")
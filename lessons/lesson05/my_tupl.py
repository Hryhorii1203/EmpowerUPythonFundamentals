

# t = tuple()
# print(type(t), t)
# t = tuple("test")
# print(type(t), t)
# t = ()
# print(type(t), t)
# t = (1)
# print(type(t), t)
# t = ("test")
# print(type(t), t)
# t = ("test",)
# print(type(t), t)
# t = ("test",1,1.5)
# print(type(t), t)

# a, b, c = t
# print(f"{a=} {b=} {c=}")

# t = (1,2,3,[10,20,30])
# print(t[0])
# print(t[-1])
# # t[0] = 10 #TypeError: 'tuple' object does not support item assignment
# t[3].append(10)
# print(t)
# # t[3] = [1,2] #TypeError: 'tuple' object does not support item assignment

print([method for method in dir(tuple) if not method.startswith('_')])

# t = (1,2,3, "test", 1)
# print(t.count(1))
# print(t.index("test"))
# from random import randint
# t = tuple(randint(0, 5) for i in range(20))
# print(t)
# n = int(input("n: "))
# i = -1
# for _ in range(t.count(n)):
#     i = t.index(n, i+1)
#     print(i)
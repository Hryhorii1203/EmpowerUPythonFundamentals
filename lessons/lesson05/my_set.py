# s = set()
# print(type(s), s)
# # s = set(1)#TypeError: 'int' object is not iterable
# s = set("testtesttest")
# print(type(s), s)
# s = {}
# print(type(s), s)
# s = {1,2,3,4,2,1,2,34,2,"tes", "tes", "set"}
# print(type(s), s)

print([method for method in dir(set) if not method.startswith('_')])

# s = set()
# s.add("test")
# s.add("test")
# s.add("test2")
# print(s)
# # print(s.pop())
# # print(s)
# # print(s.pop(""))#TypeError: set.pop() takes no arguments (1 given)
# s = {1,2,3,4,5}
# s.remove(5)
# # s.remove("test") KeyError: 'test'
# print(s)

s = {1,2,3,4,5}
s2 = {4,5,"test", 6, 7}
print(s)
s.add("qwerty")
s.add(152)

s.update(s2)
print(s)

text = input("text:")

l = []
# for c in text:
#     if c not in l:
#         l.append(c)

# for c in l:
#     print(f"{c} count:{text.count(c)}")

for c in set(text):
    print(f"{c} count:{text.count(c)}")
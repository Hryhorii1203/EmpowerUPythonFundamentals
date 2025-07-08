l = [
    [1,2,3,4,5],
    (1,2,3,4,5),
    {1,2,3,4,5},
    {1:11,2:22,3:33,4:44,5:55}
]
for con in l:
    print(type(con), con)
    print(f"5 in {5 in con}")
    print(f"6 in {6 in con}")


A =10
_ = 20
C = A*5
print(C)
# list
# d = {
#     []:1
# }
d = {}
d[1] = 1
d[5] = 5
d[2] = 2

print(d)

# list
d = {
    (1,2,3):1
}
# print(d)
# d = {
#     (1,2,[]):1 #TypeError: unhashable type: 'list'
# }
# print(d)
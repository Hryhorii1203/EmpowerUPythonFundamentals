
# # d = dict()
# # print(type(d), d)
# # d = dict([(1,2), ["key", "value"], "ab"])
# # # d = dict([(1,2), ["key", "value",2]]) #ValueError: dictionary update sequence element #1 has length 3; 2 is required
# # print(type(d), d)

# # d = {}
# # print(type(d), d)
# # d = {
# #     "key": 10,
# #     15: "test",
# #     125:152,
# #     16: "test"
# # }
# # print(type(d), d)


# # d = {
# #     "key": 10,
# #     15: "test",
# #     16: 152,
# #     16: "test"
# # }
# # print(type(d), d)


# # print(d[15])
# # print(d["key"])
# # # print(d["key_none"]) #KeyError: 'key_none'
# # d["new_key"] = 15
# # print(d)
# # print([method for method in dir(dict) if not method.startswith('_')])

# # d = {
# #     "key": 10,
# #     15: "test",
# #     125:152,
# #     16: "test"
# # }

# # # print(d.fromkeys("abcd"))
# # # print(d.fromkeys("abcd",10))
# # print(d.get("key"))
# # print(d.get("key_none"))
# # print(d.get("key_none", "temp"))
# # print(d.items())
# # print(d.keys())
# # print(d.values())
# # # print(d.pop())#TypeError: pop expected at least 1 argument, got 0
# # print(d.pop("key"))
# # print(d.popitem())
# # print(d)
# # d.update({
# #     "key2": 2,
# #     "key3": 3

# # })
# # print(d)


# d = { x:x**x for x in range(10)}
# print(d)


# for key in d:
#     print(f"{key} {d[key]}")
# t = (1,2)
# a, b = t
# print(f"{a=} {b=}")
# for key, value in d.items():
#     print(f"{key} {value}")
# l = list()
# print(type(l), l)

# l = list("hello")
# print(type(l), l)

# l = []
# print(type(l), l)

# l = [1, 2, "3", [4, 5], 6.0, "hello"]
# print(type(l), l)  

# l = [1, 2, "3", [4, 5], 6.0, "hello"]

# print(type(l[0]), l[0])  # Accessing the first element
# print(type(l[1]),l[1])  # Accessing the second element
# print(type(l[2]),l[2])  # Accessing the third element
# print(type(l[3]),l[3])  # Accessing the fourth element (which is a list)
# print(type(l[3][0]), l[3][0])  # Accessing the first element of the nested list
# print(type(l[3][1]), l[3][1])  # Accessing the second element of the nested list
# print(type(l[4]), (l[4]))  # Accessing the fifth element
# print(type(l[5]), l[5])  # Accessing the sixth element
# print(type(l[5][1]), l[5][1])  # This will raise an error since 'hello' is a string and has no index 3

# l = [
#     [1,2,3],
#     [4,5,6],
#     [
#         [71, 72, 73],
#         [81, 82, 83],
#         [91, 92, 93]
#     ]
# ]

# print(l[2])
# print(l[2][1])
# print(l[2][1][2])
# print(l[10]) #IndexError: list index out of range

# l = list(range(-10, 10))
# print(l)
# print(l[0])  # Accessing the first element
# print(l[5:10])  # Accessing the second element
# print(l[:10])  # Accessing the second element
# print(l[5:])  # Accessing the second element
# print(l[5::2])  # Accessing the second element
# print(l[::3])  # Accessing the second element
# print(l[:10:3])  # Accessing the second element


# l1 = [1,2,3]
# l2 = [4,5,6]
# print(l1*2)  # Accessing the second element
# print(l1*3)  # Accessing the second element
# print(l1+l2)  # Accessing the second element

# print(dir(list))
print([method for method in dir(list) if not method.startswith('_')])  # List all methods of the list class


# l = []
# l.append(1)
# l.append("text")
# l.append([2, 3])
# print(l)  # Output: [1, 'text', [2, 3]]

# l.clear()  # Clear the list
# print(l)  # Output: []
# l = []

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# l3 = [l1, l2]  # Nested list
# print(l3)  # Output: [[1, 2, 3], [4
# l1.clear()  # Clear the first list
# l2 = []  # Clear the second list
# print(l3, l1, l2) 

# l1 = [1, 2, 3]
# l3 = [1,2,"test", l1] 
# lc = l3.copy()  # Create a shallow copy of l3
# print(id(l3), l3)
# for i in l3:
#     print(f"id(l3[{l3.index(i)}]) = {id(i)}, {i}")
# print(id(lc), lc)
# for i in lc:
#     print(f"id(lc[{lc.index(i)}]) = {id(i)}, {i}")

# l1.append(4)  # Modify l1
# l3[3].append(5)  # Modify the nested list in l3
# l3[0] = 100  # Modify the first element of l3
# lc[1] = 200  # Modify the second element of lc
# print("After modifying l1:")
# print(id(l3), l3)
# print(id(lc), lc)
# import copy
# l4 = copy.deepcopy(l3)  # Create a deep copy of l3
# print(id(l4), l4)
# l3[3].append(5) 

# print(id(l3), l3)
# print(id(l4), l4)

# l = [1, 2, 3, "hello", 4, 5, "test", 6, 7, 8, [6, 7, 8], 9, 10, 6, 5, [6, 7, 8], "hello", "world"]
# # print(l.count(5))  # Count occurrences of 5
# # print(l.count("hello"))  # Count occurrences of "hello" 
# # print(l.count([6, 7, 8]))  # Count occurrences of the list [6, 7, 8]
# # print(l.count(6))  
# print(l.index(6))  
# # print(l.index(66))   #ValueError: 66 is not in list
# print(l.index(6, 7+1))   
# print(l.index(6, 7+1, 10))  #ValueError: 6 is not in list 


# l = [0,1,2,3,4,5,6,7,8,9,10,5,5,5]
# print(l)
# l.insert(5, -5)  # Insert -5 at index 5
# l.insert(500, -500)  # Insert -5 at index 5
# l.insert(-300, -300)  # Insert -5 at index 5

# print(l)

# l.remove(5)  # Remove the first occurrence of 5
# print(l)
# l.remove(5)  # Remove the first occurrence of 5
# l.remove(5)  # Remove the first occurrence of 5
# l.remove(5)  # Remove the first occurrence of 5
# # l.remove(5)  #ValueError: list.remove(x): x not in list
# print(l)
# l.reverse()
# print(l)  # Reverse the list
# r = reversed(l)  # Create a reversed iterator
# print(list(r))  # Convert the iterator to a list
# print(l)  # Convert the iterator to a list

# l.sort()  # Sort the list in ascending order
# print(l)  # Print the sorted list
# l.append("100")
# print(l)  # Print the list after appending "100"
# l.sort()  #TypeError: '<' not supported between instances of 'str' and 'int'

# l = [1, 2, 3, 4, 5]
# l.append("test")
# l.append(500)
# l.append([9, 10])
# print(l)  # Print the list after appending "test"
# l.extend("test")
# l.extend([9, 10])
# print(l)  # Print the list after appending "test"
# print(l.pop())
# print(l)  # Print the list after popping the last element
# print(l.pop(5))  # Pop the first element
# print(l)  # Print the list after popping the last element

# is_true = [1,2,3,4]
# is_true_false = [0,1,3,4]
# is_false = [0,None,False,[],{} ]
# print(all(is_true))  # Check if all elements are truthy
# print(all(is_true_false)) 
# print(all(is_false))  
# print(any(is_true)) 
# print(any(is_true_false)) 
# print(any(is_false))  
# print(list(enumerate(is_true)))  # Enumerate the list
# print(list(enumerate(is_true_false)))  # Enumerate the list
# print(list(enumerate(is_false)))  # Enumerate the list
# print(len(is_true_false))

# l = []
# for i in range(10):
#     l.append(i**2)  # Append squares of numbers from 0 to 9
# print(l)  # Print the list of squares

# l = [i**2 for i in range(10)]  # List comprehension to create a list of squares
# print(l)  # Print the list of squares
l=[]
for i in range(5):
    for j in range(5):
        if i %2 == 0 and j % 2 == 0: 
            l.append((i, j))  # Append tuples of (i, j) to the list
print(l)  # Print the list of tuples
p = [(i, j) for i in range(5) for j in range(5) if i % 2 == 0 and j % 2 == 0]  # List comprehension to create a list of tuples

for i in range(5):
    for j in range(5):
        print(f"{(i, j) in p} {(i, j)} in {p}")
        
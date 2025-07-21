def task_1(a = 1, b = 2):
    print(f'Largest between {a} and {b} is {max(a, b)}')

def task_2(a = 5, h = 10):
    print(f"Area of the triangle is {0.5 * a * h}")
    print(f"Area of the rectangle is {a * h}")
    print(f"Area of the circle is {3.14 * (a / 2) ** 2}")

def task_3(word = "hello"):
    print(f'The word "{word}" has {len(word)} characters.')
    for char in set(word):
        print(f'{char}: {word.count(char)}')
import tasks

def main():
    i = int(input("Enter a task number: "))

    match i:
        case 1:
            print("Executing Task 1 (largest digit between two numbers):")
            print("--------------------------")
            a = int(input('Enter first number: '))
            b = int(input('Enter second number: '))
            tasks.task_1(a=a, b=b)
            print("=======================")
        case 2:
            print("Executing Task 2 (area of figures):")
            print("--------------------------")
            a = int(input('Enter side: '))
            h = int(input('Enter height: '))
            tasks.task_2(a=a, h=h)
            print("=======================")
        case 3:
            print("Executing Task 3 (calculates the number of cgarecters):")
            print("--------------------------")
            word = input('Enter the word: ')
            tasks.task_3(word=word)
            print("=======================")
        case _:
            print("Invalid task number. Please enter 1, 2, or 3.")
            main()
            print("=======================")
   
if __name__ == "__main__":
    main()
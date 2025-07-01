
# status_code = int(input("Enter status code: "))
# if status_code == 400:
#     print("Bad request")
# elif status_code == 401:
#     print("Unauthorized")
# elif status_code == 402:
#     print("Payment required")
# elif status_code == 403:
#     print("Forbidden")
# elif status_code == 404:
#     print("Not found")
# else:
#     print("Other error")

# match status_code:
#     case 400:
#         print("Bad request")
#     case 401:
#         print("Unauthorized")
#     case 402:
#         print("Payment required")
#     case 403:
#         print("Forbidden")
#     case 404:
#         print("Not found")
#     case _:
#         print("Other error")

# # if status_code == 400:
# #     print("Bad request")
# # # elif status_code == 401 or status_code == 402 or status_code == 403:
# # elif status_code in (401, 402, 403):
# #     print(f"Error code {status_code} occurred")
# # elif status_code == 404:
# #     print("Not found")
# # else:
# #     print("Other error")
# # match status_code:
# #     case 400:
# #         print("Bad request")
# #     case 401|402|403 as error_code:
# #         print(f"Error code {error_code} occurred")
# #     case 404:
# #         print("Not found")
# #     case _:
# #         print("Other error")


# values = input("Enter command (load/save): ").split()
# print(f"Values: {values}")
# match values:
#     case "load", link:
#         print(f"Loading from {link}")
#     case "save", link, filename:
#         print(f"Saving {link} to {filename}")
#     case "save", link, *filenames:
#         print(f"Saving {link} to multiple files: {', '.join(filenames)}")
#     case _:
#         print("Unknown command")

# d = [
#     {"time": "morning", "action": "work"},
#     {"time": "afternoon", "action": "eat"},
#     {"time": "evening", "action": "relax333", "extra": "something"},
#     {"time": "evening", "action": "relax"},
#     {"time": "evening", "extra": "something else"}
# ]
# for item in d:
#     match item:
#         case {"time": 'evening', "action": action}:
#             print(f'You almost finished the day! Now {action}!')    
#         case {"time": time, "action": action}:
#             print(f'Good {time}! It is time to {action}!')
#         case _:
#             print('The time is invalid.')


# row = input("Enter a row of numbers: ").split()
# print("Row:", row)
# if not row:
#     print("No numbers entered.")
# else:
#     print("You entered:", row)

# if row:
#     print("You entered:", row)
# else:
#     print("No numbers entered.")

# str
# list 
# s = "Hello, World!"
# s.capitalize()

# print(7^2)  # Bitwise XOR
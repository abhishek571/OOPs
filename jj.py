# # def fibbonaci(n):
# #     fibbonacci_sequence=[0,1]

# #     while len(fibbonacci_sequence)<n:
# #         next_term=fibbonacci_sequence[-1]+fibbonacci_sequence[-2]
# #         fibbonacci_sequence.append(next_term)
# #     return fibbonacci_sequence

# # result=fibbonaci(10)

# # print(result)

# # prime number
# # num = int(input("Enter a Number:"))

# # if num < 2:
# #     print("Please enter a valid number greater than 1")
# # else:
# #     for i in range(2, num):
# #         if num % i == 0:
# #             print(num, "is not a prime number")
# #             break
# #     else:
# #         print(num, "is a prime number")

# def fibbonaci(n):
#     fibbonacci_sequence=[0,1]

#     while len(fibbonacci_sequence)<n:
#          next_term=fibbonacci_sequence[-1]+fibbonacci_sequence[-2]
#          fibbonacci_sequence.append(next_term)
#     return fibbonacci_sequence

# result=fibbonaci(11)
# print(result)

# def sum_of_digits(number):
#     nu1 = 0
    
#     while number > 0:
#         nn = number % 10
#         nu1 += nn
#         number //= 10
    
#     return nu1

# # Example: Find the sum of digits for the number 12345
# number_to_sum = 12345
# result = sum_of_digits(number_to_sum)

# print(f"The sum of digits in {number_to_sum} is {result}")

# string =str(input("enter a string:"))
# print("Original string:",string)

# # Using list comprehension and isdigit() method
# numbers = [int(word) for word in string.split() if word.isdigit()]
# print("After extracting numbers from a string:", numbers)

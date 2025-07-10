# # Find Smallest Number

# list = [6,1,3,4,5]
# print("Original List :", list)
# # sorted_list = list.sort()
# sorted_list = sorted(list)
# print("sorted_list :", sorted_list)
# print("Smallest Number : ", sorted_list[0])
# ------------------------------------------------------

# # Find Largest Number

# List = [1,6,2,8,7,0,6]
# print("Original List : ", List)
# sorted_list = sorted(List)
# print("sorted_list : ", sorted_list)
# print("Largest Number : ", sorted_list[-1])
# ------------------------------------------------------

# Even Numbers

# list = []
# for i in range(25):
#     if i%2 == 0:
#         list.append(i)
# print(list)
# ------------------------------------------------------

# # Odd Numbers

# list = []
# for i in range(25):
#     if i%2 != 0:
#         list.append(i)
# print(list)
# # ------------------------------------------------------

# Prime Numbers

# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def prime_numbers_in_range(start, end):
#     primes = [num for num in range(start, end + 1) if is_prime(num)]
#     return primes

# # Example usage
# start = int(input("Enter start number: "))
# end = int(input("Enter end number: "))
# print(f"Prime numbers between {start} and {end}: {prime_numbers_in_range(start, end)}")




start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

print(f"Prime numbers between {start} and {end} are:")

for num in range(start, end + 1):
    if num > 1:  # Prime numbers are greater than 1
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break  # If divisible, not prime, so break the loop
        if is_prime:
            print(num, end=" ")

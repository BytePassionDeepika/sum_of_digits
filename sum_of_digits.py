def sum_of_digits(num):
    total_sum = 0
    while num > 0:
        total_sum += num % 10
        num //= 10
    return total_sum
number_to_sum = int(input("enter the number:"))
result = sum_of_digits(number_to_sum)

print(f"Number: {number_to_sum}")
print(f"Sum of Digits: {result}")

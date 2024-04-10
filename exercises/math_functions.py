# Given two integer numbers, return their product only if the product is equal to or lower than 100. Otherwise return their sum.
def calculate_sum_or_product(num1, num2):
    product = num1 * num2
    if product <= 1000:
        return product
    return num1 + num2

# Print the sum of the current number and the previous number
def calculate_sum_of_current_and_previous(count):
    for num in range(1, count+1,1):
        print("Current is:", num, "previous is:", num - 1, "Sum is:", num + (num - 1))


# Check if a number is a palindrome number 
def is_palindrome(num):
    if num < 0:
        num *= -1
    reverse = 0
    current = num
    while current != 0:
        remainder = current % 10
        current = current // 10
        reverse = (reverse * 10) + remainder
    return reverse == num

# Write a function that returns int value of base raises to the power of exp
def calculate_exponent(base, exp):
    result = 1
    if exp < 0:
        base = 1 / base
        exp *= -1
    for i in range(exp):
        result *= base
    return result



def generate_even_numbers(start, end):
    even_numbers = []
    for num in range(start, end + 1):
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers
even_numbers_list = generate_even_numbers(4, 30)
print(even_numbers_list)

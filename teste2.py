string_01 = "251"

numbers = string_01.replace("", " ").split()

numbers = map(lambda x: int(x), numbers)

sum_number = sum(numbers)

print(sum_number)

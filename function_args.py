def add_numbers(*args):
    total = 0
    for num in args:
        total = total + num
    return total

total = add_numbers(1, 3, 5, 7, 9)
print(total)


def str_combine(*args):
    new_str = ""
    for word in args:
        new_str = new_str + word
    return new_str

new_str = str_combine("Hello", "World")
print(new_str)
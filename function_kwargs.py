# def person(**kwargs):
#     print(kwargs)
#     print(type(kwargs))

#     if 'age' in kwargs:
#         print("Your age is", kwargs.get("age"))

# person(name="Dude", age=27, brain="big")


def order_pizza(name, address, **toppings):
    print(f"Order for {name}")
    print(f"Ship order to {address}")
    price = 19.00
    for key, value in toppings.items():
        price = price + 2.00
    print(f"The total price is {price}")
    return price

total_price =  order_pizza("Person", "California", jalapenos=True, extra_cheese=True, ham=True)
from shoppingcart import add_to_cart


cart = []

add_to_cart("Laptop", cart)
add_to_cart("Mouse", cart)
add_to_cart("Keyboard", cart)

print("Shopping Cart:")
print(cart)
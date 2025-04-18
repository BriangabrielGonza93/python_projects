print("Welcome to Our Restaurant!")
name = input("May I have your name, please? ")

print("Hello", name, "! Here is our menu:")
print("In starters, we have some suggestions: ")
print("Soup, Salad, Garlic Bread")
print() # for new line

order_starters = input("What would you like for starter? ")

# Add code for the main menu here. Main menu item suggestions include: Steak, Pasta, Burger
print("For the main menu, we have some suggestions: ")
print("Steak, Pasta, Burger")
print() # for new line

order_main_menu = input("What would you like for Main menu? ")

# Add code for dessert here. Dessert item suggestions include: Cake, Ice Cream, Fruit Salad
print("Finally for the dessert, we have some suggestions: ")
print("Cake, Ice Cream, Fruit Salad")
print() # for new line
order_dessert = input("What would you like for Dessert? ")
# Add code for order confirmation here. The output could look like this:
order_confirmation = input("would you like confirmation this order? ")
# Thank you Sara ! I'm repeating your order:
print("Thank you", name, "! I'm repeating your order:")
# Salad for starters
print("For start: ")
print(order_starters)
# Pasta for main menu
print("For main menu: ")
print(order_main_menu)
# Cake for dessert
print("For dessert: ")
print(order_dessert)
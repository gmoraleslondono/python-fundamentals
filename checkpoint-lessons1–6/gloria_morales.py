# ==================================================
# TASK 1
# ==================================================

products = [
    {"name": "Laptop", "price": 12000, "stock": 4},
    {"name": "Mouse", "price": 350, "stock": 0},
    {"name": "Keyboard", "price": 800, "stock": 6},
    {"name": "Monitor", "price": 3200, "stock": 3},
    {"name": "Headset", "price": 950, "stock": 0},
    {"name": "Webcam", "price": 1100, "stock": 5}
]

# 1. Loop through the products.
# 2. Print the name of every product that is in stock.
# 3. Calculate the total value of all products in stock.
#    The value of a product is price * stock.
# 4. Print the total value.
# 5. Keep track of which in-stock product has the highest price
#    without using max(), and print its name.


# Write your solution below:
# 1
# for product in products:
#     print(product)

# 2
# for product in products:
#     if product["stock"] > 0:
#         print(product["name"])

# 3
# for product in products:
#     total_product_value = 0
#     if product["stock"] > 0:
#         total_product_value += product["price"] * product["stock"]
#         print(total_product_value)

# 4
# total_value = 0
# for product in products:
#     if product["stock"] > 0:
#         total_value += product["price"] * product["stock"]

# print(total_value)

# 5
# highest_price = 0
# highest_price_name = ""
# for product in products:
#     if product["stock"] > 0:
#         if product["price"] > highest_price:
#             highest_price = product["price"]
#             highest_price_name = product["name"]

# print(highest_price_name)




# ==================================================
# TASK 2
# ==================================================

scores = [78, 92, 55, 81, 67, 95, 73]

# Create a function called calculate_average that:
# - receives a list of scores
# - calculates and returns the average score
#
# Create another function called create_result that:
# - receives a list of scores
# - uses calculate_average()
# - returns "PASS" if the average is 70 or higher
# - otherwise returns "FAIL"
#
# Call create_result() using the scores above.
# Print both the average score and the final result.


# Write your solution below:

# def calculate_average(list):
#     average = sum(list)/len(list)
#     return average

# def create_result(list):
#     if calculate_average(list) >= 70:
#         return "PASS"
#     return "FAIL"

# print(f"The average score is: {calculate_average(scores)}")
# print(f"The final result is: {create_result(scores)}")




# ==================================================
# TASK 3
# ==================================================

product_prices = [250, 400, 150, 700]

order_settings = {
    "discount": 10,
    "shipping": 49,
    "priority": True
}

# Create a function called calculate_order that:
# - receives a customer name as a normal parameter
# - receives any number of product prices using *args
# - receives optional settings using **kwargs
# - calculates the subtotal of all product prices
# - applies the discount percentage if "discount" exists
# - adds shipping if "shipping" exists
# - returns a dictionary containing:
#       customer
#       subtotal
#       final_total
#       settings
#
# Call the function using:
# - customer name "Anna"
# - the values from product_prices using unpacking
# - the values from order_settings using dictionary unpacking
#
# Print the returned dictionary.


# Write your solution below:
# def calculate_order(name, *args, **kwargs):
#     subtotal = sum(args)
#     discount = subtotal * kwargs.get("discount", 0) / 100
#     shipping = kwargs.get("shipping", 0)
#     final_total = subtotal - discount + shipping
#     return {
#         "customer": name,
#         "subtotal": subtotal,
#         "final_total": final_total,
#         "settings": kwargs}

# print(calculate_order("Anna", *product_prices, **order_settings))




# ==================================================
# TASK 4
# ==================================================

players = [
    {"name": "  anna", "score": 85, "active": True},
    {"name": "DAVID ", "score": 72, "active": False},
    {"name": " sara ", "score": 94, "active": True},
    {"name": "LEO", "score": 67, "active": True},
    {"name": " emma", "score": 88, "active": True},
    {"name": "OSCAR ", "score": 76, "active": False}
]

# 1. Create a new list containing normalized player names.
#    Remove unnecessary whitespace and use consistent capitalization.
#    Use a list comprehension.
#
# 2. Create a new list containing only the active players
#    with a score of 80 or higher.
#    Use a list comprehension.
#
# 3. Sort the original players by score from highest to lowest.
#    Use sorted() with a lambda.
#
# 4. Print the ranking in the following format:
#
#    1. Sara - 94
#    2. Emma - 88
#    ...
#
#    Generate the ranking numbers using enumerate().
#
# 5. Create a separate list containing the player names and
#    another list containing their scores.
#    Combine them using zip() and print each name together
#    with its score.


# Write your solution below:
# 1
# normalized_prayers = [player["name"].strip().title() for player in players]
# print(normalized_prayers)

# 2
active_payers = [player for player in players if player["active"] and player["score"] >= 80 ]
print(active_payers)

# 3
# sorted_players = sorted(players, key=lambda player:player["score"], reverse=True)
# print(sorted_players)

# 4
# sorted_players = sorted(players, key=lambda player:player["score"], reverse=True)
# def print_ranking(list):
#     for position, player in enumerate(list, start=1):
#         print(f"{position}. {player["name"].strip().title()} - {player["score"]}")

# print_ranking(sorted_players)

# 5
# normalized_prayers = [player["name"].strip().title() for player in players]
# scores = [player["score"] for player in players]

# players_and_score = list(zip(normalized_prayers, scores))
# print(players_and_score)


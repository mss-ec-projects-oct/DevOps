# variable Length Arguments *args(Non keyword Arguments)
def order_food(min_order, *args):
    print(f"you have ordered: {min_order}")
    for item in args:
        print(f"you have ordered: {item}")
    print("your food will be delivered in 30 mins: ")
    print("Enjoy the party")

order_food("salad", "pizza", "Biryani", "Soup")

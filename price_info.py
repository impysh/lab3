
price_list={'apple' : 1.20, 'orange':1.40, 'watermelon': 6.50, 'pineapple': 2.70, 'pear' : 0.90, 'papaya': 2.95, 'pomegranate': 4.95 }

quantity_list= {'apple': 5, 'orange':5, 'watermelon': 1, 'pineapple': 2, 'pear' : 10, 'papaya': 1, 'pomegranate': 2}


def total_cost_shopping():
    total_cost = 0
    for key in price_list.keys():
        if key in quantity_list:
            # loops for every key in the list - goes thru each fruit and multiplies its respective price and quantity

            cost = quantity_list[key] * price_list[key]
            # basically multipling the price and quantity of each fruit, as the fruits for both lists are in the same order

            # using [key], basically lets me retrieve the value associated with that key
            # [value] IS NOT A THING!! [key] is the correct term
            total_cost += cost

    print("total cost = ", total_cost)
    return total_cost # for testing purposes


def cost_of_fruits(fruit, quantity):
    for key in price_list.keys():
        if key == fruit:
            cost = quantity*price_list[key]
            break

    print("cost of", quantity, fruit, "=", cost)
    return cost # for testing purposes


def main():

    cost_of_fruits('apple', 10)
    total_cost_shopping()


if __name__ == "__main__":
    main()
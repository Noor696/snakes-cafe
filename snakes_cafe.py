
    
if __name__ == "__main__" : 

 restaurant_MENU = """
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************"""


 rest_orders = {
        "Wings": 0,
        "Cookies": 0,
        "Spring Rolls": 0,
        "Salmon": 0,
        "Steak": 0,
        "Meat Tornado": 0,
        "A literal Garden": 0,
        "Ice Cream": 0,
        "Cake": 0,
        "Pie": 0,
        "Coffee": 0,
        "Tea": 0,
        "Unicorn Tears": 0
    }

 print(restaurant_MENU)

 def menu_order():
    """this is function to take the user order"""
    order =0
    while True:
        order_input = input("> ")

        if order_input == "quit":
            print("Thank You, Bye")
            for i in rest_orders :
                if rest_orders[i]!=0:
                    print (f"your order is : {i} - Quantity : {rest_orders[i]}")
            break
        
        if order_input in rest_orders:
            rest_orders[f'{order_input}']+=1
            if rest_orders[f'{order_input}']==1:
                print(f"** {rest_orders[f'{order_input}']} orders of {order_input} have been added to your meal **")
            else :
                print(f"** {rest_orders[f'{order_input}']} orders of {order_input} have been added to your meal **")
        else :
            print(f"Your order {order_input} is not available in our restaurant ")
        
        
        
        


        order += 1

menu_order()
def login_page():
    for x in range(1, 4):
        tab = "         "
        password = input("Enter system Password\n:")
        if password != "Admin123":
            print("nope".upper())
            trials_left = 3 - x
            print("trials left \a", trials_left)
            if trials_left == 0:
                print("!!!!You are under arrest for exhausting the trials Dummy!!!!".upper())
                break
        elif password == "Admin123":
            print("Welcome".upper())
            # the system should print the items available in the store and the prices
            Items_prices()


def Items_prices():
    while True:
        try:
            itemcode = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
                        26, 27, 28]

            items = ['Kensalt 2kg', "Pembe maize flour 1kg", 'Ajab wheat flour 1kg', 'Pwani Cooking_oil 1 litre',
                     'coffee 100g', 'Eden tea 50g', 'Mafuko Bread 60g', 'Sawa soap 200g', 'Pishori Rice 1kg',
                     'Mumias sugar', 'Vegetables 50g', 'mount kenya milk 500g', 'Mineral Water 500g', 'Indomie 120g',
                     'sphaggetti 200g', 'mayai Dozen', 'tropical heat 90g', 'Royco 100g', 'sauce 500g', 'Cucumber 1kg',
                     'tomato 1kg', 'snacks 500g']

            # itemsdict = {'Maize flour':230, 'Rice':140, 'sugar':170, 'Wheat flour': 200, 'Salt':50, 'Cooking_oil':300, 'soap':100}

            prices = [50, 100, 110, 300, 80, 65, 70, 80, 130, 170, 30, 60, 35, 40, 70, 200, 55, 150, 320, 100, 50, 100]

            tab = "         "

            # for k,v in itemsdict.items():
            # print(k,tab,v)
            amount_2_pay = 0
            count = 0
            customer_items = []
            customer_price = []
            customer_itemcode = []
            decorations = '<&&&&%%%%%$$$$$$$$$$$%%%%%%%&&&&&&>'

            while True:
                print(decorations * 2)
                print(tab * 2, 'dkut pos system'.upper())
                print(decorations * 2)

                option = int(input("""
                    1. ADD AN ITEM
                    2. MAKE PAYMENT
                    3. DISPLAY RECEIPT



                    Choose an option\n:"""))
                if option == 1:
                    try:
                        print('To make payment press enter'.upper())
                        print("\nSTOCKED ITEMS\n")
                        print("ITEM CODE", tab, "ITEM & QUANTITY", tab, 'PRICES')

                        for x in range(len(items)):
                            print(itemcode[x], tab, items[x], tab, 'kshs', prices[x])
                        item_choice = int(input("type in the item code for the item you want to buy:\n"))
                        customer_items.append(items[item_choice])
                        customer_price.append(prices[item_choice])
                        customer_itemcode.append(itemcode[item_choice])
                        amount_2_pay += prices[item_choice]
                        count += 1
                    except:
                        print('ERROR 1 !!!!\nItem not in the list ')
                        continue


                elif option == 2:
                    try:
                        if amount_2_pay <= 0:
                            print('nothing to count here yet'.upper())
                            continue
                        print('Item_code', end=tab)
                        print('Quantity', end=tab)
                        print('Unit_Price', end=tab * 2)
                        print('total price')
                        for c in range(count):
                            print(customer_itemcode[c], tab, customer_items[c], tab, 'Kshs', customer_price[c], tab *2 , customer_price[c])

                        print(
                            '*************************************************************************************************')
                        print('Total amount to paid by the customer:_________________ ', amount_2_pay)
                        print(
                            '*************************************************************************************************')
                        customer_pay = int(input('Enter the amount issued by the customer___________'))
                        change = customer_pay - amount_2_pay
                        if change < 0:
                            print("\nNot enough Amount!!!!\n\n".upper())
                            continue
                        print(
                            '*************************************************************************************************')
                        print('change =_________________________________ Kshs ', change)
                        print('Thank You for Shopping with us'.upper())
                        input('press enter to serve another customer'.upper())
                        break
                    except:
                        print('error 2!!!!'.upper())
                        continue

                elif option == 3:
                    if amount_2_pay <= 0:
                        print('nothing to count here yet'.upper())
                        continue
                    print('YOU BOUGHT THE FOLLOWING ITEMS')
                    for c in range(count):
                        print(customer_items[c], customer_price[c])
                    continue
                else:
                    continue
        except:
            print("error in input!!!!! system reboot".upper())
            continue


login_page()

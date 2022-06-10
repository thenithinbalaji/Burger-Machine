burgers_available = {"A": 20, "B": 20, "C": 10, "D": 30} #burger initialisation dict

def time_needed(list):
    time = 0
    for i in list:
        time = time + burgers_available[i]
    
    return time


print("Burgers Available::")
for burger in burgers_available.keys():
    print("Burger ", burger, "-", burgers_available[burger], "mins to cook")

choice = 1 #default choice
choice_list = [1,2,3] #menu options
order_queue = [] #contains order

while choice in choice_list: 
    choice = int(input("\nMENU:: \n1 for choosing burger \n2 for viewing your orders \n3 for finalising orders \nAny other number for exiting \nEnter your choice:: "))

    if(choice == 1):
        burger_type = input("Enter Burger Type:: ")
        if(burger_type not in burgers_available.keys()):
            print("\nInvalid Burger Name")
        
        else:
            order_queue.append(burger_type)
            print("\nBurger",burger_type, "was added to cart")
    
    elif(choice == 2):
        if(len(order_queue) > 0):
            print("\nYour Orders:: ")
            count = 1
            for burger in order_queue:
                print("Order No:", count, " - ", burger)
                count = count + 1
        else:
            print("\nNo orders made")

    elif(choice == 3):
        print("\nOrder Finalised")
        print("Cooking", len(order_queue), "Orders")
        break

    else:
        print("\nExiting Burger System")
        print("Order Finalised")
        print("Cooking", len(order_queue), "Orders")


number_of_ovens = int(input("\n\nEnter number of burger machines present in the kitchen:: "))
if(number_of_ovens <= 0):
    number_of_ovens = 1

print("\nStarted cooking", len(order_queue), "burgers in", number_of_ovens, "ovens. Please wait while we estimate the time needed.")        

type_of_ds = int(input("\nEnter 1 for solving using queues, Enter 2 for solving using priority queue:: "))

if(type_of_ds == 1):
    cooking = {}
    
    if(number_of_ovens >= len(order_queue)):
        print("\nTotal Time required to complete the orders = ", end = "")
        max_time = 0
        for i in order_queue:
            if(burgers_available[i] > max_time):
                max_time = burgers_available[i]
        
        print(max_time)

    else:

        oven =  1
        for burger in order_queue:
            if(len(cooking.keys()) < number_of_ovens):
                cooking[oven] =  [burger]
                oven = oven + 1

            else:
                time = 9999
                for i in cooking.keys():
                    if(time_needed(cooking[i]) < time):
                        min_oven = i
                        time = time_needed(cooking[i])
                
                cooking[min_oven] = cooking[min_oven] + [burger]

        print(cooking)  
        #cooking will have the burgers and their respective oven number in which they are cooked
        #after all the ovens are full, the next burger is addded to the oven with burger that cooks in min time
        max_time = 0
        for i in cooking.keys():
            if(time_needed(cooking[i]) > time):
                max_time = time_needed(cooking[i])


        print("\nTotal Time required to complete the orders = ", max_time)
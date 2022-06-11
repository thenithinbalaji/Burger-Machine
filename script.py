import heapADT as heapq

burgers_available = {
    "CHICKENS DOUBLE PATTY with ONION and PEPSI": 14,
    "CHICKENS DOUBLE PATTY with ONION and TIPSY": 12,
    "CHICKENS DOUBLE PATTY with CHILLI and PEPSI": 10,
    "CHICKENS DOUBLE PATTY with CHILLI and TIPSY": 8,
    "CRISPY DOUBLEER PATTY with ONION and PEPSI": 5,
    "CRISPY DOUBLEER PATTY with ONION and TIPSY": 6,
    "CRISPY DOUBLEER PATTY with CHILLI and PEPSI": 7,
    "CRISPY DOUBLEER PATTY with CHILLI and TIPSY": 8,
    "SMOKY GRILLED CHICKEN with ONION and PEPSI": 20,
    "SMOKY GRILLED CHICKEN with ONION and TIPSY": 18,
    "SMOKY GRILLED CHICKEN with CHILLI and PEPSI": 22,
    "SMOKY GRILLED CHICKEN with CHILLI and TIPSY": 24,
}


def time_needed1(list):
    time = 0
    for i in list:
        time = time + burgers_available[i]

    return time


def time_needed2(list):
    time = 0

    for btime, bname in list:
        time = time + btime

    # print(list, time)
    return time


def burger_machine2(order_queue=[], number_of_ovens=1):
    order_queue2 = []
    for i in order_queue:
        order_queue2.append((burgers_available[i], i))

    # print(order_queue2)

    heapq._heapify_max(order_queue2)
    # print(order_queue2)

    cooking = {}

    if number_of_ovens >= len(order_queue):
        max_time = 0
        for i in order_queue:
            if burgers_available[i] > max_time:
                max_time = burgers_available[i]

        print("\nTotal Time required to complete the orders = ", max_time)

    else:
        oven = 1
        while len(order_queue2) > 0:
            burger = heapq._heappop_max(order_queue2)
            if len(cooking.keys()) < number_of_ovens:
                cooking[oven] = [burger]
                oven = oven + 1

            else:
                time = 9999
                for i in cooking.keys():
                    if time_needed2(cooking[i]) < time:
                        min_oven = i
                        time = time_needed2(cooking[i])

                cooking[min_oven] = cooking[min_oven] + [burger]

        print(cooking)

        # cooking will have the burgers and their respective oven number in which they are cooked
        # after all the ovens are full, the next burger is addded to the oven with burger that cooks in min time

        max_time = 0
        for i in cooking.keys():
            if time_needed2(cooking[i]) > max_time:
                max_time = time_needed2(cooking[i])

        print("\nTotal Time required to complete the orders = ", max_time)

    return max_time


def burger_machine1(order_queue=[], number_of_ovens=1):
    cooking = {}

    if number_of_ovens >= len(order_queue):
        max_time = 0
        for i in order_queue:
            if burgers_available[i] > max_time:
                max_time = burgers_available[i]

        print("\nTotal Time required to complete the orders = ", max_time)

    else:
        oven = 1
        for burger in order_queue:
            if len(cooking.keys()) < number_of_ovens:
                cooking[oven] = [burger]
                oven = oven + 1

            else:
                time = 9999
                for i in cooking.keys():
                    if time_needed1(cooking[i]) < time:
                        min_oven = i
                        time = time_needed1(cooking[i])

                cooking[min_oven] = cooking[min_oven] + [burger]

        print(cooking)

        # cooking will have the burgers and their respective oven number in which they are cooked
        # after all the ovens are full, the next burger is addded to the oven with burger that cooks in min time

        max_time = 0
        for i in cooking.keys():
            if time_needed1(cooking[i]) > max_time:
                max_time = time_needed1(cooking[i])

        print("\nTotal Time required to complete the orders = ", max_time)

    return max_time


def burger_god(order_queue=[], number_of_ovens=1):
    return burger_machine1(order_queue, number_of_ovens), burger_machine2(
        order_queue, number_of_ovens
    )


# if __name__ == "__main__":
#     order_queue =  [
#     ]
#     number_of_ovens = 1

#     print(burger_god(order_queue, number_of_ovens))

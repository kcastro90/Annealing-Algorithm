__author__ = 'karic_000'
import random
import math


def search_map():
    """This part is used to find the occupied regions of the map representing a location in the
    BSU map and to identify the coordinates' representations."""

    location_options = []
    path = []
    path2 = []  # Second path option with swapped elements

    #              [1 , 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18]
    location_map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # A
                    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # B
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # C
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # D
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],  # E
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # F
                    [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # G
                    [0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],  # H
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # I
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # J
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]  # K

    index_in_matrix = 0  # Keeps track of index in matrix, and total elements (198 of them)
    row_index = 0   # Keeps track of row number during loop
    for row_letter in location_map:
        for number_index in row_letter:
            index_in_row = index_in_matrix - (18*row_index)  # # Keeps track of index in row
            if number_index == 1:  # If position is occupied
                location_options.append([row_index, index_in_row])  # Create a list out of them
            index_in_matrix += 1
        row_index += 1
    print("Location options:", location_options)

    # Now create a random path to optimize
    while len(path) < len(location_options):  # from 0 - 10 (0<11)
        i = random.randint(0, 10)  # 11 options
        if location_options[i] not in path:  # Assure no items are being repeated
            path.append(location_options[i])
            path2.append(location_options[i])

    print("This will be the randomly chosen path to be optimized:")
    for element in path:
        letter = element[0]
        number = element[1]
        index_to_name(letter, number)
    print("It will be represented by the following coordinates:", path)

    global_best_euclidean = 100  # A worst case starting value for the algorithm to fix
    euclidean1 = 0
    euclidean2 = 0
    best_euclidean = 100
    step = 0  # Will hold which cycle was the best path found on

    for cycles in range(1000):  # 1000 cycles were the chose max iteration to find the best path
        already_seen_order = []
        good_random = True

        while good_random:
            random_int1 = random.randint(0, 10)
            random_int2 = random.randint(0, 10)
            if random_int2 != random_int1:  # Assure that both indices aren't the same
                swap = list(path)  # Clones the immutable list
                swap[random_int1], swap[random_int2] = path[random_int2], path[random_int1]
                # Swap items and assign new list "swap" to path2
                path2 = swap

                if path2 not in already_seen_order:
                    # Add path that hasn't been seen before to list so there are no repeated paths
                    if path2 not in already_seen_order:
                        already_seen_order.append(path2)
                    if path not in already_seen_order:
                        already_seen_order.append(path)
                good_random = False

        i, j = 0, 1  # Keeps up with current index and the next
        for element in path:
            if i <= 9:
                x1, x2 = element[0], element[1]
                _next = path[j]
                y1, y2 = _next[0], _next[1]
                euclidean1 += (math.sqrt(((x1-y1)**2) + ((x2-y2)**2)))
            if i < 9:
                i += 1
                j += 1
        i, j = 0, 1
        for element in path2:
            if i <= 9:
                x1, x2 = element[0], element[1]
                _next = path2[j]
                y1, y2 = _next[0], _next[1]
                euclidean2 += (math.sqrt(((x1-y1)**2) + ((x2-y2)**2)))
            if i < 9:
                i += 1
                j += 1
        # print("path1:", path,"path2:", path2, euclidean1, euclidean2)
        if (euclidean1 < best_euclidean) and (euclidean1 < euclidean2):
            best_euclidean = euclidean1

        if (euclidean2 < best_euclidean) and (euclidean2 < euclidean1):
            path = list(path2)  # Path 1 is always the best path
            best_euclidean = euclidean2
        # print("Best local Euclidean Distance is:", best_local)
        if best_euclidean < global_best_euclidean:
            global_best_euclidean = best_euclidean
            step = cycles
        euclidean1, euclidean2, i, j = 0, 0, 0, 0  # Resets values so it won't affect next loop

    print("The best path was found in cycle number:", step+1)  # Increment 1 to count ZERO step
    print("\nTHE BEST GLOBAL EUCLIDEAN VALUE:", global_best_euclidean) 
    print("\nThe best chosen path was found to be in the following order:")
    for element in path:
        letter = element[0]
        number = element[1]
        index_to_name(letter, number)


def index_to_name(letter, number):

    if letter == 6 and number == 1:
        print("Gates House")
    if letter == 7 and number == 9:
        print("Grimson Hall")
    if letter == 2 and number == 9:
        print("Hooper St. Lot")
    if letter == 1 and number == 4:
        print("Spring St. Lot")
    if letter == 6 and number == 5:
        print("Kelly Gymnasium")
    if letter == 7 and number == 2:
        print("Woodard Hall")
    if letter == 4 and number == 9:
        print("Burnell Hall")
    if letter == 4 and number == 11:
        print("Tinsley Center")
    if letter == 7 and number == 10:
        print("East Campus Commons")
    if letter == 7 and number == 4:
        print("Davis Alumni Center")
    if letter == 6 and number == 9:
        print("Burril Office Complex")


search_map()

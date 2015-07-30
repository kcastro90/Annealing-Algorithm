__author__ = 'karic_000'
import random
import math


def search_map():
    """This part is used to find the occupied regions of the map representing a location in the
    BSU map and to identify the coodinates' representations."""
    cycles = 1  # Keeps track of how many times the let_d_alg... ran until it found the best path
    a, b, c, d, e, f, g, h, i, j, k = 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'
    letters = (a, b, c, d, e, f, g, h, i, j, k)

    g2, h10, c10, b3, g6, h3, e10, e12, h11, h5, g10 = ('Gates House', 'Grimson Hall',
                                                        'Hooper St. Lot', 'Spring St. Lot',
                                                        'Kelly Gymnasium', 'Woodard Hall',
                                                        'Burnell Hall', 'Tinsley Center',
                                                        'East Campus Commons',
                                                        'Davis Alumni Center',
                                                        'Burril Office Complex')
    places = (g2, h10, c10, b3, g6, h3, e10, e12, h11, h5, g10)

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
    best_local = 0
    for row_letter in location_map:
        for number_index in row_letter:
            index_in_row = index_in_matrix - (18*row_index)  # # Keeps track of index in row
            if number_index == 1:  # If position is occupied
                # print("Row number:", row_index+1, "Column number:", index_in_row+1)
                row_index_to_letter(row_index, a, b, c, d, e, f, g, h, i, j, k)

                location_options.append([row_index, index_in_row])
                # print("Location's coordinates:", letters[row_index], index_in_row+1)

                # Identify coordinates with locate_name
                locate_name(letters[row_index], row_index)
                # print("Letter:", letters[row_index], "Numbers:", row_index, "Index:", row_index)
                # print("Place name:", places[row_index], "\n")

            index_in_matrix += 1
        row_index += 1
    # print("Location options:", location_options)

    # Now create a random path to optimize
    while len(path) < len(location_options):  # from 0 - 10 (0<11)
        i = random.randint(0, 10)  # 11 options
        if location_options[i] not in path:  # Assure no items are being repeated
            path.append(location_options[i])
            path2.append(location_options[i])

    print("This will be the randomly chosen path to be optimized:", path)

    global_best_euclidean = 100
    euclidean1 = 0
    euclidean2 = 0
    best_euclidean = 100
    best_path = []

    for cycles in range(2):
        ##########################################################
        #############################CHANGE BACK TO 1000
        already_seen_order = []
        good_random = True

        while good_random == True:
            random_int1 = random.randint(0, 10)
            random_int2 = random.randint(0, 10)
            if random_int2 != random_int1:
                print("print random int", random_int1, random_int2)
                """ Swap items for second list,
                Check if order is in already seen, if not, then it's a new path to test."""
                path2[random_int1], path2[random_int2] = path2[random_int1], path2[random_int2]

                if path2 not in already_seen_order:
                    """ They both start the same and path2 is always the new
                    option so no need to check both paths.
                    Make sure to add the any path that hasn't been seen before to the list."""
                    if path2 not in already_seen_order:
                        already_seen_order.append(path2)
                    #if path not in already_seen_order:
                        #already_seen_order.append(path)
                    #path2[random_int1], path2[random_int2] = path2[random_int1], path2[random_int2]
            path2[random_int1], path2[random_int2] = path2[random_int1], path2[random_int2]
            good_random = False
             # Swap
        i = 0  # Keeps up with the index so it doesn't exceed the number of elements in list
        j = 1  # Keeps up with the index of the next element

        print("path1:", path)
        for element in path:
            if i <= 9:
                x1, x2 = element[0], element[1]
                _next = path[j]
                y1, y2 = _next[0], _next[1]
                euclidean2 += (math.sqrt(((x1-y1)**2) + ((x2-y2)**2)))
            if i < 9:
                i += 1
                j += 1
        print("path2:", path2)
        for element in path2:
            if i <= 9:
                x1, x2 = element[0], element[1]
                _next = path2[j]
                y1, y2 = _next[0], _next[1]
                euclidean2 += (math.sqrt(((x1-y1)**2) + ((x2-y2)**2)))
            if i < 9:
                i += 1
                j += 1
        print(euclidean1, euclidean2)
        if (euclidean1 < best_euclidean) and (euclidean1 < euclidean2):
            #path = path1
            best_euclidean = euclidean1
            # print("Best local random path chosen was:", path_copy)
            best_local = best_euclidean
        if (euclidean2 < best_euclidean) and (euclidean2 < euclidean1):
            #path = path2  # Path 1 is always the best path
            best_euclidean = euclidean2
            # print("Best local random path chosen was:", path_copy)
            best_local = best_euclidean
            #euclidean1, euclidean2 = 0, 0  # Reset variables for next check
            print("The best local local Euclidean Distance is:", best_local)
            # print("Best path:", path)
            if best_euclidean < global_best_euclidean:
                global_best_euclidean = best_euclidean
                print("cycle number for best path", cycles)

        print("GLOBAL BEST EUCLIDEAN VALUE:", global_best_euclidean)  # Cycles:", cycles


def row_index_to_letter(index, a, b, c, d, e, f, g, h, i, j, k):
    letter = None
    if index == 0:
        letter = a
    if index == 1:
        letter = b
    if index == 2:
        letter = c
    if index == 3:
        letter = d
    if index == 4:
        letter = e
    if index == 5:
        letter = f
    if index == 6:
        letter = g
    if index == 7:
        letter = h
    if index == 8:
        letter = i
    if index == 9:
        letter = j
    if index == 10:
        letter = k
    return letter


def locate_name(letter, number):

    if letter == 'G' and number == 2:
        number = 0
        return number
    if letter == 'H' and number == 10:
        number = 1
        return number
    if letter == 'C' and number == 10:
        number = 2
        return number
    if letter == 'B' and number == 3:
        number = 3
        return number
    if letter == 'G' and number == 6:
        number = 4
        return number
    if letter == 'H' and number == 3:
        number = 5
        return number
    if letter == 'E' and number == 10:
        number = 6
        return number
    if letter == 'E' and number == 12:
        number = 7
        return number
    if letter == 'H' and number == 11:
        number = 8
        return number
    if letter == 'H' and number == 5:
        number = 9
        return number
    if letter == 'G' and number == 10:
        number = 10
        return number



"""def locate_name2(letter, number):

    if letter == 7 and number == 1:
        print("Gates House")
    if letter == 8 and number == 10:
        print("Grimson Hall")
    if letter == 3 and number == 10:
        print("Hooper St. Lot")
    if letter == 2 and number == 3:
        print("Spring St. Lot")
    if letter == 7 and number == 6:
        print("Kelly Gymnasium")
    if letter == 8 and number == 3:
        print("Woodard Hall")
    if letter == 5 and number == 10:
        print("Tinsley Center")
    if letter == 5 and number == 12:
        print("East Campus Commons")
    if letter == 8 and number == 11:
        print("Davis Alumni Cente")
    if letter == 8 and number == 5:
        print("Davis Alumni Center")
    if letter == 7 and number == 10:
        print("Burril Office Complex")
"""
search_map()
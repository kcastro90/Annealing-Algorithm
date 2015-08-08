__author__ = 'karic_000'
import random
import math
import copy


def search_map():
    """This part is used to find the occupied regions of the map representing a location in the
    BSU map and to identify the coordinates' representations."""
    cycles = 1  # Keeps track of how many times method "let_d_alg" ran until it found the best path
    a, b, c, d, e, f, g, h, i, j, k = 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'
    letters = (a, b, c, d, e, f, g, h, i, j, k)

    g2, h10, c10, b5, g6, h3, e10, e12, h11, h5, g10 = ('Gates House', 'Grimson Hall',
                                                        'Hooper St. Lot', 'Spring St. Lot',
                                                        'Kelly Gymnasium', 'Woodard Hall',
                                                        'Burnell Hall', 'Tinsley Center',
                                                        'East Campus Commons',
                                                        'Davis Alumni Center',
                                                        'Burril Office Complex')
    places = (g2, h10, c10, b5, g6, h3, e10, e12, h11, h5, g10)

    location_options = []
    path_order = []
    path2 = []
    #global_best_euclidean = 100  # Pretend worst case scenario of Euclidean Distance of 100
    #best_euclidean = 0  # The return value will replace this value
    already_seen_order = []

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
                """ print("Row number:", row_index+1, "Column number:", index_in_row+1)
                row_index_to_letter(row_index, a, b, c, d, e, f, g, h, i, j, k)
                Commented out area of the program. Unsure if this part will be used
                at all. Possibly not in this assignment."""

                location_options.append([row_index, index_in_row])
                # print("Location's coordinates:", letters[row_index], index_in_row+1)

                # Identify coordinates with locate_name
                # locate_name(letters[row_index], row_index)
                # print("Letter:", letters[row_index], "Numbers:", row_index, "Index:", row_index)
                # print("Place name:", places[row_index], "\n")

            index_in_matrix += 1
        row_index += 1
    print("Location options:", location_options)

    # Now create a random path to optimize
    while len(path_order) < len(location_options):  # from 0 - 10
        i = random.randint(0, 10)  # 11 options
        if location_options[i] not in path_order:  # Assure no items are being repeated
            path_order.append(location_options[i])

    print("This will be the randomly chosen path to be optimized:", path_order)
    # best_euclidean = copy.local_euclidean
    global_best_euclidean = 100.00
    for cycles in range(5):
        ##############################################
        #############################CHANGE BACK TO 1000
        #step = cycles
        let_d_alg_begin(path_order, path2, global_best_euclidean, already_seen_order)
        local_euclidean = global_best_euclidean
        if local_euclidean < global_best_euclidean:
            global_best_euclidean = copy(local_euclidean)
            # best_euclidean = local_euclidean
            print("Potential global best value found at step", cycles)
    print("local_euclidean", local_euclidean)
    print("GLOBAL BEST EUCLIDEAN VALUE:", global_best_euclidean)

    print("\nThe best chosen path was found to be in the following order:")
    for element in path_order:
        letter = element[0]
        number = element[1]
        index_to_name(letter, number,)


def let_d_alg_begin(path, path2, best_local, already_seen_order):

    good_random = True
    while good_random:
        random_int1 = random.randint(0, 10)
        random_int2 = random.randint(0, 10)

        if random_int2 != random_int1:
            swap = list(path)
            swap[random_int1], swap[random_int2] = path[random_int2], path[random_int1]
            # Swap items and have path2 be that new list
            path2 = swap

            if path2 not in already_seen_order:
                # Make sure to add the any path that hasn't been seen before to the list
                if path2 not in already_seen_order:
                    already_seen_order.append(path2)
                if path not in already_seen_order:
                    already_seen_order.append(path)
            good_random = False

    get_euclidean_distance(path, path2, best_local)
    print("best_euclidean in let d alg..", best_local)
    return path, path2, best_local


def get_euclidean_distance(best_path, path2, best_local):
    i = 0  # Keeps up with the index so it doesn't exceed the number of elements in list
    j = 1  # Keeps up with the index of the next element
    euclidean1 = 0
    euclidean2 = 0
    best_euclidean = best_local
    path = list(best_path)  # Clones list

    for element in path:
        if i <= 9:
            x1, x2 = element[0], element[1]
            _next = path[j]
            y1, y2 = _next[0], _next[1]
            euclidean1 += (math.sqrt(((x1-y1)**2) + ((x2-y2)**2)))
        if i < 9:
            i += 1
            j += 1
    # print("path1:", path)
    for element in path2:
        if i <= 9:
            x1, x2 = element[0], element[1]
            _next = path2[j]
            y1, y2 = _next[0], _next[1]
            euclidean2 += (math.sqrt(((x1-y1)**2) + ((x2-y2)**2)))
        if i < 9:
            i += 1
            j += 1
    # print("path2:", path2)
    print(euclidean1, euclidean2)

    if (euclidean1 < best_euclidean) and (euclidean1 < euclidean2):
        best_euclidean = euclidean1
    if (euclidean2 < best_euclidean) and (euclidean2 < euclidean1):
        best_path = list(path2)  # "best_path or path1 will always be the returned "best path"
        best_euclidean = euclidean2
    best_local = best_euclidean
    print("The best local Euclidean Distance is:", best_local, "\nBest path:", best_path)
    return best_path, best_local



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
    if letter == 'B' and number == 5:
        number = 4
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

    g2, h10, c10, b3, g6, h3, e10, e12, h11, h5, g10 = ('Gates House', 'Grimson Hall',
                                                        'Hooper St. Lot', 'Spring St. Lot',
                                                        'Kelly Gymnasium', 'Woodard Hall',
                                                        'Burnell Hall', 'Tinsley Center',
                                                        'East Campus Commons',
                                                        'Davis Alumni Center',
                                                        'Burril Office Complex')
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

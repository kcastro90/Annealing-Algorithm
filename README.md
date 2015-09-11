# Annealing-Algorithm
    This program simulates a map for Bridgewater State University. A list called "location_map" holds a 2-dimentional matrix 
representing which rows and columns hold a location, shown with a number 1. Empty locations are the zeroes.
    First locations are found, then the locations are randomly picked for an initial path. It then uses an annealing algorithm, 
with a maximum amount of 1000 cycles for this program, and it looks for the shortest eucliden distance for a path. Each time 
there is a location swap, it checks if that path's Euclidean Distance is smaller/better, and if so, that swap will be kept, 
if not it keeps cycling through the process.
    Once it reaches the 1000th cycle the program will stop, but the best path may be found prior to that. The cycle number is 
stored and then printed along with the best path once the algorithm runs for the last time.

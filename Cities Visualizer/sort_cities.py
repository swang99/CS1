# name: Stephen Wang
# date: November 7, 2020
# purpose: Quicksort algorithm to sort cities by alphabet, population, and latitude

from city import City

# -- quicksort.py algorithm --
def partition(the_list, p, r, compare_func):
    pivot = the_list[r]
    i = p - 1
    j = p

    for k in range(p, r):
        if compare_func(the_list[k], pivot):
            i += 1
            the_list[i], the_list[j] = the_list[j], the_list[i]
        j += 1
    the_list[r], the_list[i+1] = the_list[i+1], the_list[r]
  
    return i + 1

def quicksort(the_list, p, r, compare_func):
    if r > p:
        q = partition(the_list, p, r, compare_func)
        quicksort(the_list, p, q-1, compare_func)
        quicksort(the_list, q+1, r, compare_func)

def sort(the_list, compare_func):
    quicksort(the_list, 0, len(the_list)-1, compare_func)

def compare_city_names(c1, c2):
    return compare_items(c1.name.lower(), c2.name.lower())

def compare_city_pops(c1, c2):
    return compare_items(c2.population, c1.population)

def compare_city_lats(c1, c2):
    return compare_items(c1.latitude, c2.latitude)

def compare_items(a, b):
    if a <= b:
        return True
    else:
        return False

# list of references to City objects
cities = []

# read into world_cities.txt
r_file = open("world_cities.txt", "r")

for line in r_file:
    city2 = line.strip().split(",")
    cities.append(City(city2[0], city2[1], city2[2], city2[3], city2[4], city2[5]))

r_file.close()

# -- open files to write into -- 
w_file = open("cities_alpha.txt", "w")
w2_file = open("cities_population.txt", "w")
w3_file = open("cities_latitude.txt", "w")

# alphabetize cities
sort(cities, compare_city_names)
for city in cities:
    w_file.write(str(city) + "\n")
w_file.close()

# sort cities by population
sort(cities, compare_city_pops)
for city in cities:
    w2_file.write(str(city) + "\n")
w2_file.close()

# sort cities by latitude
sort(cities, compare_city_lats)
for city in cities:
    w3_file.write(str(city) + "\n")
w3_file.close()
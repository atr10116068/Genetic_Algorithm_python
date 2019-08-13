from genlogic import create_gen
from calculate_fitness import fitness
from create_population import create_population
from selection import selection

#ord(n) [string to ascii]
#chr(n) [ascii to string]

target = 'abcdeaabcccce'
besar_populasi = 4
populasi = create_population(target,besar_populasi)

print(str(selection(populasi)))

def selection(populasi):
    #individu terbaik
    fitness_data = []
    for i in range(len(populasi)):
        fitness_data.append(populasi[i])
    #mencari indexnya max value
    indek = []
    for i in fitness_data:
        indek.append(float(i['fitness']))
        
    parentIndex = indek.index(max(indek))
    parent1=populasi[parentIndex]
    indek[parentIndex]=0.0

    parentIndex2 = indek.index(max(indek))
    parent2=populasi[parentIndex2]
    indek[parentIndex]=0.0

    otput={
        'best1':parent1,
        'best2':parent2
    }

    return otput

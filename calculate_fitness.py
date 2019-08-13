
#function fitnes
def fitness(gen,target):
    fitnes=0
    for x in range(len(target)):
        if(target[x:x+1] == gen[x:x+1]):
            #print("-> {} sama".format(gen[x:x+1]))
            fitnes += 1
    fitness = str((fitnes/len(target))*100)
    return fitness

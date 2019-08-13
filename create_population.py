from genlogic import create_gen
from calculate_fitness import fitness

def create_population(target,besar_populasi):
    populasi={}
    for i in range(besar_populasi):
        gen = create_gen(len(target))
        populasi[i]={
            'gen': gen,
            'fitness':fitness(gen,target)
        }
        #print('target\t\t: '+target)
        #print('gen_baru\t: '+gen)
        #print('fitness\t\t: '+fitness(gen,target))
        #print()
    return populasi
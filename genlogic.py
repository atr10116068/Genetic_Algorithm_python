from random import randint

#representasi genetik
def create_gen(panjang_gen):
    gen = ""
    for x in range(panjang_gen):
        gen += chr(randint(97,101))
    return gen
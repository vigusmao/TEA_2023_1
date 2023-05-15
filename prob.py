from random import random

REPETICOES = 100000

# legibilidade
HONESTA = 0
FALSA = 1
CARA = 0
COROA = 1

DISTRIB_FALSA = 0.1


# probs condicionais
pr_cara_dado_viciada = 1
pr_coroa_dado_viciada = 1 - pr_cara_dado_viciada

pr_cara_dado_honesta = 0.5
pr_coroa_dado_honesta = 1 - pr_cara_dado_honesta


def sortear_moeda_da_urna():
    return FALSA if random() < DISTRIB_FALSA\
                 else HONESTA 

def lancar_moeda(moeda):
    r = random()
    if moeda == HONESTA:
        return CARA \
            if r < pr_cara_dado_honesta \
            else COROA   
    # FALSA:
    return CARA \
        if r < pr_cara_dado_viciada \
        else COROA 
  

moeda = sortear_moeda_da_urna()
print "sorteada foi", "honesta" if moeda==HONESTA\
                                else "viciada"

# modelo de crencas
pr_viciada = 0.8


cont = 0
print cont, "--- Pr{falsa} =", pr_viciada
for _ in range(REPETICOES):
    cont += 1    
    pr_honesta = 1 - pr_viciada
    
    resultado = lancar_moeda(moeda)

    if resultado == COROA:
        print "Pr{falsa} = 0" 
        break
    
    # CARA
    
    # n = Pr{C|V}.Pr{V}
    # d = Pr{C|V}.Pr{V} + Pr{C|H}.Pr{H}
    # Pr{V|C} = n/d
 
    n = pr_cara_dado_viciada * pr_viciada
    d = n + pr_cara_dado_honesta * pr_honesta
    pr_viciada = n / d

    print cont, "--- Pr{falsa} =", pr_viciada




   







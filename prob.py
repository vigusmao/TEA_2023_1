from random import random

REPETICOES = 1000000

# legibilidade
HONESTA = 0
FALSA = 1
CARA = 0
COROA = 1

DISTRIB_FALSA = 0.5


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
  

cont_tres_caras, cont_falsas = 0, 0

for _ in range(REPETICOES):
    moeda = sortear_moeda_da_urna()
#print "sorteada foi", "honesta" if moeda==HONESTA\
#                                else "viciada"
    r1,r2,r3 = lancar_moeda(moeda),\
               lancar_moeda(moeda),\
               lancar_moeda(moeda)

    if (r1,r2,r3) == (CARA,CARA,CARA):
        cont_tres_caras += 1
        if moeda == FALSA:
            cont_falsas += 1
    
print 1.0 * cont_falsas/cont_tres_caras









# modelo de crencas
pr_viciada = 0.8

cont = 0
#print cont, "--- Pr{falsa} =", pr_viciada
for _ in range(REPETICOES):
    break  ### 
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




   







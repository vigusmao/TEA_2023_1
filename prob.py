from random import random

REPETICOES = 100

# legibilidade
BOM = 0
MAU = 1
GREEN = 0
RED = 1

DISTRIB_BOM = 0.5


# probs condicionais
pr_G_dado_BOM = 0.8
pr_R_dado_BOM = 1 - pr_G_dado_BOM

pr_G_dado_MAU = 0.3
pr_R_dado_MAU = 1 - pr_G_dado_MAU


def sortear_jogador():
    return BOM if random() < DISTRIB_BOM\
                 else MAU

def acender_luz(jogador):
    r = random()
    if jogador == BOM:
        return GREEN \
            if r < pr_G_dado_BOM \
            else RED   
    # MAU:
    return GREEN \
        if r < pr_G_dado_MAU \
        else RED
  

#cont_tres_caras, cont_falsas = 0, 0

for _ in range(REPETICOES):
    break ###
    moeda = sortear_moeda_da_urna()
    r1,r2,r3 = lancar_moeda(moeda),\
               lancar_moeda(moeda),\
               lancar_moeda(moeda)

    if (r1,r2,r3) == (CARA,CARA,CARA):
        cont_tres_caras += 1
        if moeda == FALSA:
            cont_falsas += 1
    
#print 1.0 * cont_falsas/cont_tres_caras


jogador = sortear_jogador()
print "Jogador sorteado:", "BOM" if jogador==BOM \
                                 else "MAU"

# modelo de crencas
pr_BOM = 0.5

cont = 0
#print cont, "--- Pr{bom} =", pr_bom
for _ in range(REPETICOES):
    cont += 1    
    
    resultado = acender_luz(jogador)

    if resultado == RED:
        
        # n = Pr{R|B}.Pr{B}
        # d = Pr{R|B}.Pr{B} + Pr{R|M}.Pr{M}
        # Pr{B|R} = n/d

        n = pr_R_dado_BOM * pr_BOM
        d = n + pr_R_dado_MAU * (1 - pr_BOM)
        pr_BOM = n / d
    
    if resultado == GREEN:
    
        # n = Pr{G|B}.Pr{B}
        # d = Pr{G|B}.Pr{B} + Pr{G|M}.Pr{M}
        # Pr{B|G} = n/d
 
        n = pr_G_dado_BOM * pr_BOM
        d = n + pr_G_dado_MAU * (1 - pr_BOM)
        pr_BOM = n / d

    print cont, \
          "G" if resultado == GREEN else "R", \
          "--- Pr{bom} =", pr_BOM




   







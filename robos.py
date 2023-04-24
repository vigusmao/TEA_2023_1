##
##  Rendezvous unidimensional com marcadores
##  (Robos de paraquedas)
##
##


from random import choice, randint


DESENHAR = True
ESTRATEGIAS = [0,1,2,3,4]
ESPACAMENTO = 75


# estrategia 0: zigue-zague aritmetico,
#               encontrou paraquedas do amigo fica parado
# estrategia 1: zigue-zague geometrico,
#               encontrou paraquedas do amigo fica parado
# estrategia 2: zigue-zague geometrico,
#               encontrou paraquedas do amigo continua andando 
# estrategia 3: perseguicao
# estrategia 4: igual a estrategia 2 (zigue-zague geometrico otimizado),
#               mas com definicao randomizada da direcao inicial


# const
A = 0
B = 1
DIR = 1
ESQ = -1

MIN_D = 1
MAX_D = 2000

RECOLHER_PARAQUEDAS = False
REPETICOES = 4

# global
tempo = 0
pos_inicial = [None]*2
pos_atual = [None]*2
sentido = [None]*2
tempo_espera = [None]*2
cont_inversoes_sentido = [None]*2
encontrou_paraquedas = [None]*2


def inicializar(robo, dist, estrat, iteracao):
    pos_inicial[robo] = robo * dist
    pos_atual[robo] = pos_inicial[robo]
    cont_inversoes_sentido[robo] = 0
    encontrou_paraquedas[robo] = False

    if estrat in [4,6]:
        sentidos = [(-1,-1),(1,1),(1,-1),(-1,1)]
        sentido[robo] = sentidos[t%4][robo]
    elif estrat == 5:
        sentido[robo] = choice((-1,1))
    else:
        sentido[robo] = DIR

    if estrat == 6:
        tempo_espera[robo] = randint(0,4)
    else:
        tempo_espera[robo] = 0
    
def mover(robo):
    pos_atual[robo] = pos_atual[robo] + sentido[robo]

    if not encontrou_paraquedas[robo]:
        # verifica se encontrou o paraquedas do amigo
        outro_robo = (3-robo)%2
        if pos_atual[robo] == pos_inicial[outro_robo]:
            encontrou_paraquedas[robo] = True

def agir(robo, estrategia):
    globals()["agir" + str(estrategia)](robo)

def agir0(robo):
    if encontrou_paraquedas[robo]:
        return   # robo nao faz nada, apenas aguarda
    
    mover(robo)

    # verifica se precisa inverter o sentido do movimento
    pos_proxima_inversao = pos_inicial[robo] + sentido[robo] * (cont_inversoes_sentido[robo] + 1)
    if pos_atual[robo] == pos_proxima_inversao:
        sentido[robo] *= -1
        cont_inversoes_sentido[robo] += 1
        
def agir1(robo):
    if encontrou_paraquedas[robo]:
        return   # robo nao faz nada, apenas aguarda
    
    mover(robo)

    # verifica se precisa inverter o sentido do movimento
    pos_proxima_inversao = pos_inicial[robo] + sentido[robo] * 2**(cont_inversoes_sentido[robo])
    if pos_atual[robo] == pos_proxima_inversao:
        sentido[robo] *= -1
        cont_inversoes_sentido[robo] += 1

def agir2(robo):
    mover(robo)

    # verifica se precisa inverter o sentido do movimento
    if not encontrou_paraquedas[robo]:
        pos_proxima_inversao = pos_inicial[robo] + sentido[robo] * 2**(cont_inversoes_sentido[robo])
        if pos_atual[robo] == pos_proxima_inversao:
            sentido[robo] *= -1
            cont_inversoes_sentido[robo] += 1

def agir3(robo):
    if encontrou_paraquedas[robo] or (tempo % 2 == 1):
        mover(robo)

def agir4(robo):
    agir2(robo)

def agir5(robo):
    mover(robo)

    # verifica se precisa inverter o sentido do movimento
    if not encontrou_paraquedas[robo]:
        sentido[robo] *= choice((-1,1))

def agir6(robo):
    if tempo <= tempo_espera[robo]:
        return

    agir2(robo)

                        
def mostrar_robos():
    print("\n" + " " * (5-len(str(tempo))) + "(%d)" % tempo, end="")
    linha = []
    
    sobra = (ESPACAMENTO - MAX_D) // 2
    for i in range(-sobra, max(pos_inicial[B], pos_atual[B]) + 1):
        if pos_atual[A] == i:
            if pos_atual[B] == i:
                linha.append("+")
            else:
                linha.append("A")
        elif pos_atual[B] == i:
            linha.append("B")
        else:
            if (pos_inicial[A] == i) or \
               (pos_inicial[B] == i):
                linha.append("|")
            else:
                linha.append(" ")
    print(''.join(linha), end="")
    

# main

while(True):
    d = eval(input("\nDistancia: "))
    if d == 0:
        break
    
    MIN_D = d
    MAX_D = d

    print()

    tempos = {}
    posicoes = {}
    vitorias_4 = 0

    deu_problema = False

    for estrategia in ESTRATEGIAS:
        tempos[estrategia] = 0
        
    for distancia in range(MIN_D, MAX_D+1):
        print("\ndistancia %d" % distancia)

        for estrategia in ESTRATEGIAS:   
            
            tempos[(distancia, estrategia)] = []
            posicoes[(distancia, estrategia)] = []

            if estrategia in [4, 6]:  # randomizada
                rep = REPETICOES
            else:
                rep = 1
            
            for t in range(rep):
                tempo = 0
                inicializar(A, distancia, estrategia, t)
                inicializar(B, distancia, estrategia, t)
                if DESENHAR:
                    mostrar_robos()

                while pos_atual[A] < pos_atual[B]:
                    tempo += 1
                    agir(A, estrategia)
                    agir(B, estrategia)

                    if pos_atual[A] > pos_atual[B]:
                        if encontrou_paraquedas[A]:
                            pos_atual[A] = pos_atual[B]
                        elif encontrou_paraquedas[B]:
                            pos_atual[B] = pos_atual[A]
                        else:
                            if not RECOLHER_PARAQUEDAS:
                                pos_atual[B] = pos_atual[A]
                            
                    if DESENHAR:
                        mostrar_robos()
                        
                if RECOLHER_PARAQUEDAS:
                    destino = [None, None]
                    
                    if encontrou_paraquedas[A]:
                        destino[A] = pos_inicial[A]
                        destino[B] = pos_inicial[A]
                    elif encontrou_paraquedas[B]:
                        destino[A] = pos_inicial[B]
                        destino[B] = pos_inicial[B]
                    else:
                        destino[A] = pos_inicial[B]
                        destino[B] = pos_inicial[A]
                
                    while pos_atual[A] != destino[A]:
                        tempo += 1
                        pos_atual[A] += (destino[A] - pos_atual[A]) / abs(destino[A] - pos_atual[A])
                        pos_atual[B] += (destino[B] - pos_atual[B]) / abs(destino[B] - pos_atual[B])
                        if DESENHAR:
                            mostrar_robos()

                        encontrou_paraquedas[A] = True
                        encontrou_paraquedas[B] = True

                    if pos_atual[A] != pos_atual[B]:
                        destino[A] = pos_inicial[A]
                        destino[B] = pos_inicial[B]
                        while pos_atual[A] > pos_atual[B]:
                            tempo += 1
                            pos_atual[A] += (destino[A] - pos_atual[A]) / abs(destino[A] - pos_atual[A])
                            pos_atual[B] += (destino[B] - pos_atual[B]) / abs(destino[B] - pos_atual[B])

                            if pos_atual[A] < pos_atual[B]:
                                pos_atual[B] = pos_atual[A]  # se encontram, na verdade, no meio do caminho
                            
                            if DESENHAR:
                                mostrar_robos()

                    

                ponto_medio_inicial = (pos_inicial[A] + pos_inicial[B]) / 2
                posicao = abs((pos_atual[A] + pos_atual[B]) / 2 - ponto_medio_inicial)
                posicoes[(distancia, estrategia)] += [posicao]
                tempos[(distancia, estrategia)] += [tempo]
                #if RECOLHER_PARAQUEDAS:
                #    tempos[(distancia, estrategia)][-1] += posicao + ponto_medio_inicial

            print("\nestrategia %d " % estrategia, end="")
            if estrategia != 4:
                print("tempo total = %d" % tempo)
            else:
                print("tempo medio = %.2f" %
                      (sum(tempos[(distancia, estrategia)]) / rep))

            print("tempo acumulado = %.2f" %
                  (sum([sum(tempos[(d, estrategia)]) / len(tempos[(d, estrategia)]) \
                        for d in range(MIN_D, distancia + 1)])))

print("\nTchau!!")

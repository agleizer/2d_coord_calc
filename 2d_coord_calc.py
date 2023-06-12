print("PARTE A")
#definição das variaveis e input da transladada
transladaX = int(input("Forneça a coordenada X da origem transladada: "))
transladaY = int(input("Forneça a coordenada Y da origem transladada: "))

#definição da variavel e input do numero de pontos
n_pontos = int(input("Forneça o número de pontos para leitura: "))

#criação das variaveis para os pontos
pontoX_input = 0 #variável para receber input de X de cada ponto
pontoY_input = 0 #variável para receber input de Y de cada ponto
pontoX_output = 0 #variável para receber o cálculo de X transladado de cada ponto
pontoY_output = 0 #variável para receber o cálculo de Y transladado de cada ponto
armazenador_quadrante_1 = 0 #contador para guardar o número de pontos em determinado quadrante, precisaremos mais para frente
armazenador_quadrante_2 = 0 #idem
armazenador_quadrante_3 = 0 #idem
armazenador_quadrante_4 = 0 #idem
distancia_atual = 0 #variável para armazenar a distância euclidiana do ponto sendo calculado no momento
armazenador_maior_X = 0 #variável para armazenar o valor X do ponto com maior distancia euclidiana
armazenador_maior_Y = 0 #variável para armazenar o valor Y do ponto com maior distancia euclidiana
armazenador_menor_X = 0 #variável para armazenar o valor X do ponto com menor distancia euclidiana
armazenador_menor_Y = 0 #variável para armazenar o valor X do ponto com menor distancia euclidiana
armazenador_maior_distancia = 0 #variável para armazenar o valor da maior distancia euclidiana
armazenador_menor_distancia = 0 #variável para armazenar o valor da menor distancia euclidiana. Não podemos manter 0, pois nada será menor. No loop essa var assume o valor da primeira distancia calculada, e depopis é reavaliada

#definição da variável para loop de input dos pontos
contador_pontos_input = 0

#loop integrado
while (contador_pontos_input < n_pontos):
    print("Forneça o valor X do ponto",contador_pontos_input+1,": ") #comando input precisa conter apenas uma string, então separei um print com o prompt, onde posso usar variaveis para indicar o numero do ponto, e um input vazio abaixo disso.
    pontoX_input = int(input())
    print("Forneça o valor Y do ponto",contador_pontos_input+1,": ") #idem, para a coordenada Y
    pontoY_input = int(input())
    # calculo dos pontos transladados
    pontoX_output = pontoX_input - transladaX #calculo do novo ponto X
    pontoY_output = pontoY_input - transladaY #calculo do novo ponto Y
    #calculo das distancias euclidianas
    distancia_atual = ((pontoX_output-0)**2 + (pontoY_output-0)**2)**0.5 #formula da distancia entre um ponto na list pontos_output (VALOR TRANSLADO) e a nova origem, (0,0)
    if contador_pontos_input == 0: #define o armazenador da maior distancia com o valor da primeira distancia calculada, pois não podiamos manter o valor 0 que usamos para inicializar se não nada seria menor
        armazenador_menor_distancia = distancia_atual
        armazenador_menor_X = pontoX_input
        armazenador_menor_Y = pontoY_input
    if distancia_atual > armazenador_maior_distancia: #armazena as infos do ponto se for o mais distante avaliado até o momento
        armazenador_maior_distancia = distancia_atual
        armazenador_maior_X = pontoX_input
        armazenador_maior_Y = pontoY_input
    if distancia_atual < armazenador_menor_distancia: #armazena as infos do ponto se for o menos distante avaliado até o momento
        armazenador_menor_distancia = distancia_atual
        armazenador_menor_X = pontoX_input
        armazenador_menor_Y = pontoY_input
    # calculo dos novos quadrantes
    if pontoX_output == 0: #se um valor X for = 0, par ordenado está no eixo das ordenadas
        print("O ponto (%d, %d) está sobre o eixo das ordenadas." %(pontoX_input, pontoY_input))
        contador_pontos_input = contador_pontos_input +1
    elif pontoY_output == 0: # se um valor Y for = 0, par ordenado está no eixo das abcissas.
        print("O ponto (%d, %d) está sobre o eixo das abcissas." %(pontoX_input, pontoY_input))
        contador_pontos_input = contador_pontos_input +1
    elif pontoX_output > 0 and pontoY_output > 0: # se ambos X e Y positivos = 1 quadrante
        print("O ponto (%d, %d) está no primeiro quadrante." %(pontoX_input, pontoY_input))
        armazenador_quadrante_1 = armazenador_quadrante_1 +1
        contador_pontos_input = contador_pontos_input +1
    elif pontoX_output < 0 and pontoY_output > 0: # se X < 0 e Y > 0 = 2 quadrante
        print("O ponto (%d, %d) está no segundo quadrante." %(pontoX_input, pontoY_input))
        armazenador_quadrante_2 = armazenador_quadrante_2 +1
        contador_pontos_input = contador_pontos_input +1
    elif pontoX_output < 0 and pontoY_output < 0: # se X < 0 e Y < 0 = 3 quadrante
        print("O ponto (%d, %d) está no terceiro quadrante." %(pontoX_input, pontoY_input))
        armazenador_quadrante_3 = armazenador_quadrante_3 +1
        contador_pontos_input = contador_pontos_input +1
    elif pontoX_output > 0 and pontoY_output < 0: # se X > 0 e Y < 0 = 4 quadrante
        print("O ponto (%d, %d) está no quarto quadrante." %(pontoX_input, pontoY_input))
        armazenador_quadrante_4 = armazenador_quadrante_4 +1
        contador_pontos_input = contador_pontos_input +1

#print de informações sobre total de pontos em quadrantes e maiores e menores distancias
print("Existem %d pontos no primeiro quadrante, %d pontos no segundo quadrante, %d pontos no terceiro quadrante e %d pontos no quarto quadrante." %(armazenador_quadrante_1, armazenador_quadrante_2, armazenador_quadrante_3, armazenador_quadrante_4))
print("O ponto (%d, %d) é o mais próximo, distância: %.2f" %(armazenador_menor_X, armazenador_menor_Y, armazenador_menor_distancia))
print("O ponto (%d, %d) é o mais distante, distância: %.2f" %(armazenador_maior_X, armazenador_maior_Y, armazenador_maior_distancia))

"""
Pontos para input teste
-5
-3
-4
3
-3
1
-2
-1
2
-4
2
3
4
-3
5
4
"""

print("PARTE B")

#definição de variaveis e input
origemX = int(input("Forneça a coordenada X do ponto de origem do robô: "))
origemY = int(input("Forneça a coordenada Y do ponto de origem do robô: "))
tempo = int(input("Forneça o tempo que o robô deve caminhar: "))

#calculo da caminhada e definição de variáveis para o loop
destinoX = origemX #destino = origem para iniciar a variavel e manter as infos separadas
destinoY = origemY #destino = origem para iniciar a variavel e manter as infos separadas
contador_passos = 0 #variavel para o loop

while (contador_passos < tempo): #limitando o loop/passos até o tempo max definido pelo usuario
    if (contador_passos % 3 == 0): #padrão é: só andamos para cima quando o número de passos mod 3 = 0 (no passo 0, no passo 3...)
        destinoY = destinoY + 1 #quando contador mod 3 = 0, andamos 1 para cima
        contador_passos = contador_passos + 1 #+1 no contador para não cair nessa condição na proxima iteração
    else: #sempre que o mod do contador não for 0, andamos para a direita
        destinoX = destinoX + 1 #+1 passo para a direita
        contador_passos = contador_passos + 1 #+1 click no contador

print("Ao final da caminhada, o robô estará no ponto (%d, %d) do plano cartesiano." %(destinoX, destinoY))
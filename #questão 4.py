#questão 4
import numpy as np
import matplotlib.pyplot as plt
# Criando a função para caminhada aleatoria bidimensional
def caminhada_aleatoria_bidimensional(passos):
    posicao_atual = [0, 0]
    posicoes_x = [posicao_atual[0]]
    posicoes_y = [posicao_atual[1]]
    #Criando os valores que ele pode assumir, com probabilidades iguais
    for _ in range(passos):
        direcao_x = 1 if np.random.rand() < 0.5 else -1  # 1 para direita, -1 para esquerda
        direcao_y = 1 if np.random.rand() < 0.5 else -1  # 1 para cima, -1 para baixo
        posicao_atual[0] += direcao_x
        posicao_atual[1] += direcao_y
        posicoes_x.append(posicao_atual[0])
        posicoes_y.append(posicao_atual[1])

    return posicoes_x, posicoes_y

# Número total de passos em cada caminhada aleatória bidimensional
total_passos = 1000

# Número de caminhadas aleatórias
num_caminhadas = 5

# Simulação das caminhadas aleatórias bidimensionais
plt.figure(figsize=(8, 6))
for i in range(num_caminhadas):
    caminhada_x, caminhada_y = caminhada_aleatoria_bidimensional(total_passos)
    plt.plot(caminhada_x, caminhada_y, label=f'Caminhada {i+1}')

# Adicionando ponto inicial
plt.scatter(0, 0, color='brown', label='Ponto Inicial',s=100) #s=tamanho do ponto
# Adicionando linha horizontal no ponto y = 0
plt.axhline(0, color='black', linewidth=1.5)
# Adicionando linha vertical no ponto x = 0
plt.axvline(0, color='black', linewidth=1.5)

plt.title(f'Simulação de {num_caminhadas} Caminhadas Aleatórias Bidimensionais')
plt.xlabel('Posição X')
plt.ylabel('Posição Y')
plt.legend()
plt.grid(True) #Nesse caso uso grid para facilitar a visualização
plt.show()
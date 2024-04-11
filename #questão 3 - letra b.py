#questão 3 - letra b
import numpy as np
import matplotlib.pyplot as plt
# Criando a função para caminhada aleatoria
def caminhada_aleatoria(passos):
    posicao_atual = 0
    posicoes = [posicao_atual]
    #Criando os valores que ele pode assumir, com probabilidades diferentes
    for _ in range(passos):
        direcao = np.random.choice([-1, 1], p=[0.25, 0.75])  # 1 para direita (probabilidade 3/4), -1 para esquerda (probabilidade 1/4)
        posicao_atual += direcao
        posicoes.append(posicao_atual)

    return posicoes

# Determinando o número total de passos em cada caminhada aleatória
total_passos = 500

# Determinando o número de caminhadas aleatórias
num_caminhadas = 10

# Simulação das caminhadas aleatórias
for i in range(num_caminhadas):
    caminhada = caminhada_aleatoria(total_passos)
    plt.plot(caminhada, label=f'Caminhada {i+1}')

# Adicionando linha horizontal no ponto y = 0
plt.axhline(0, color='black', linewidth=1.5)

plt.title(f'Simulação de {num_caminhadas} Caminhadas Aleatórias')
plt.xlabel('Número de Passos')
plt.ylabel('Posição')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.gcf().set_size_inches(10, 6)
plt.show()
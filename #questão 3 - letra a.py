#questão 3 - letra a
import numpy as np
import matplotlib.pyplot as plt
# Criando a função para caminhada aleatoria
def caminhada_aleatoria(passos):
    posicao_atual = 0
    posicoes = [posicao_atual]
    #Criando os valores que ele pode assumir, com a mesma probabilidade
    for _ in range(passos):
        direcao = np.random.choice([-1, 1])  # -1 para esquerda, 1 para direita
        posicao_atual += direcao
        posicoes.append(posicao_atual)

    return posicoes

# Número total de passos em cada caminhada aleatória
total_passos = 500

# Número de caminhadas aleatórias
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
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))  # Alterando a posição da legenda fora do gráfico
plt.gcf().set_size_inches(10, 6)
plt.show()
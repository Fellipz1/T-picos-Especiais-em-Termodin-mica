# questão 2
import numpy as np
import matplotlib.pyplot as plt
#Criando a função para o lançamento de moedas
def simula_lancamentos(N):
    # Simula N lançamentos de moeda sendo 1 para cara e 0 para coroa
    lancamentos = np.random.randint(2, size=N)
    print(lancamentos)
    # Calcula quantas vezes deu cara
    caras_cumulativo = np.cumsum(lancamentos)
    # Calcula a probabilidade de sair caras
    probabilidade_caras = caras_cumulativo / np.arange(1, N+1)
    return probabilidade_caras

# Valores de N para simulação, conforme a questão
Ns = [10, 500, 1000]
# Criação da figura e subplots
fig, axs = plt.subplots(1, 3, figsize=(18, 6))

for i, N in enumerate(Ns):
    probabilidade_caras = simula_lancamentos(N)
    axs[i].plot(range(1, N+1), probabilidade_caras)
    axs[i].axhline(y=0.5, color='r', linestyle='--')
    axs[i].set_title(f'N = {N}')
    axs[i].set_xlabel('Número de Lançamentos')
    axs[i].set_ylabel('Probabilidade de Cara')
    axs[i].grid(True)

plt.tight_layout()
plt.show()

Ns = [10, 500, 1000]
plt.figure(figsize=(14, 8))

for N in Ns:
    probabilidade_caras = simula_lancamentos(N)
    plt.plot(range(1, N+1), probabilidade_caras, label=f'N={N}')

plt.axhline(y=0.5, color='r', linestyle='--', label='Probabilidade Esperada = 0.5')
plt.title('Probabilidade de Cara em Função do Número de Lançamentos')
plt.xlabel('Número de Lançamentos')
plt.ylabel('Probabilidade de Cara')
plt.legend()
plt.show()

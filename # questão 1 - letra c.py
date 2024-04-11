# questão 1 - letra c
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import comb
# Criando a função de n e N
def probabilidade_binomial(N, p, n):
    N1 = (N + n) // 2
    N2 = N - N1
    if N1 < 0 or N2 < 0 or N1 > N or N2 > N:
        return 0
    return comb(N, N1) * (p ** N1) * ((1 - p) ** N2) / (2 ** N)

def plot_distribuicao_binomial(ax, N, p):
    n_values = np.arange(-N, N+1, 2)
    probabilidades = [probabilidade_binomial(N, p, n) for n in n_values]
    # Se for um numero pequeno vai ser gráfico de barra, se for maior que 50, vai ser de linha
    if N <= 50:
        ax.bar(n_values, probabilidades, width=1.0)
    else:
        ax.plot(n_values, probabilidades, 'o-', markersize=4, linewidth=1)

    ax.set_title('Distribuição Binomial para Caminhada Aleatória com {} Passos'.format(N), fontsize = 10)
    ax.set_xlabel('Deslocamento (n)')
    ax.set_ylabel('Probabilidade')
    if N <= 100:
        ax.set_xticks(n_values[::max(1,N//20)])
        ax.tick_params(axis='x', labelsize=6)
    else:
        ax.set_xticks(np.linspace(n_values.min(), n_values.max(), num=20))
        ax.grid(True, which='both', axis='x', linestyle='--', linewidth=0.5)
        ax.tick_params(axis='x', labelsize=6)


# Criação da figura e subplots
fig, axs = plt.subplots(1, 3, figsize=(18, 6))

# Fazendo com os números de passos da questão
for i, N_total_passos in enumerate([50, 100, 500]):
    prob_passo_direita = 0.75
    plot_distribuicao_binomial(axs[i], N_total_passos, prob_passo_direita)

plt.tight_layout()
plt.show()

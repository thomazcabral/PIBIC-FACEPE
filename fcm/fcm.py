import numpy as np
from itertools import combinations
from sklearn.metrics import adjusted_rand_score

def inicializao_matriz_pertinencia(num_amostras, num_clusters):
    matriz_pertinencia = np.random.rand(num_amostras, num_clusters) # gera uma matriz inicial aleatória com valores entre 0 e 1
    matriz_pertinencia = matriz_pertinencia / matriz_pertinencia.sum(axis=1, keepdims=True) # normalização da matriz pra garantir que a soma dos graus dê um
    return matriz_pertinencia


def atualizacao_centroides(dados, matriz_pertinencia, m):
    matriz_pertinencia_m = matriz_pertinencia ** m # preparação dos graus de pertinência
    centroides = np.dot(matriz_pertinencia_m.T, dados) / np.sum(matriz_pertinencia_m.T, axis=1, keepdims=True) # fórmula para o cálculo dos centroides
    return centroides


def atualizacao_matriz_pertinencia(dados, centroides, m): # talvez a fórmula para calcular a matriz de pertinência esteja errada
    # dados[:, np.newaxis] - centroides cria uma matriz de diferenças entre os pontos de dados e os centroides
    # np.linalg.norm(..., axis=2) calcula a norma (distância euclidiana) das diferenças
    # ** 2 para a distância ser a quadrada
    matriz_distancias = np.linalg.norm(dados[:, np.newaxis] - centroides, axis=2) ** 2
    matriz_distancias = np.fmax(matriz_distancias, np.finfo(np.float64).eps) # evita que matriz_distancias seja 0, np.finfo... é o menor número maior que zero aaqui
    matriz_distancias_inversa = 1 / matriz_distancias
    potencia = 1 / (m-1)
    matriz_pertinencia_atualizada = matriz_distancias_inversa ** potencia/ np.sum(matriz_distancias_inversa ** potencia, axis=1, keepdims=True) # fórmula para atualizar os graus de pertinência
    return matriz_pertinencia_atualizada


def fcm(dados, num_clusters, m=2, max_iter=1000, erro=1e-5):
    num_amostras = dados.shape[0]
    matriz_pertinencia = inicializao_matriz_pertinencia(num_amostras, num_clusters)
    for _ in range(max_iter): # primeiro critério de parada
        centroides = atualizacao_centroides(dados, matriz_pertinencia, m)
        nova_matriz_pertinencia = atualizacao_matriz_pertinencia(dados, centroides, m)
        if np.linalg.norm(nova_matriz_pertinencia - matriz_pertinencia) < erro: # segundo critério de parada
            break
        matriz_pertinencia = nova_matriz_pertinencia
    return centroides, matriz_pertinencia


def indice_rand(labels, predicted_labels):
    return adjusted_rand_score(labels, predicted_labels)


def experimento_monte_carlo(dados, labels, num_clusters, num_trials):
    indices_rand = []
    for _ in range(num_trials):
        centroides, matriz_pertinencia = fcm(dados, num_clusters)
        predicted_labels = np.argmax(matriz_pertinencia, axis=1)
        idx_rand = indice_rand(labels, predicted_labels)
        indices_rand.append(idx_rand)
    mean_rand_index = np.mean(indices_rand)
    std_rand_index = np.std(indices_rand)
    return mean_rand_index, std_rand_index


dados = np.array([[2, 1], [1.5, 1], [1.5, 0.5], [2, 2.5], [3, 3], [2, 4], [2, 3], [2, 2]])
labels = np.array([2, 2, 2, 0, 0, 1, 2, 0])

num_clusters = 3
num_trials = 100
media_indice_rand, dp_indice_rand = experimento_monte_carlo(dados, labels, num_clusters, num_trials)

print(f"Monte Carlo FCM Clustering Results ({num_trials} trials)")
print(f"Mean Rand Index: {media_indice_rand:.4f}")
print(f"Standard Deviation of Rand Index: {dp_indice_rand:.4f}")

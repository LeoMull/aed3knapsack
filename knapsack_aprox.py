def ordena_por_razão(valor, peso):
    # Criar um dicionário com índices como chaves e (valor, peso) como valores
    itens = {i: (valor[i], peso[i]) for i in range(1, len(valor))}

    # Calcular a razão valor/peso e armazenar em uma lista de tuplas
    razões = [(i, itens[i][0] / itens[i][1]) for i in itens]

    # Ordenar os itens pela razão valor/peso em ordem decrescente
    razões_ordenadas = sorted(razões, key=lambda x: x[1], reverse=True)

    # Retornar a lista de índices dos itens ordenados
    return [i[0] for i in razões_ordenadas]

def knapsack(m, vi, wi):
    solucao = []
    s = 0
    for k in range(len(vi)):
        if s + wi[k] <= m:
            solucao.append(k)
            s += wi[k]
        else:
            break
    return solucao

def main():
    m = 7
    vi = [0, 3, 4, 2, 1, 1]  # Incluindo um 0 no início para indexar de 1 a n
    wi = [0, 1, 2, 4, 2, 2]  # Incluindo um 0 no início para indexar de 1 a n
    
    # Ordenar os itens por razão valor/peso
    indices_ordenados = ordena_por_razão(vi, wi)
    
    # Criar as listas de valor e peso na ordem dos índices ordenados
    vi_ordenado = [vi[i] for i in indices_ordenados]
    wi_ordenado = [wi[i] for i in indices_ordenados]
    
    # Executar o algoritmo da mochila
    resultado = knapsack(m, vi_ordenado, wi_ordenado)
    
    # Ajustar índices de volta para o formato original
    resultado_original = [indices_ordenados[i] for i in resultado]
    
    print("Itens selecionados:", resultado_original)

if __name__ == '__main__':
    main()

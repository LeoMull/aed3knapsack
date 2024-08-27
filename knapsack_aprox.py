import time

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
    m = 40

    start_time = time.time()
    vi = [0, 23, 85, 76, 45, 32, 90, 12, 56, 78, 34, 91, 67, 5, 49, 18, 50, 72, 84, 22, 11, 29, 47, 94, 99, 61, 7, 19, 55, 2, 30, 66, 44, 25, 64, 70, 81, 38, 3, 60, 14, 87, 98, 42, 27, 8, 35, 93, 40, 53, 68]
    wi = [0, 4, 7, 9, 2, 3, 8, 5, 6, 10, 1, 2, 4, 7, 5, 8, 3, 6, 9, 7, 2, 1, 4, 3, 8, 10, 5, 6, 7, 1, 4, 9, 2, 3, 5, 7, 10, 8, 1, 6, 3, 2, 4, 7, 9, 10, 5, 6, 8, 7, 4]

    # Ordenar os itens por razão valor/peso
    indices_ordenados = ordena_por_razão(vi, wi)
    
    # Criar as listas de valor e peso na ordem dos índices ordenados
    vi_ordenado = [vi[i] for i in indices_ordenados]
    wi_ordenado = [wi[i] for i in indices_ordenados]
    
    # Executar o algoritmo da mochila

    resultado = knapsack(m, vi_ordenado, wi_ordenado)
    
    # Ajustar índices de volta para o formato original
    resultado_original = [indices_ordenados[i] for i in resultado]
    
    end_time = time.time()

    # Calcular o peso total e o volume total dos itens selecionados
    peso_total = sum(wi_ordenado[i] for i in resultado)
    volume_total = sum(vi_ordenado[i] for i in resultado)

    print(f'Time = {end_time - start_time}')
    print("Itens selecionados:", resultado_original)
    print("Peso total dos itens na mochila:", peso_total)
    print("Volume total dos itens na mochila:", volume_total)

if __name__ == '__main__':
    main()

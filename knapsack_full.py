from itertools import combinations

def knapsack(items, max_volume, max_weight):
    items_len = len(items)
    best_comb = []
    best_vol = 0
    best_weight = 0

    for size in range(1, items_len ): 
        iter_comb = combinations(items, size)
        #passa por todas as combinações possíveis
        for i in iter_comb:
            sum_vol = 0
            sum_weight = 0
            #soma volume e peso de cada combinação
            for volume in i:
                sum_vol += volume[0]
                sum_weight += volume[1]
            #verifica se a combinação é válida
            if sum_vol <= max_volume and sum_weight <= max_weight:
                print(i)
                print(len(i))
                print(f"volume {sum_vol}")
                print(f"peso {sum_weight}")

                #verifica se a combinação é melhor que a anterior 
                if (len(i) > len(best_comb)) or ((len(i) == len(best_comb) and sum_weight > best_weight)) or ((len(i) == len(best_comb) and sum_vol > best_vol)):
                    best_comb = i
                    best_weight = sum_weight
                    best_vol = sum_vol
    return best_comb, best_vol, best_weight
             
def main():
    #item (volume, peso)
    items = [
        (20, 1),
        (5, 2),
        (10, 3),
        (40, 8),
        (15, 7),
        (22, 1),
        (12, 1),
        (16, 8),
        (6, 3),
        (9, 3),
        (16, 8),
        (6, 2),
        (9, 13),
        (16, 8),
        (6, 2),
        (9, 13),
        (6, 2),
        (9, 13),
        (16, 8),
        (6, 2),
        (9, 13)
    ]

    for i in items:
        print(f'Item {i} - Peso: {i[1]} - Volume: {i[0]}')

    print('Mochila: volume máximo 70')

    max_volume = 70
    max_weight = 20
    best_comb, best_vol, best_weight = knapsack(items, max_volume, max_weight)
    print(f" Best Combination = {best_comb}\n Volume = {best_vol}\n Weight = {best_weight}")

main()


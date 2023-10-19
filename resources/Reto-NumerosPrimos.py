def num_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

primos = [num for num in range(1, 251) if num_primo(num)]

with open('results.txt', 'w') as file:
    for primo in primos:
        file.write(str(primo) + '\n')

print("Los Números primos encontrados entre 1 y 251 se guardaron en 'results.txt'")

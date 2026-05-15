def leia_lista_numeros():
    lista = []
    for _ in range(10):
        numero = int(input('Digite um número:'))
        lista.append(numero)
    return lista

def busca_o_maior_elemento(lista):
    maior = lista[0]
    for numero in lista:
        if numero > maior:
            maior = numero
    return maior

def main():
    lista = leia_lista_numeros()
    maior = busca_o_maior_elemento(lista)

    print('Lista: ', lista)
    print('O maior número da lista: ', maior)


main()
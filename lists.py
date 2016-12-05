# coding=UTF-8


def add_numbers(x, y, z):
    a = []
    inicial_num = x
    size = y
    qtd_lists = z

    while (qtd_lists > 0):
        final_num = inicial_num + size
        a.append(range(inicial_num, final_num))
        qtd_lists = qtd_lists - 1
        inicial_num = final_num
    print(a)


if __name__ == "__main__":
    x = input("Qual o número inicial: ")
    y = input("Qual o tamanho das listas: ")
    z = input("Qual a quantidade de listas: ")

    add_numbers(x, y, z)

'''
x - numero inicial (1 = [1,2,3])
y - tamanho das listas (2 = [1,2])
z - quantidade de listas (3 = [1,2],[3,4],[5,6])
'''

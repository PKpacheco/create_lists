

# coding=UTF-8

def add_numbers(x, y, z, s):
    normal_list = []
    square_list = []
    inicial_num = x
    size = y
    qtd_lists = z
    square = s

    while (qtd_lists > 0):
        final_num = inicial_num + size
        if square.lower() in 'y':
            square_list.append([x * x for x in range(inicial_num, final_num)])
        elif square.lower() in 'n':
            normal_list.append(range(inicial_num, final_num))
        qtd_lists = qtd_lists - 1
        inicial_num = final_num
    print(normal_list)
    print(square_list)

if __name__ == "__main__":
    x = input("Inicial number: ")
    y = input("Size of lists: ")
    z = input("Amount of lists: ")
    s = str(raw_input("Square? y (yes) or n (no) "))

    add_numbers(x, y, z, s)


'''
x - numero inicial (1 = [1,2,3])
y - tamanho das listas (2 = [1,2])
z - quantidade de listas (3 = [1,2],[3,4],[5,6])
'''

# a = []
# for x in a range(1,4):
#     a[i] = a[i] * a[i]
#     i=+1
#
# words = ['cat', 'window', 'defenestrate']
# for value  in words:
#     print w

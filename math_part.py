import sfml as sf
import math as ma

def conv_hex(nbr):
    base = list()
    base = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    l = 0
    dec = 0
    for h in nbr:
        k = 0
        while (h != base[k]):
            k = k + 1
            if (k is 16):
                del (base)
                base = list()
                base = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
                k = 0
                while (h != base[k]):
                    k = k + 1

        if (l is 0):
            dec = dec + int(k) * 16
        else:
            dec = dec + int(k)
        l = 1
    return (dec)

def conv_dec(nbr):
    base = list()
    base = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    conv_nbr = list()
    f_b = nbr / 16
    conv_nbr.append(base[int(f_b % 16)])
    conv_nbr.append(base[int(nbr % 16)])
    return (conv_nbr)

def de_rotate_mat(points, height, width):
    c = 0
    fin_mat = list()
    while (c < height - 1):
        l = width - 1
        line = list()
        while (l >= 0):
            line.append(points[l][c])
            l = l - 1
        fin_mat.append(line)
        del (line)
        c = c + 1
    return (fin_mat)

def rotate_mat(points, height, width):
    c = width - 1
    fin_mat = list()
    while (c >= 0):
        l = 0
        line = list()
        while (l < height - 1):
            line.append(points[l][c])
            l = l + 1
        fin_mat.append(line)
        del (line)
        c = c - 1
    return (fin_mat)

def get_width(points):
    w = 0
    for i in points[0]:
        w = w + 1
    return (w)

def get_height(points):
    h = 0
    for i in points:
        h = h + 1
    return (h)

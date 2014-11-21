import sfml as sf
import draw_line as drw
import math_part as mp

def draw_field(fdf):
    f_point = sf.Vector2()
    r_point = sf.Vector2()
    b_point = sf.Vector2()
    frc_point = sf.Vector2()
    color = list()
    l = 0
    while (l < fdf[2].x):
        c = 0
        while (c < fdf[2].y):
            f_point.x = 0.5 * c * fdf[5] - 0.5 * l * fdf[5] + fdf[4].x
            f_point.y = 0.25 * c * fdf[5] + 0.25 * l * fdf[5] + fdf[4].y - fdf[1][l][c][0] * fdf[5] / 50
            if (l + 1 < fdf[2].x):
                b_point.x = 0.5 * c * fdf[5] - 0.5 * (l + 1) * fdf[5] + fdf[4].x
                b_point.y = 0.25 * c * fdf[5] + 0.25 * (l + 1) * fdf[5] + fdf[4].y - fdf[1][l + 1][c][0] * fdf[5] / 50
                del (color)
                color = list()
                color.append(sf.Color(fdf[1][l][c][1], fdf[1][l][c][2], fdf[1][l][c][3]))
                color.append(sf.Color(fdf[1][l + 1][c][1], fdf[1][l + 1][c][2], fdf[1][l + 1][c][3]))
                drw.draw_line(fdf[6], f_point, b_point, color)
            if (c + 1 < fdf[2].y):
                r_point.x = 0.5 * (c + 1) * fdf[5] - 0.5 * l * fdf[5] + fdf[4].x
                r_point.y = 0.25 * (c + 1) * fdf[5] + 0.25 * l * fdf[5] + fdf[4].y - fdf[1][l][c + 1][0] * fdf[5] / 50
                del (color)
                color = list()
                color.append(sf.Color(fdf[1][l][c][1], fdf[1][l][c][2], fdf[1][l][c][3]))
                color.append(sf.Color(fdf[1][l][c + 1][1], fdf[1][l][c + 1][2], fdf[1][l][c + 1][3]))
                drw.draw_line(fdf[6], f_point, r_point, color)
            if (c + 1 < fdf[2].y and l + 1 < fdf[2].x):
                frc_point.x = 0.5 * (c + 1) * fdf[5] - 0.5 * (l + 1) * fdf[5] + fdf[4].x
                frc_point.y = 0.25 * (c + 1) * fdf[5] + 0.25 * (l + 1) * fdf[5] + fdf[4].y - fdf[1][l + 1][c + 1][0] * fdf[5] / 50
                del (color)
                color = list()
                color.append(sf.Color(fdf[1][l][c][1], fdf[1][l][c][2], fdf[1][l][c][3]))
                color.append(sf.Color(fdf[1][l + 1][c + 1][1], fdf[1][l + 1][c + 1][2], fdf[1][l + 1][c + 1][3]))
                drw.draw_line(fdf[6], f_point, frc_point, color)
            c = c + 1
        l = l + 1

def my_get_nbr(nbr):
    size = 0
    coeff = 1
    final_nbr = 0
    g = 0
    sign = 1
    for i in nbr:
        if i is '-':
            sign = sign * (-1)
        else:
            size = size + 1
    size = size - 1
    while (size >= 0):
        if (nbr[size] != '-'):
            final_nbr = final_nbr + coeff * int(nbr[size])
            coeff = coeff * 10
        size = size - 1
    return (final_nbr * sign)

def my_get_points(file):
    content = file.read(1)
    points = list()
    line = list()
    nbr = list()
    ok = 0
    blu = 0
    while (content != ""):
        if (content != ' ' and content != '\n'):
            if (content is ','):
                i = my_get_nbr(nbr)
                del (nbr)
                nbr = list()
                nbr.append(i)
                content = file.read(2)
                for u in range(0, 3):
                    content = file.read(2)
                    nbr.append(mp.conv_hex(content))
                col = sf.Color(nbr[1], nbr[2], nbr[3])
                blu = 1
            else:
                nbr.append(content)
            ok = 1
        elif (ok is 1):
            if (content is " "):
                if (blu is 0):
                    i = my_get_nbr(nbr)
                    del (nbr)
                    nbr = list()
                    nbr.append(i)
                    nbr.append(255)
                    nbr.append(255)
                    nbr.append(255)
                    line.append(nbr)
                else:
                    line.append(nbr)
                    blu = 0
                del (nbr)
                nbr = list()
            elif (content is "\n"):
                if (blu is 0):
                    i = my_get_nbr(nbr)
                    del (nbr)
                    nbr = list()
                    nbr.append(i)
                    nbr.append(255)
                    nbr.append(255)
                    nbr.append(255)
                    line.append(nbr)
                else:
                    line.append(nbr)
                    blu = 0
                del (nbr)
                nbr = list()
                points.append(line)
                del (line)
                line = list()
            ok = 0
        content = file.read(1)
    points.append(line)
    return (points)

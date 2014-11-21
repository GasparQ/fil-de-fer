import sfml as sf
import math_part as ma
import math as mth

def disp_selec(img, pos, color, fdf):
    center = sf.Vector2()
    center.x = 0.5 * pos.x * fdf[5] - 0.5 * pos.y * fdf[5] + fdf[4].x
    center.y = 0.25 * pos.x * fdf[5] + 0.25 * pos.y * fdf[5] + fdf[4].y - fdf[1][pos.y][pos.x][0] * fdf[5] / 50
    for alpha in range(0, 360):
        img[center.x + 10 * mth.cos(alpha), center.y + 10 * mth.sin(alpha)] = color
    return (img)

def choose_point(fdf, mouse_pos):
    line = 0
    point = sf.Vector2()
    mat_id = 0
    for l in fdf[1]:
        col = 0
        for c in l:
            point.x = 0.5 * col * fdf[5] - 0.5 * line * fdf[5] + fdf[4].x
            point.y = 0.25 * col * fdf[5] + 0.25 * line * fdf[5] + fdf[4].y - c[0] * fdf[5] / 50
            if (mouse_pos.x <= point.x + 10 and mouse_pos.x >= point.x - 10):
                if (mouse_pos.y <= point.y + 10 and mouse_pos.y >= point.y - 10):
                    mat_id = sf.Vector2(col, line)
            col = col + 1
        line = line + 1
    return (mat_id)

def init_mat(size):
    mat = list()
    for l in range(1, size.y):
        line = list()
        for c in range(1, size.x):
            point = list()
            point.append(0)
            point.append(255)
            point.append(255)
            point.append(255)
            line.append(point)
            del (point)
        mat.append(line)
        del (line)
    return (mat)

def save_field(mat):
    with open("fields/created/fld01.txt", "w") as file:
        for l in mat:
            tem = 0
            for c in l:
                file.write(str(c[0]))
                file.write(",0x")
                col = ma.conv_dec(c[1])
                file.write(str(col[0]))
                file.write(str(col[1]))
                col = ma.conv_dec(c[2])
                file.write(str(col[0]))
                file.write(str(col[1]))
                col = ma.conv_dec(c[3])
                file.write(str(col[0]))
                file.write(str(col[1]))
                tem = tem + 1
                if (tem < 19):
                    file.write(" ")
            file.write("\n")

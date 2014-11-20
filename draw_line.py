import sfml as sf

def search_color(tab_color, act_color, pixel_nbr):
    if tab_color[0].r < tab_color[1].r:
        if act_color.r + (tab_color[1].r - tab_color[0].r) / pixel_nbr <= tab_color[1].r:
            act_color.r = act_color.r + (tab_color[1].r - tab_color[0].r) / pixel_nbr
    else:
        if act_color.r - (tab_color[0].r - tab_color[1].r) / pixel_nbr >= tab_color[1].r:
            act_color.r = act_color.r - (tab_color[0].r - tab_color[1].r) / pixel_nbr
    if tab_color[0].g < tab_color[1].g:
        if act_color.g + (tab_color[1].g - tab_color[0].g) / pixel_nbr <= tab_color[1].g:
            act_color.g = act_color.g + (tab_color[1].g - tab_color[0].g) / pixel_nbr
    else:
        if act_color.g - (tab_color[0].g - tab_color[1].g) / pixel_nbr >= tab_color[1].g:
            act_color.g = act_color.g - (tab_color[0].g - tab_color[1].g) / pixel_nbr
    if tab_color[0].b < tab_color[1].b:
        if act_color.b + (tab_color[1].b - tab_color[0].b) / pixel_nbr <= tab_color[1].b:
            act_color.b = act_color.b + (tab_color[1].b - tab_color[0].b) / pixel_nbr
    else:
        if act_color.b - (tab_color[0].b - tab_color[1].b) / pixel_nbr >= tab_color[1].b:
            act_color.b = act_color.b - (tab_color[0].b - tab_color[1].b) / pixel_nbr
    return act_color

def draw_decreased(img, f_point, s_point, color):
    mine_color = color[0]
    if s_point.x - f_point.x >= f_point.y - s_point.y: #tracer une ligne plus horizontale que verticale
        g = f_point.x
        pixel_nbr = s_point.x - f_point.x
        if f_point.x != s_point.x:
            while g <= s_point.x:
                ordon = f_point.y - ((f_point.y - s_point.y) * (g - f_point.x)) / (s_point.x - f_point.x)
                if g >= 0 and ordon >= 0 and g < img.width and g < img.height:
                    img[g, ordon] = mine_color
                mine_color = search_color(color, mine_color, pixel_nbr)
                g = g + 1
    elif s_point.x - f_point.x <= f_point.y - s_point.y: #tracer une ligne plus verticale qu'horizontale
        g = s_point.y
        pixel_nbr = f_point.y - s_point.y
        if f_point.y != s_point.y:
            while g <= f_point.y:
                abcs = f_point.x - ((f_point.x - s_point.x) * (g - f_point.y)) / (s_point.y - f_point.y)
                if g >= 0 and abcs >= 0 and g < img.height and abcs < img.width:
                    img[abcs, g] = mine_color
                mine_color = search_color(color, mine_color, pixel_nbr)
                g = g + 1

def draw_increased(img, f_point, s_point, color):
    mine_color = color[0]
    if s_point.x - f_point.x >= s_point.y - f_point.y: #tracer une ligne plus horizontale que verticale
        g = f_point.x
        pixel_nbr = s_point.x - f_point.x
        if f_point.x != s_point.x:
            while g <= s_point.x:
                ordon = f_point.y + ((s_point.y - f_point.y) * (g - f_point.x)) / (s_point.x - f_point.x)
                if g >= 0 and ordon >= 0 and g < img.width and ordon < img.height:
                    img[g, ordon] = mine_color
                mine_color = search_color(color, mine_color, pixel_nbr)
                g = g + 1
    elif s_point.x - f_point.x <= s_point.y - f_point.y: #tracer une ligne plus vertical qu'horizontale
        g = f_point.y
        pixel_nbr = s_point.y - f_point.y
        if f_point.y != s_point.y:
            while g <= s_point.y:
                abcs = f_point.x + ((s_point.x - f_point.x) * (g - f_point.y)) / (s_point.y - f_point.y)
                if g >= 0 and abcs >= 0 and g < img.height and abcs < img.width:
                    img[abcs, g] = mine_color
                mine_color = search_color(color, mine_color, pixel_nbr)
                g = g + 1

def draw_line(img, f_point, s_point, color):
    if f_point.x <= s_point.x and f_point.y <= s_point.y:
        draw_increased(img, f_point, s_point, color)
    elif f_point.x <= s_point.x and f_point.y >= s_point.y:
        draw_decreased(img, f_point, s_point, color)
    elif f_point.x >= s_point.x and f_point.y <= s_point.y:
        k = color[0]
        l = color[1]
        del color
        color = list()
        color.append(l)
        color.append(k)
        draw_decreased(img, s_point, f_point, color)
    elif f_point.x >= s_point.x and f_point.y >= s_point.y:
        k = color[0]
        l = color[1]
        del color
        color = list()
        color.append(l)
        color.append(k)
        draw_increased(img, s_point, f_point, color)

#!
import sfml as sf
import draw_line as drw
import draw_field as fld
import math_part as mp
import create_field as crt_fld
import home

def disp_color_map(img, width, height):
    x = 0
    y = 0
    r = 255
    b = 0
    g = 0
    while (y < height):
        img[x, y] = sf.Color(r, g, b)
        if (x > (width / 2) - y/2 and r > 2):
            r = r - 2
        if (x > y/2 and b < 254):
            b = b + 2
        x = x + 1
        if (x > width):
            y = y + 1
            g = g + 1
            x = 0
            r = 255
            b = 0

def disp_my_field(all_params, selec):
    graph = sf.Image.create(all_params[3].y, all_params[3].x, sf.Color.TRANSPARENT)
    all_params.append(graph)
    fld.draw_field(all_params)
    if (type(selec) == sf.system.Vector2):
        all_params[6] = crt_fld.disp_selec(all_params[6], selec, sf.Color.RED, all_params)
    text = sf.Texture.from_image(all_params[6])
    sprite = sf.Sprite(text)
    all_params[0].draw(sprite)
    return (all_params)

def main():
    l = 0
    a = 0
    all_params = 0
    all_params = home.home_choice(all_params)
    disab = all_params[6]
    del all_params[6]
    selec = 0
    while (all_params[0].is_open):
        for event in all_params[0].events:
            if (type(event) is sf.CloseEvent or disab is 5):
                all_params[0].close()
            if (type(event) is sf.MouseMoveEvent and disab is 0):
                selec = crt_fld.choose_point(all_params, event.position)
                l = 0
            if (type(event) is sf.MouseButtonEvent and disab is 0):
                if (event.pressed):
                    if (type(selec) is sf.system.Vector2):
                        disab = 1
            if (type(event) is sf.MouseButtonEvent and disab is 4):
                if (event.position.x > 0 and event.position.x < 256):
                    if (event.position.y > 0 and event.position.y < 256):
                        all_params[1][selec.y][selec.x][1] = colormap[event.position.x, event.position.y].r
                        all_params[1][selec.y][selec.x][2] = colormap[event.position.x, event.position.y].g
                        all_params[1][selec.y][selec.x][3] = colormap[event.position.x, event.position.y].b
                        disab = 0
                        l = 0
            if (type(event) is sf.KeyEvent):
                if (event.pressed):
                    if (event.alt):
                        if (event.code is sf.Keyboard.UP and all_params[2].x < 50 and all_params[2].x < 50):
                            if (all_params[5] + 1 < 51):
                                all_params[5] = all_params[5] + 1
                                l = 0
                        if (event.code is sf.Keyboard.DOWN and all_params[2].x < 50 and all_params[2].x < 50):
                            if (all_params[5] - 1 > 6):
                                all_params[5] = all_params[5] - 1
                                l = 0
                    else:
                        if (event.code is sf.Keyboard.UP and disab != 1  and all_params[2].x < 50 and all_params[2].x < 50):
                            if (all_params[4].y - 10 > 0):
                                all_params[4].y = all_params[4].y - 10
                                l = 0
                        if (event.code is sf.Keyboard.DOWN and disab != 1  and all_params[2].x < 50 and all_params[2].x < 50):
                            if (all_params[4].y + 10 < all_params[3].x - 250):
                                all_params[4].y = all_params[4].y + 10
                                l = 0
                        if (event.code is sf.Keyboard.LEFT and all_params[2].x < 50 and all_params[2].x < 50):
                            if (all_params[4].x - 10 > 0):
                                all_params[4].x = all_params[4].x - 10
                                l = 0
                        if (event.code is sf.Keyboard.RIGHT and all_params[2].x < 50 and all_params[2].x < 50):
                            if (all_params[4].x + 10 < all_params[3].y):
                                all_params[4].x = all_params[4].x + 10
                                l = 0
                        if (event.code is sf.Keyboard.ESCAPE and disab != 1):
                            all_params[0].close()
                        if (event.code is sf.Keyboard.RETURN and disab != 1):
                            crt_fld.save_field(all_params[1])
                        if (event.code is sf.Keyboard.UP and disab is 1):
                            if (all_params[1][selec.y][selec.x][0] + 1 < 100):
                                all_params[1][selec.y][selec.x][0] = all_params[1][selec.y][selec.x][0] + 1
                                l = 0
                        if (event.code is sf.Keyboard.DOWN and disab is 1):
                            if (all_params[1][selec.y][selec.x][0] - 1 > -100):
                                all_params[1][selec.y][selec.x][0] = all_params[1][selec.y][selec.x][0] - 1
                                l = 0
                        if (event.code is sf.Keyboard.RETURN and disab is 1):
                            disab = 4
                            colormap = sf.Image.create(256, 256, sf.Color.TRANSPARENT)
                            disp_color_map(colormap, 256, 256)
                            color_tex = sf.Texture.from_image(colormap)
                            color_sprite = sf.Sprite(color_tex)
                            all_params[0].draw(color_sprite)
                            all_params[0].display()
        if (l is 0):
            all_params[0].clear()
            all_params = disp_my_field(all_params, selec)
            del all_params[6]
            l = 1
            a = 0
            all_params[0].display()
    main()

main()

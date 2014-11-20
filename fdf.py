#!
import sfml as sf
import draw_line as drw
import draw_field as fld
import math_part as mp

def main():
    l = 0
    with open("fields/elem-fract.txt", "r") as file:
        points = list()
        points = fld.my_get_points(file)
    dim = sf.Vector2(mp.get_height(points), mp.get_width(points))
    w_dim = sf.Vector2(dim.x * 50, dim.y * 50 / 2)
    img_dim = sf.Vector2(dim.x * 50, dim.y * 55)
    zoom = 50
    img_width = dim.y * 55
    img_height = dim.x * 100
    if w_dim.x > 1700:
        w_dim.x = 1700
        img_dim.x = 1700
        dim.x = 500
        zoom = 5
    if w_dim.y > 1200:
        w_dim.y = 1000
        img_dim.y = 1700
        dim.y = 500
        zoom = 5
    points = mp.rotate_mat(points, dim.x, dim.y)
    dim.x = mp.get_height(points)
    dim.y = mp.get_width(points)
    window = sf.RenderWindow(sf.VideoMode(w_dim.x, w_dim.y), "field")
    origin = sf.Vector2(w_dim.y, 20)
    while (window.is_open):
        for event in window.events:
            if type(event) is sf.CloseEvent:
                window.close()
            if type(event) is sf.MouseButtonEvent:
                if event.pressed:
                    print(graph[event.position.x, event.position.y])
            if type(event) is sf.KeyEvent:
                if event.pressed:
                    if event.alt:
                        if event.code is sf.Keyboard.UP:
                            if zoom + 1 < 51:
                                zoom = zoom + 1
                                l = 0
                        if event.code is sf.Keyboard.DOWN:
                            if zoom - 1 > 6:
                                zoom = zoom - 1
                                l = 0
                    else:
                        if event.code is sf.Keyboard.UP:
                            if origin.y - 10 > 0:
                                origin.y = origin.y - 10
                                l = 0
                        if event.code is sf.Keyboard.DOWN:
                            if origin.y + 10 < img_dim.x - 250:
                                origin.y = origin.y + 10
                                l = 0
                        if event.code is sf.Keyboard.LEFT:
                            if origin.x - 10 > 0:
                                origin.x = origin.x - 10
                                l = 0
                        if event.code is sf.Keyboard.RIGHT:
                            if origin.x + 10 < img_dim.y:
                                origin.x = origin.x + 10
                                l = 0
                        if event.code is sf.Keyboard.ESCAPE:
                            window.close()
        if l is 0:
            graph = sf.Image.create(img_dim.y, img_dim.x, sf.Color.TRANSPARENT)
            window.clear()
            fld.draw_field(graph, points, origin, dim, zoom)
            text = sf.Texture.from_image(graph)
            sprite = sf.Sprite(text)
            window.draw(sprite)
            l = 1
            window.display()

main()

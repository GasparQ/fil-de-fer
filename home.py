import sfml as sf
import draw_field as fld
import math_part as mp
import create_field as crt_fld

def field_choice():
    print("Choose the field you want to load :")
    print(" [1] or [&]: elem.txt -> classical field")
    print(" [2] or [é]: elem2.txt -> display a 42 extruded")
    print(" [3] or [\"]: elem-col.txt -> classical field with colors")
    print(" [4]  or [\']: elem-fract.txt -> display the Mandelbrot set (it take 10s to load)")
    print(" [5] or [(]: a created field")
    while (1):
        if (sf.Keyboard.is_key_pressed(sf.Keyboard.NUM1)):
            return ("fields/basic/elem.txt")
        if (sf.Keyboard.is_key_pressed(sf.Keyboard.NUM2)):
            return ("fields/basic/elem2.txt")
        if (sf.Keyboard.is_key_pressed(sf.Keyboard.NUM3)):
            return ("fields/basic/elem-col.txt")
        if (sf.Keyboard.is_key_pressed(sf.Keyboard.NUM4)):
            return ("fields/basic/elem-fract.txt")
        if (sf.Keyboard.is_key_pressed(sf.Keyboard.NUM5)):
            return ("fields/created/fld01.txt")

def load_field(all_params):
    with open(field_choice(), "r") as file:
        points = list()
        points = fld.my_get_points(file)
    dim = sf.Vector2(mp.get_height(points), mp.get_width(points))
    w_dim = sf.Vector2(dim.x * 50, dim.y * 50 / 2)
    img_dim = sf.Vector2(dim.x * 50, dim.y * 55)
    zoom = 50
    img_width = dim.y * 55
    img_height = dim.x * 100
    if (w_dim.x > 1700):
        w_dim.x = 1700
        img_dim.x = 1700
        dim.x = 500
        zoom = 5
    if (w_dim.y > 1200):
        w_dim.y = 1000
        img_dim.y = 1700
        dim.y = 500
        zoom = 5
    points = mp.rotate_mat(points, dim.x, dim.y)
    dim.x = mp.get_height(points)
    dim.y = mp.get_width(points)
    window = sf.RenderWindow(sf.VideoMode(w_dim.x, w_dim.y), "field")
    origin = sf.Vector2(w_dim.y, 20)
    del (all_params)
    all_params = list()
    all_params.append(window)
    all_params.append(points)
    all_params.append(dim)
    all_params.append(img_dim)
    all_params.append(origin)
    all_params.append(zoom)
    return (all_params)

def edit_field(all_params):
    size = sf.Vector2(20, 20)
    points = crt_fld.init_mat(size)
    crt_fld.save_field(points)
    dim = sf.Vector2(mp.get_height(points), mp.get_width(points))
    w_dim = sf.Vector2(dim.x * 50, dim.y * 50 / 2)
    img_dim = sf.Vector2(dim.x * 50, dim.y * 55)
    zoom = 50
    img_width = dim.y * 55
    img_height = dim.x * 100
    if (w_dim.x > 1700):
        w_dim.x = 1700
        img_dim.x = 1700
        dim.x = 500
        zoom = 5
    if (w_dim.y > 1200):
        w_dim.y = 1000
        img_dim.y = 1700
        dim.y = 500
        zoom = 5
    points = mp.rotate_mat(points, dim.x, dim.y)
    dim.x = mp.get_height(points)
    dim.y = mp.get_width(points)
    window = sf.RenderWindow(sf.VideoMode(w_dim.x, w_dim.y), "field")
    origin = sf.Vector2(w_dim.y, 20)
    del (all_params)
    all_params = list()
    all_params.append(window)
    all_params.append(points)
    all_params.append(dim)
    all_params.append(img_dim)
    all_params.append(origin)
    all_params.append(zoom)
    return (all_params)

def home_choice(all_params):
    choice = 1
    print("Charger un terrain : C\nEditer un terrain : E\nQuitter : Q")
    while (choice is 1):
        if (sf.Keyboard.is_key_pressed(sf.Keyboard.C)):
            all_params = load_field(all_params)
            choice = 2
        if (sf.Keyboard.is_key_pressed(sf.Keyboard.E)):
            all_params = edit_field(all_params)
            choice = 0
        if (sf.Keyboard.is_key_pressed(sf.Keyboard.Q)):
            exit(1)
    all_params.append(choice)
    return (all_params)

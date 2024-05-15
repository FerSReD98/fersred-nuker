# This library was made by https://github.com/561fffDemon
from pystyle import Colorate
import shutil

def rgbGrad(colors, steps=10):
    gradient = []
    num_colors = len(colors)  # Number of colors in the list

    # Calculate the number of steps between each color
    steps_per_color = steps // (num_colors - 1)

    for i in range(num_colors - 1):
        rgb1 = colors[i]
        rgb2 = colors[i + 1]

        # Calculate the difference between each RGB component
        r_diff = (rgb2[0] - rgb1[0]) / steps_per_color
        g_diff = (rgb2[1] - rgb1[1]) / steps_per_color
        b_diff = (rgb2[2] - rgb1[2]) / steps_per_color

        # Generate the gradient between the current and next color
        for j in range(steps_per_color):
            r = int(rgb1[0] + (r_diff * j))
            g = int(rgb1[1] + (g_diff * j))
            b = int(rgb1[2] + (b_diff * j))
            gradient.append(f"{r};{g};{b}")
            # print(r,g,b)
            
    gradient.append(f"{colors[-1][0]};{colors[-1][1]};{colors[-1][2]}")
    # print(colors[-1][0],colors[-1][1],colors[-1][2])

    return gradient

def CenterColor(s,colors,steps,type):
    centered = ""
    for i in s.split("\n"):
        centered += i.center(shutil.get_terminal_size().columns) + "\n"
    gradientText(colors,steps,centered,type)

def Center(s):
    centered = ""
    for i in s.split("\n"):
        centered += i.center(shutil.get_terminal_size().columns) + "\n"
    print(centered,end="")

def gradientText(colors,steps,text,type):
    gradient = rgbGrad(colors,steps)
    if type == "V":
        print(Colorate.Vertical(gradient, text, 1))
    elif type == "H":
        print(Colorate.Horizontal(gradient, text, 1))
    else:
        print(Colorate.Vertical(gradient, "Yanlış tip, Tip V - Dikey ve H - Yatay olabilir", 1))

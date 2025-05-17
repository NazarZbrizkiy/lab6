import math
import glob
import os

# --- Класи фігур ---
class Figure:
    def area(self):
        raise NotImplementedError

    def perimeter(self):
        raise NotImplementedError

class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c

class Rectangle(Figure):
    def __init__(self, a, b):
        self.a, self.b = a, b

    def area(self):
        return self.a * self.b

    def perimeter(self):
        return 2 * (self.a + self.b)

class Trapeze(Figure):
    def __init__(self, a, b, c, d):
        self.a, self.b, self.c, self.d = a, b, c, d

    def area(self):
        # Формула площі через сторони (Брама-Грама)
        s = (self.a + self.b + self.c + self.d) / 2
        if self.a == self.b:
            return 0  # уникнення ділення на 0
        h = (2 / abs(self.a - self.b)) * math.sqrt(
            (s - self.a) * (s - self.b) * (s - self.a - self.c) * (s - self.a - self.d)
        )
        return ((self.a + self.b) / 2) * h

    def perimeter(self):
        return self.a + self.b + self.c + self.d

class Parallelogram(Figure):
    def __init__(self, a, b, h):
        self.a, self.b, self.h = a, b, h

    def area(self):
        return self.a * self.h

    def perimeter(self):
        return 2 * (self.a + self.b)

class Circle(Figure):
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r ** 2

    def perimeter(self):
        return 2 * math.pi * self.r

# --- Парсер рядка ---
def parse_figure(line):
    parts = line.strip().split()
    if not parts:
        return None
    name = parts[0]
    params = list(map(int, parts[1:]))
    if name == "Triangle" and len(params) == 3:
        return Triangle(*params)
    elif name == "Rectangle" and len(params) == 2:
        return Rectangle(*params)
    elif name == "Trapeze" and len(params) == 4:
        return Trapeze(*params)
    elif name == "Parallelogram" and len(params) == 3:
        return Parallelogram(*params)
    elif name == "Circle" and len(params) == 1:
        return Circle(*params)
    else:
        return None

def figure_info(fig):
    if isinstance(fig, Triangle):
        return f"Triangle sides: {fig.a}, {fig.b}, {fig.c}"
    elif isinstance(fig, Rectangle):
        return f"Rectangle sides: {fig.a}, {fig.b}"
    elif isinstance(fig, Trapeze):
        return f"Trapeze sides: {fig.a}, {fig.b}, {fig.c}, {fig.d}"
    elif isinstance(fig, Parallelogram):
        return f"Parallelogram sides: {fig.a}, {fig.b}, height: {fig.h}"
    elif isinstance(fig, Circle):
        return f"Circle radius: {fig.r}"
    else:
        return "Unknown figure"

# --- Основна частина ---
folder = r'c:\Users\Nosok\Downloads'
patterns = ["input*.txt", "input* (1).txt"]
files = []
for pattern in patterns:
    files.extend(glob.glob(os.path.join(folder, pattern)))

for filename in files:
    print(f"\nОбробка файлу: {os.path.basename(filename)}")
    figures = []
    with open(filename, encoding='utf-8') as f:
        for line in f:
            fig = parse_figure(line)
            if fig:
                figures.append(fig)

    max_area = -1
    max_perimeter = -1
    max_area_figure = None
    max_perimeter_figure = None

    for fig in figures:
        try:
            area = fig.area()
            perimeter = fig.perimeter()
        except Exception:
            continue
        if area > max_area:
            max_area = area
            max_area_figure = fig
        if perimeter > max_perimeter:
            max_perimeter = perimeter
            max_perimeter_figure = fig

    print("Фігура з максимальною площею:", figure_info(max_area_figure), "Площа:", max_area)
    print("Фігура з максимальним периметром:", figure_info(max_perimeter_figure), "Периметр:", max_perimeter)
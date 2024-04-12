x1, y1, x2, y2 = map(int, input('Координаты прямоугольника (через пробел)').split())
point_x, point_y = map(int, input('Координаты точки (через пробел)').split())
rect = ((x1,y1),(x2,y2))
bool = False

if point_x <= x2 and point_x >= x1 and point_y <= y1 and point_y >= y2:
    bool = True
    print('Point is inside: ', bool)
else:
    print('Not inside')
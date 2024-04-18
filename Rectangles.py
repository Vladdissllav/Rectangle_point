# def length(x1, y1, x2, y2):
#     len = ( (x2-x1)**2 + (y2-y1)**2 ) ** 0.5
#     return len

def rect_area(xa1, ya1, xc1, yc1):
    width = abs(xc1 - xa1)
    height = abs(yc1 - ya1)
    area = width * height
    return area

# def rect_inters_coord(xa1, ya1, xc1, yc1, xa2, ya2, xc2, yc2):
#     zx1 = min(xc1, xc2)
#     zy1 = min(ya1, ya2)
#     zx2 = max(xa1, xa2)
#     zy2 = max(yc1, yc2)
#     yield zx1, zy1, zx2, zy2

xa1, ya1, xc1, yc1 = map(int, input('Координаты точек А(верхний левый угол) и С(правый нижний угол) первого прямоугольника (через пробел)').split())
xa2, ya2, xc2, yc2 = map(int, input('Координаты точек А(верхний левый угол) и С(правый нижний угол) второго прямоугольника (через пробел)').split())

if xa2 > xc1 or xc2 < xa1 or ya2 < yc1 or yc2 > ya1:
    print('Rectangles do not intersect')
    print('Overall area equals to : ', rect_area(xa1, ya1, xc1, yc1) + rect_area(xa2, ya2, xc2, yc2))
else:
    print('Rectangles have an intersection')
    print('Overall area equals to : ', rect_area(xa1, ya1, xc1, yc1) + rect_area(xa2, ya2, xc2, yc2) - rect_area(min(xc1, xc2), min(ya1, ya2), max(xa1, xa2), max(yc1, yc2)))


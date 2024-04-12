xA = int(input('Enter X of A '))
yA = int(input('Enter Y of A '))
xB = int(input('Enter X of B '))
yB = int(input('Enter Y of B '))
xC = int(input('Enter X of C '))
yC = int(input('Enter Y of C '))
xD = int(input('Enter X of D '))
yD = int(input('Enter Y of D '))
xE = int(input('Enter X of E '))
yE = int(input('Enter Y of E '))
bool = False

if yA != yB or xA != xD or xC != xB or yC != yD:
    print('Not a rectangle')

else:
    if xE < xB and xE > xA and yE < yA and yE > yD:
        bool = True
        print('Point is inside: ', bool)
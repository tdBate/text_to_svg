#a kapott színt jelelő karaktert visszaadja színként ami megfelelő az svg-be
def szinAtalakit(szin):
    szin = szin.upper()
    if szin == 'F':
        return 'white'
    elif szin == 'P':
        return 'red'
    elif szin == 'K':
        return 'blue'
    elif szin == 'Z':
        return 'green'
    elif szin == 'S':
        return 'yellow'
    elif szin == 'N':
        return 'orange'
    elif szin == 'L':
        return 'purple'
    elif szin == 'B':
        return 'black'


def main():
    file = open("zaszlo.txt", "r")

    kockameret = 100 #az svg kockáinak a méretének a beállítása

    #svg fájl kezdeti adatainak megadása
    svg = '<?xml version="1.0" encoding="UTF-8" standalone="no"?>'
    svg += f'\n<svg width="{kockameret*(len(file.readline())-1)}" height="{kockameret*(len(file.readlines())+1)}" xmlns="http://www.w3.org/2000/svg">'

    file.seek(0) #a stream alaphelyzetbe való állítása

    y_count = 0
    for line in file: #sor
        x_count = 0
        line = line.strip()
        for i in range(len(line)): #oszlop
            svg += f'\n<rect x="{x_count*kockameret}" y="{y_count*kockameret}" width="{kockameret}" height="{kockameret}" fill="{szinAtalakit(line[i])}"/>' #alakzat létrehozása
            x_count+=1
        y_count += 1

    file.close() 
    svg += '\n</svg>'

    #svg file létrehozáse
    file = open("zaszlo.svg","w",encoding="UTF-8")
    file.write(svg)
    file.close()
    print("Az svg fájl létrehozva!")
    

main()
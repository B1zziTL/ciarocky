#vlozenie modulov
import random
import tkinter

#nastavenie platna
canvas = tkinter.Canvas(width="250",height="270",background="white")
canvas.pack()

#vytvorenie prazdneho zoznamu
kod = []

def generuj_kod(): #funkcia na generovanie kodu
    for i in range(8): #cyklus s 8 opakovaniami
        cislica = random.randint(1,9)

        #vlozenie cislice do zoznamu
        kod.append(cislica)

def kresli_kod(): #funkcia na vykreslenie kodu
    #nastavenie zakladnych suradnic
    x = 10
    y = 10
    x1 = 26
    y1 = 100

    #nastavenie pomocnej premennej
    daco = 0
    
    for i in kod: #cyklus na prechadzanie cisel v kode
        #zmena pomocnej premennej
        daco += 1
        
        #podmienka na vykreslenie obdlznika
        if daco == 1 or daco == 8:
            canvas.create_rectangle(x,y,x+i,y+100,fill="black")
        else:
            canvas.create_rectangle(x,y,x+i,y+80,fill="black")

        #vykreslenie cisla
        canvas.create_text(x1,y1,text=i,font="Arial 10")

        #zmena suradnic
        x += 11
        x1 += 7

def citaj_a_kresli_kod(): #funkcia na precitanie kodu zo suboru a jeho vykreslenie
    #otvorenie kodu v mode na citanie
    subor = open("ciarovy_kod_1.txt","r")

    #nastavenie pomocnych premennych
    nieco = 0
    daco1 = 0

    for riadok in subor: #cyklus na prechadzanie riadkov v subore
        #zmena pomocnej premennej
        nieco += 1

        #podmienky na nastavenie pociatocnych suradnic
        if nieco == 1:
            x = 150
            y = 10

            x1 = 166
            y1 = 100
        elif nieco == 2:
            x = 10
            y = 150

            x1 = 26
            y1 = 240
        elif nieco == 3:
            x = 150
            y = 150

            x1 = 166
            y1 = 240
        elif nieco > 3:
            return

        #odstranenie zbytocnych znakov z riadku
        riadocek = riadok.strip()
        kodik = riadocek

        for pismeno in riadocek: #cyklus na prechadzanie pismen v riadku
            #zmena pomocnej premennej
            daco1 += 1

            #podmienka na vykreslenie obdlznika
            if daco1 == 1 or daco1 == 8:
                canvas.create_rectangle(x,y,x+int(pismeno),y+100,fill="black")
            else:
                canvas.create_rectangle(x,y,x+int(pismeno),y+80,fill="black")

            #vykreslenie cisla
            canvas.create_text(x1,y1,text=pismeno,font="Arial 10")

            #zmena suradnic
            x += 11
            x1 += 7

        #zmena pomocnej premennej
        daco1 = 0

#privolanie funkcii        
generuj_kod()
kresli_kod()
citaj_a_kresli_kod()

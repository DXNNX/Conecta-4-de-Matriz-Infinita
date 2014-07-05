####################################
##	Instituto Tecnologico de  ##
##	Costa Rica (TEC)	  ##
##				  ##
##	Estudiante: Danny Chaves  ##
##				  ##
##	Profesor: Diego Mora	  ##
##				  ##
##	Conecta 4 de Matriz	  ##
##	Infinita con UI		  ##
##	Personalizable		  ##
##	e inteligencia Artificial ##
##				  ##
##	Tiempo invertido: 45h	  ##
####################################
##	Autor: Danny Chaves	  ##
##				  ##
##	Facebook: fb.com/DXNNXCH  ##
##				  ##
##	Twitter: @d4nnyc87	  ##
##				  ##
##	GitHub: DXNNX		  ##
##				  ##
##	Correo: dxnnx@me.com	  ##
##				  ##
####################################

#Librerias necesarias para que funcione el algoritmo
from tkinter.filedialog import *
from tkinter import *
import random,time
import os

#Variables globales necesarias para el algorimo
turno = True
jugador1=""
jugador2=""
ficha1 = ""
ficha2=""
coin1=""
coin2=""
ordenarfichas=0
PC = False
indiceH = [0,1,2,3,4,5,6]
indiceV = [0,1,2,3,4,5]
MatrizH = 0
MatrizV = 0
posV = 0
posH = 0
Inicio = True
Chrom = False
Chromturno = False
detener = False
detenerturno=False
detenerturnototal = False
#Matriz a asignar las fichas
matriz = [
    
            [0,0,0,0,0,0,0],
            
            [0,0,0,0,0,0,0],
            
            [0,0,0,0,0,0,0],
            
            [0,0,0,0,0,0,0],
            
            [0,0,0,0,0,0,0],
            
            [0,0,0,0,0,0,0],
            
            ]

#Matriz a asignar las listas de indices y los botones de fichas
boton = [
            [0,0,0,0,0,0,0,0],
            
            [0,0,0,0,0,0,0,0],
            
            [0,0,0,0,0,0,0,0],
            
            [0,0,0,0,0,0,0,0],
            
            [0,0,0,0,0,0,0,0],
            
            [0,0,0,0,0,0,0,0],
            
            [0,0,0,0,0,0,0,0],
            
            [0,0,0]
            
            ]
##Crea los botones y les asigna las imagenes correctamente y comandos
##entradas: NULL/ Todo lo necesario lo obtiene de las globales o de variables predefinidas
##salidas: Null
##restricciones: No poner entradas al llamarse
def crearbotones(cols=1,k=6,rows=1,command =0):
    global matriz,posV,posH,boton,MatrizH,MatrizV,ficha1,ficha2
    null=PhotoImage(file="./extra/fichas/null.gif")
    va1=PhotoImage(file="./extra/fichas/"+ficha1+".gif")
    va2=PhotoImage(file="./extra/fichas/"+ficha2+".gif")
    for i in range(MatrizV,MatrizV+6):
        for j in range(MatrizH, MatrizH+7):
            texto = str(matriz[i][j])
            if command == 0:
                btn = Button(mainFrame,image=null,command=lambda:[c(0)])
                btn.image = null
                pass
            elif command == 1:
                btn = Button(mainFrame,image=null,command=lambda:[c(1)])
                btn.image = null
                pass
            elif command == 2:
                btn = Button(mainFrame,image=null,command=lambda:[c(2)])
                btn.image = null
                pass
            elif command == 3:
                btn = Button(mainFrame,image=null, command=lambda:[c(3)])
                btn.image = null
                pass
            elif command == 4:
                btn = Button(mainFrame,image=null, command=lambda:[c(4)])
                btn.image = null
                pass
            elif command == 5:
                btn = Button(mainFrame,image=null,command=lambda:[c(5)])
                btn.image = null
                pass
            elif command == 6:
                btn = Button(mainFrame,image=null,command=lambda:[c(6)])
                btn.image = null
                pass
            if texto == "1":
                btn.config(image=va1,bd=0)
                btn.image = va1
                pass
            elif texto == "2":
                btn.config(image=va2,bd=0)
                btn.image = va2
                pass
            btn.grid(row=k,column=cols)
            boton[rows][cols] = btn
            cols+=1
            command +=1
        k-=1
        rows+=1
        cols = 1
        command=0
    return

##Crea los indeces y los acomoda, de las lisata InidceV e IndiceH
##entradas: Null
##salidas: Null
##restricciones: no poner entradas
def crearindices(cols=1,rows=6,H=0,V=0):
    global boton,indiceH,indiceV,posV,posH,MatrizV,matriz,MatrizH
    if posV==0:
        bajar.config(state="disabled")
    else:
        bajar.config(state="active")
    for i in indiceH:
        if i == posH:
                for j in range(indiceH[H],indiceH[H]+7):
                    texto = str(indiceH[H])
                    btn = Canvas(mainFrame,width=30,height=30)
                    btn.grid(row=0,column=cols)
                    btn = btn.create_text(2,20,ancho=W,text=texto ,fill="#00cc00",font=("Time 13 bold italic"))
                    boton[0][cols] = btn
                    H+=1
                    cols+=1
        else:
            H+=1        

    for i in indiceV:
        if i == posV:
            for j in range(indiceV[V],indiceV[V]+6):
                    texto = str(indiceV[V])
                    V+=1
                    btn = Canvas(mainFrame,width=30,height=30)
                    btn.grid(row=rows,column=0)
                    btn = btn.create_text(2,20,ancho=W,text=texto ,fill="#00cc00",font=("Time 15 bold italic"))
                    boton[rows][0] = btn
                    rows-=1
        else:
            V+=1

## Asigna la ficha, valida movimiento, inicia el cronometro
##entradas: Entero [0-7[
##salidas: Null
##restricciones: numeros enteros de el [0,7[
def c(mov):
    global matriz,turno,MatrizH,Chrom,largopartida,Chromturno,detenerturno,largoturno
    pos = len(matriz)
    mov+=MatrizH
    if not Chrom:
        Chrom=True
        cronometro(largopartida[0],largopartida[1])
        pass
    if not Chromturno:
        Chromturno=True
        cronoturn(largoturno[0],largoturno[1])
        pass
    if valmove(mov):
        detenerturno=True
        for i in range(pos):
            if matriz[i][mov]==0:
                if turno:
                    matriz[i][mov]=1
                    crearbotones()
                    nextmov()
                    return
                else:
                    matriz[i][mov]=2
                    crearbotones()
                    nextmov()
                    return

    else:
        messagebox.showinfo(title="Error",message="NO puede colocar una ficha a mas de 4 espacios de distancia")
        return
##revisa la matriz en busca de ganador, asigna el siguiente movimiento y activa el movimiento de la computadora
##entradas:Null
##salidas:Null
##restricciones:Null
def nextmov():
    global turno, quienjuega,jugador1,jugador2,mainFrame,quien,redc,bluec,PC,largoturno,coin2,coin1,jugar1c,jugar2c
    winner = vernumero()
    if checkmat():
        winner=jugador2
        if turno:
            winner = jugador1
            pass
        mainFrame.withdraw()
        messagebox.showinfo(title="Felicidades "+winner,message="Felicidades "+winner+" has ganado")
        top()
        blank()
        return
    if turno:
        quien.config(image=jugar2c)
        quienjuega.config(text=jugador2)
        pass
    else:
        quien.config(image=jugar1c)
        quienjuega.config(text=jugador1)
        pass
    turno = not turno
    if PC and not turno:
        return CPU()
##Busca el ultimo numero que se mostrara en la lista de indices, si no esta agrega una fila mas a Matriz
##y un numero mas al IndiceV, hace llamada recursiva pero con el indice y matriz mas amplios
##entradas:entero
##salidas:Null
##restricciones:solo enteros
def aumentarV(aum):
    global indiceH,indiceV,matriz,posV,posH,MatrizH,MatrizV
    if buscarindice(aum+6,1):
        posV = aum
        if aum>MatrizV:
            MatrizV+=1
            crearbotones()
            crearindices()
            return
        elif aum<MatrizV:
            MatrizV-=1
            crearbotones()
            crearindices()
            return
        else:
            return
    else:
        num = indiceV[-1]
        indiceV+=[num+1]
        return aummatriz(2),aumentarV(aum)
##Aumenta la matriz, busca el indice maximo o minimo dependiendo si es negativo o positivo, si no esta amplia la matriz y el IndiceH
##hace llamada recursiva pero con el indiceH y matriz mas amplios
##entradas:2 enteros, un booleano
##salidas:Null
##restricciones:solo enteros/bool
def aumentarH(aum,lado,fix=True):
    global indiceV,indiceH,posV,posH,matriz,MatrizV,MatrizH
    if aum>=0:
        if buscarindice(aum+6,0):
            MatrizH+=lado
            posH=aum
            crearbotones()
            crearindices()

        else:
            indiceH+=[indiceH[-1]+1]
            aummatriz(0)
            return aumentarH(aum,lado)

    else:
        if buscarindice(aum,0):
            if fix:
                MatrizH+=lado
                pass
            posH=aum
            crearbotones()
            crearindices()
        else:
            indiceH=[indiceH[0]-1]+indiceH
            aummatriz(1)
            MatrizH=0
            return aumentarH(aum,lado,False)
##Busca un numero en el indiceH o indice V
##entradas:2 int
##salidas:Booleano
##restricciones:2 enteros
def buscarindice(num,ind):
    global indiceV,indiceH
    if ind == 1:
        for i in indiceV:
            if num == i:
                return True
        return False
    elif ind == 0:
        for i in indiceH:
            if num == i:
                return True
        return False
##Aumenta la matriz tanto filas como columnas, dependiendo del entero
##Entradas:entero
##Salidas:Null
##Restricciones:entero
def aummatriz(mov):
    global matriz
    rows = len(matriz)
    cols = len(matriz[0])
    if mov == 0:
        for i in range(rows):
            matriz[i]=matriz[i]+[0]
        return
    elif mov == 1:
        for i in range(rows):
            matriz[i] = [0] + matriz[i]
        return
    else:
        mas = [0,0,0,0,0,0,0]
        while (len(mas)!=cols):
            mas+=[0]
        matriz= matriz+[mas]
        return
##Valida el movimiento para que no se pase de 4 espacios
##Entradas:int
##Salidas:Bool
##Restricciones:int
def valmove(move):
    global matriz,Inicio
    total = len(matriz[0])
    for i in range(move,move+5):
        if i<total:
            if matriz[0][i]!=0:
                return True 
        else:
            break

    for i in range(move-4,move):
        if 0>i:
            continue
        elif total>i:
            if matriz[0][i]!=0:
                return True          
    if Inicio:
        Inicio = False
        return True
    return False

##Dice el numero del jugador que esta en ese momento        
##Entradas:null
##Salidas:1/2
##Restricciones:null
def vernumero():
    global turno
    if turno:
        return 1
    else:
        return 2
##Revisa la matriz y busca un ganador
##Entradas: null
##Salidas:bool
##Restricciones:null
def checkmat():
    global matriz,turno
    jugador = vernumero()
    H=len(matriz[0])
    V=len(matriz)
    #Horizonatal
    for x in range(V):
        for y in range(H-3):
            if matriz[x][y]==jugador and matriz[x][y+1]==jugador and matriz[x][y+2]==jugador and matriz[x][y+3]==jugador:
                return True
    #Vertical
    for x in range(V-3):
        for y in range(H):
            if matriz[x][y]==jugador and matriz[x+1][y]==jugador and matriz[x+2][y]==jugador and matriz[x+3][y]==jugador:
                return True
    #Diagonal /
    for x in range(V-3):
        for y in range(3,H):
            if matriz[x][y]==jugador and matriz[x+1][y-1]==jugador and matriz[x+2][y-2]==jugador and matriz[x+3][y-3]==jugador:
                return True
    #Diagonal \
    for x in range(V-3):
        for y in range(H-3):
            if matriz[x][y]==jugador and matriz[x+1][y+1]==jugador and matriz[x+2][y+2]==jugador and matriz[x+3][y+3]==jugador:
                return True
    return False
#Jugador de la computadora
##Entradas:null
##Salidas:Funcion c(int)
##Restricciones:null
def CPU():
    jugador = 1
    global matriz,MatrizH,MatrizV
    for x in range(MatrizV,MatrizV+6-3-1):
        for y in range(abs(MatrizH)+3, abs(MatrizH)+7):
            if matriz[x][y]==0 and matriz[x-1][y]==0 and matriz[x+1][y-1]==jugador and matriz[x+2][y-2]==jugador and matriz[x+3][y-3]==jugador:
                return c((y)%7)
    for x in range(MatrizV,MatrizV+6-3):
        for y in range(abs(MatrizH)+3, abs(MatrizH)+7):
            if x==0:
                if matriz[x][y]==0 and matriz[x+1][y-1]==0 and matriz[x][y-1]!=0 and matriz[x+2][y-2]==jugador and matriz[x+3][y-3]==jugador:
                    return c((y-1)%7)
            if matriz[x][y]==0 and matriz[x+1][y-1]==jugador and matriz[x-1][y-1]!=0 and matriz[x+2][y-2]==jugador and matriz[x+3][y-3]==jugador:
                    return c((y-1)%7)
            if matriz[x][y]==jugador and matriz[x+1][y-1]==0 and matriz[x][y-1]!=0 and matriz[x+2][y-2]==jugador and matriz[x+3][y-3]==jugador:
                    return c((y-1)%7)
            if matriz[x][y]==jugador and matriz[x+1][y-1]==jugador and matriz[x+2][y-2]==0 and matriz[x+1][y-2]!=0  and matriz[x+3][y-3]==jugador:
                return c((y-2)%7)
            if matriz[x][y]==jugador and matriz[x+1][y-1]==jugador and matriz[x+2][y-2]==jugador and matriz[x+3][y-3]==0 and matriz[x+2][y-3]!=0 :
                return c((y-3)%7)
    for x in range(MatrizV,MatrizV+6-3):
        for y in range(abs(MatrizH),abs(MatrizH)+7-3):
            if matriz[x][y]==0 and matriz[x+1][y+1]==jugador and matriz[x+2][y+2]==jugador and matriz[x+3][y+3]==jugador:
                return c((y)%7)
            if matriz[x][y]==jugador and matriz[x][y+1]!=0 and matriz[x+1][y+1]==0 and matriz[x+2][y+2]==jugador and matriz[x+3][y+3]==jugador:
                return c((y+1)%7)
            if matriz[x][y]==jugador and matriz[x][y+2]!=0 and matriz[x+1][y+1]==jugador and matriz[x+2][y+2]==0 and matriz[x+3][y+3]==jugador:
                return c((y+2)%7)
            if matriz[x][y]==jugador and matriz[x+1][y+1]==jugador and matriz[x+2][y+2]==jugador and matriz[x+3][y+3]==0 and matriz[x][y+3]!=0:
                return c((y+3)%7)
    for x in range(MatrizV,MatrizV+6-1):
        for y in range(abs(MatrizH), abs(MatrizH)+7-3):
            if matriz[x][y]==jugador and matriz[x][y+1]==jugador and matriz[x][y+2]==jugador and matriz[x][y+3]==0 and matriz[x-1][y+3]!=0:
                return c((y+3)%7)
            if matriz[x][y]==0 and matriz[x-1][y]!=0 and matriz[x][y+1]==jugador and matriz[x][y+2]==jugador and matriz[x][y+3]==jugador:
                return c((y)%7)
            if matriz[x][y]==jugador and matriz[x][y+1]==0 and matriz[x-1][y+1]!=0 and matriz[x][y+2]==jugador and matriz[x][y+3]==jugador:
                return c((y+1)%7)
            if matriz[x][y]==jugador and matriz[x][y+1]==jugador and matriz[x][y+2]==0 and matriz[x-1][y+2]!=0  and matriz[x][y+3]==jugador:
                return c((y+2)%7)
    for x in range(MatrizV,MatrizV+6-3):
        for y in range(abs(MatrizH), abs(MatrizH)+7):
            if matriz[x][y]==jugador and matriz[x+1][y]==jugador and matriz[x+2][y]==jugador and matriz[x+3][y]==0:
                return c((y)%7)
    for x in range(MatrizV,MatrizV+6-2):
        for y in range(abs(MatrizH)+2, abs(MatrizH)+7):
            if matriz[x][y]==0 and matriz[x+1][y-1]==jugador and matriz[x+2][y-2]==jugador:
                return c(y)
            if matriz[x][y]==jugador and matriz[x+1][y-1]==0 and matriz[x+2][y-2]==jugador :
                return c((y-1)%7)
            if matriz[x][y]==jugador and matriz[x+1][y-1]==jugador and matriz[x+2][y-2]==0 :
                return c((y-2)%7)
    for x in range(MatrizV,MatrizV+6-2):
        for y in range(abs(MatrizH),abs(MatrizH)+7-2):
            if matriz[x][y]==0 and matriz[x+1][y+1]==jugador and matriz[x+2][y+2]==jugador:
                return c((y)%7)
            if matriz[x][y]==jugador and matriz[x+1][y+1]==0 and matriz[x+2][y+2]==jugador:
                return c((y+1)%7)
            if matriz[x][y]==jugador and matriz[x+1][y+1]==jugador and matriz[x+2][y+2]==0:
                return c((y+2)%7) 
    for x in range(MatrizV,MatrizV+6-2):
        for y in range(abs(MatrizH), abs(MatrizH)+7):
            if matriz[x][y]==jugador and matriz[x+1][y]==jugador and matriz[x+2][y]==0:
                return c(y%7)
    for x in range(MatrizV,MatrizV+6):
        for y in range(abs(MatrizH), abs(MatrizH)+7-2):
            if matriz[x][y]==jugador and matriz[x][y+1]==jugador and matriz[x][y+2]==0:
                return c(y+2)
            if matriz[x][y]==0 and matriz[x][y+1]==jugador and matriz[x][y+2]==jugador:
                return c((y)%7)
            if matriz[x][y]==jugador and matriz[x][y+1]==0 and matriz[x][y+2]==jugador:
                return c((y+1)%7)
    for x in range(MatrizV,MatrizV+6):
        for y in range(abs(MatrizH), abs(MatrizH)+7):
            if matriz[x][y]==jugador:
                return c(y%7)
#Cierra mainFrame y lo resetea y muestra mensaje que se acabo el tiempo
##Entradas:Null
##Salidas:Null
##Restricciones:Null
def timesup():
    blank()
    messagebox.showinfo("TIempo Fuera",message="Se a acabado el tiempo!")
    return
#Agrega el ganador de la partida al documento, si no esta lo crea el documento y lo agrega
##Entradas:Null
##Salidas:Null
##Restricciones:Null
def top():
    global jugador1,jugador2
    if turno:
        ganador = jugador1
        pass
    else:
        ganador = jugador2
        pass
    try:
        win = open("./extra/datos.txt","r")
        total = eval(win.readline())
        win.close()
        new=True
        for i in total:
            if i[0] == ganador:
                i[1]+=1
                new= False
        if new:
            total+=[[ganador,1]]
            pass
        win = open("./extra/datos.txt","w")
        win.write(str(total))
        win.close()
    except:
        win = open("./extra/datos.txt","a+")
        total = [[ganador,1]]
        win.write(str(total))
        win.close()
##Pone la Variable detener en False
##Entradas:Null
##Salidas:Null
##Restricciones:Null
def normaldeten():
    global detener
    detener = False
    return
##esconde y resetea el MainFrame para una nueva partida
##Entradas:Null
##Salidas:Null
##Restricciones:Null
def blank():
    global quienjuega,matriz,detenerturnototal,boton,tiempo,Chromturno,detener,Inicio,jugador1,largopartida,largoturno,jugador2,indiceH,indiceV,MatrizV,MatrizH,posV,posH,turno,mainFrame,up,leftt,rightt,down,app,PC,redc,bluec,derecha,bajar,izq,boton,chronometer,quien,menubar,Chrom,chronturn,Chromturn
    mainFrame.withdraw()
    app.deiconify()
    turno = False
    PC = False
    jugador1=""
    jugador2=""
    indiceH = [0,1,2,3,4,5,6]
    indiceV = [0,1,2,3,4,5]
    MatrizH = 0
    MatrizV = 0
    posV = 0
    posH = 0
    Inicio = True
    Chrom=False
    detener=True
    detenerturno = True
    detenerturnototal=True
    Chromturno = False
    controlcronometro(str(largopartida[0]),str(largopartida[1]))
    mainFrame.withdraw()
    mainFrame.protocol("WM_DELETE_WINDOW", blank)
    matriz = [
        
                [0,0,0,0,0,0,0],
                
                [0,0,0,0,0,0,0],
                
                [0,0,0,0,0,0,0],
                
                [0,0,0,0,0,0,0],
                
                [0,0,0,0,0,0,0],
                
                [0,0,0,0,0,0,0],
                
                ]
    boton = [
                [0,0,0,0,0,0,0,0],
                
                [0,0,0,0,0,0,0,0],
                
                [0,0,0,0,0,0,0,0],
                
                [0,0,0,0,0,0,0,0],
                
                [0,0,0,0,0,0,0,0],
                
                [0,0,0,0,0,0,0,0],
                
                [0,0,0,0,0,0,0,0],
                
                [0,0,0]
                
                ]
    nextmov()
    try:
        fopen = open("./extra/preferences.pref","r")
        datosextraidos = eval(fopen.readline())
        fopen.close()
        largopartida = datosextraidos[0]
        largoturno = datosextraidos[1]
        chronometer = Label(mainFrame,text=largopartida[0]+":"+largopartida[1], fg="white",font=('times', 11, 'italic bold'), bg='black')
    except:
        tosave = [largopartida,largoturno]
        os.remove("./extra/preferences.pref")
        fopen = open("./extra/preferences.pref","a")
        fopen.write(str(tosave))
        fopen.close()
        chronometer = Label(mainFrame,text=largopartida[0]+":"+largopartida[1], fg="white",font=('times', 15, 'italic bold'), bg='black')
        chronometer.grid(row=0,column=8)
    return
##Guarda la partida
##Entradas:Null
##Salidas:Null
##Restricciones:Null
def guardarpartida():
    global quienjuega,matriz,boton,Inicio,jugador1,jugador2,indiceH,indiceV,MatrizV,MatrizH,posV,posH,turno,PC,detener
    listasave = [[matriz],[PC],[Inicio],[jugador1],[jugador2],[indiceH],[indiceV],[MatrizV],[MatrizH],[posH],[posV],[turno]]
    archivo = asksaveasfilename(defaultextension=".dx")
    try:
        save = open(archivo,"a")
        save.write(str(listasave))
        save.close()
        return
    except:
        return
##Muestra el buscador de archivos para cargar partida
##Entradas:Documento
##Salidas:Null
##Restricciones:Null
def cargarpartida():
    global quienjuega,matriz,boton,Chrom,Inicio,jugador1,jugador2,indiceH,indiceV,MatrizV,MatrizH,posV,posH,turno,mainFrame,PC,rightt,leftt,up,down,app
    try:
        load = filedialog.askopenfilename(filetypes=[("Archivos DX","*.dx")])
        if load == "":
            return
        saved = open(load,"r")
        game = eval(saved.readline())
        saved.close()
        matriz = game[0][0]
        PC = game[1][0]
        Inicio = game[2][0]
        jugador1 = game[3][0]
        jugador2 =game[4][0]
        indiceH =game[5][0]
        indiceV =game[6][0]
        MatrizV =game[7][0]
        MatrizH =game[8][0]
        posV =game[9][0]
        posH =game[10][0]
        turno = not game[11][0]
        app.withdraw()
        nextmov()
        crearindices()
        crearbotones()
        Chrom = False
        mainFrame.deiconify()
    except:
        messagebox.showinfo(title="Error",message="Los datos del archivo estan dañados")
##Muestra la ventana sobre la informacion personal del creador
##Entradas:Null
##Salidas:Null
##Restricciones:Null
def about():
    top = Toplevel(app)
    top.title("Acerca de Nosotros")
    top.config(bg="white")
    top.geometry("350x120")
    top.resizable(False,False)
    lab = Label(top, text="Desarrollador: Danny Chaves\nProyecto de Taller de Programacion\n © 2014",bg="white",fg="#ff9933",font=("Arial 15 italic bold"))
    lab.pack()

#Abre la ventana Principal
app = Tk()
app.title("Connecta 4")
app.geometry("350x290")
app.resizable(False,False)

##Preferencia sobre duracion de la partida
##Entradas:2 int mediante optionmenu
##Salidas:null
##Restricciones:null
def largopartida():
    def listo(event=0):
        global chronometer,largopartida,app,tiempo,largoturno
        n1 = segundos.get()
        n2 = minutos.get()
        if n1=="0" and n2=="0":
            messagebox.showinfo("Error",message="El tiempo de la partida no puede ser 00min 00seg")
            return
        if int(n1)<10:
            n1 = "0"+n1
        if int(n2)<10:
            n2="0"+n2
        largopartida[0] = n2
        largopartida[1] = n1
        tosave = str([largopartida,largoturno])
        os.remove("./extra/preferences.pref")
        pref = open("./extra/preferences.pref", "a")
        pref.write(tosave)
        pref.close()
        controlcronometro(str(n2),str(n1))
        nombres.withdraw()
        app.deiconify()

    global app
    nombres = Toplevel(app)
    nombres.title("Connecta 4")
    nombres.title("Tiempo")
    nombres.geometry("158x100")
    nombres.resizable(False,False)
    nombres.config(bg="white")
    app.withdraw()
    label1 = Label(nombres,text="Minutos: ",font=("Times 15 bold italic"),bg="white")
    label1.grid(row=0,column=0)
    label2 = Label(nombres,text="Segundos: ",font=("Times 15 bold italic"),bg="white")
    label2.grid(row=1,column=0)
    minutos= StringVar(nombres)
    minutos.set("15")
    segundos=StringVar(nombres)
    segundos.set("0")
    mins = OptionMenu(nombres, minutos,'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59')
    mins.grid(row=0,column=1)
    segs = OptionMenu(nombres, segundos,'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59')
    segs.grid(row=1,column=1)
    bot = Button(nombres,text="Guardar Cambios",command=listo,bg="#FF9933",font=("Times 15 bold italic"))
    bot.grid(row=2,column=0,columnspan=10)
    nombres.protocol("WM_DELETE_WINDOW", lambda:[normal(),nombres.destroy()])

##Preferencia sobre la duracion del turno
##Entradas:Null
##Salidas:Null
##Restriccione:Null
def largoturnos():
    def listo(event=0):
        global chronometer,largopartida,app,tiempo,largoturno
        n1 = segundos.get()
        n2 = minutos.get()
        if n1=="0" and n2=="0":
            messagebox.showinfo("Error",message="El tiempo por turno no puede ser 00min 00seg")
            return
        if int(n1)<10:
            n1 = "0"+n1
        if int(n2)<10:
            n2="0"+n2
        largoturno = [n2,n1]
        tosave = str([largopartida,largoturno])
        os.remove("./extra/preferences.pref")
        pref = open("./extra/preferences.pref", "a")
        pref.write(tosave)
        pref.close()
        controlturno(str(n2),str(n1))
        nombres.withdraw()
        app.deiconify()

    global app
    nombres = Toplevel(app)
    nombres.title("Tiempo")
    nombres.geometry("158x100")
    nombres.resizable(False,False)
    nombres.config(bg="white")
    app.withdraw()
    label1 = Label(nombres,text="Minutos: ",font=("Times 15 bold italic"),bg="white")
    label1.grid(row=0,column=0)
    label2 = Label(nombres,text="Segundos: ",font=("Times 15 bold italic"),bg="white")
    label2.grid(row=1,column=0)
    nom = Entry(nombres,bg="black",fg="white",font=("Times 15 bold italic"),insertbackground="red")
    nom2 = Entry(nombres,bg="black",fg="white",font=("Times 15 bold italic"),insertbackground="red")
    minutos= StringVar(nombres)
    minutos.set("2")
    segundos=StringVar(nombres)
    segundos.set("0")
    mins = OptionMenu(nombres, minutos,'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59')
    mins.grid(row=0,column=1)
    segs = OptionMenu(nombres, segundos,'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59')
    segs.grid(row=1,column=1)
    bot = Button(nombres,text="Guardar Cambios",command=listo,bg="#FF9933",font=("Times 15 bold italic"))
    bot.grid(row=2,column=0,columnspan=10)
    nombres.protocol("WM_DELETE_WINDOW", lambda:[normal(),nombres.destroy()])

##Ventana para cambiar la ficha a usar cada jugador
##EntradasNull
##Salidas:Null
##Restrucciones:Null
def cambiofichas():
    global ordenarfichas
    def listo(event=0):
        global app,ficha1,coin1,ficha2,coin2,jugar1c,jugar2c,quien,ordenarfichas
        n1 = jugador1.get()
        n2 = jugador2.get()
        if n1==n2:
            messagebox.showinfo("Error",message="Ambos Jugadores no pueden tener la misma ficha")
            return
        if n1 == "Rojo":
            ficha1 = "roja"
            coin1 = "redcoin"
            pass
        elif n1 =="Azul":
            ficha1 = "azul"
            coin1 = "bluecoin"
            pass
        elif n1 =="Negro":
            ficha1 = "negro"
            coin1 = "blackc"
            pass
        elif n1 =="Verde":
            ficha1 = "verde"
            coin1 = "greenc"
            pass
        elif n1 =="Rosado":
            ficha1 = "rosa"
            coin1 = "pinkc"
            pass
        elif n1 =="FC Barcelona":
            ficha1 = "fcb"
            coin1 = "fcbc"
            pass
        elif n1 =="Real Madrid":
            ficha1 = "rm"
            coin1 = "rmc"
            pass
        elif n1 =="Trafalgar Law":
            ficha1 = "law"
            coin1 = "lawc"
            pass
        elif n1 =="Mugiwaras":
            ficha1 = "luffy"
            coin1 = "luffyc"
            pass
        elif n1 =="Mario Colita":
            ficha1 = "mariocolita"
            coin1 = "mariocolitac"
            pass
        elif n1 =="Mario World":
            ficha1 = "mariow"
            coin1 = "mariowc"
            pass
        elif n1 =="Luigi's Mansion":
            ficha1 = "luigi"
            coin1 = "luigic"
            pass
        elif n1 =="Amarillo":
            ficha1 = "amarillo"
            coin1 = "yellowc"
            pass
        elif n1 =="4 Estrellas":
            ficha1 = "4estrellas"
            coin1 = "4estrellasc"
            pass
        elif n1 =="Balon Clasico":
            ficha1 = "balonclasico"
            coin1 = "balonclasicoc"
            pass
        elif n1 =="Celeste":
            ficha1 = "celes"
            coin1 = "celeste"
            pass
        elif n1 =="Konoha":
            ficha1 = "konoha"
            coin1 = "konohac"
            pass
        elif n1 =="Python Logo":
            ficha1 = "python"
            coin1 = "pythonc"
            pass
        elif n1 =="Saprissa":
            ficha1 = "saprissa"
            coin1 = "saprissac"
            pass
        if n2 == "Rojo":
            ficha2 = "roja"
            coin2= "redcoin"
            pass
        elif n2 =="Azul":
            ficha2 = "azul"
            coin2 = "bluecoin"
            pass
        elif n2 =="Negro":
            ficha2 = "negro"
            coin2 = "blackc"
            pass
        elif n2 =="Verde":
            ficha2 = "verde"
            coin2 = "greenc"
            pass
        elif n2 =="Rosado":
            ficha2 = "rosa"
            coin2 = "pinkc"
            pass
        elif n2 =="FC Barcelona":
            ficha2 = "fcb"
            coin2 = "fcbc"
            pass
        elif n2 =="Real Madrid":
            ficha2 = "rm"
            coin2 = "rmc"
            pass
        elif n2 =="Trafalgar Law":
            ficha2 = "law"
            coin2 = "lawc"
            pass
        elif n2 =="Mugiwaras":
            ficha2 = "luffy"
            coin2 = "luffyc"
            pass
        elif n2 =="Mario Colita":
            ficha2 = "mariocolita"
            coin2 = "mariocolitac"
            pass
        elif n2 =="Mario World":
            ficha2 = "mariow"
            coin2 = "mariowc"
            pass
        elif n2 =="Luigi's Mansion":
            ficha2 = "luigi"
            coin2 = "luigic"
            pass
        elif n2 =="Amarillo":
            ficha2 = "amarillo"
            coin2 = "yellowc"
            pass
        elif n2 =="4 Estrellas":
            ficha2 = "4estrellas"
            coin2 = "4estrellasc"
            pass
        elif n2 =="Balon Clasico":
            ficha2 = "balonclasico"
            coin2 = "balonclasicoc"
            pass
        elif n2 =="Celeste":
            ficha2 = "celes"
            coin2 = "celeste"
            pass
        elif n2 =="Konoha":
            ficha2 = "konoha"
            coin2 = "konohac"
            pass
        elif n2 =="Python Logo":
            ficha2 = "python"
            coin2 = "pythonc"
            pass
        elif n2 =="Saprissa":
            ficha2 = "saprissa"
            coin2 = "saprissac"
            pass
        tosave = str([ficha1,coin1,ficha2,coin2])
        os.remove("./extra/ui.pref")
        pref = open("./extra/ui.pref", "a")
        pref.write(tosave)
        pref.close()
        jugar1c = PhotoImage(file="./extra/fichas/"+coin1+".gif")
        jugar2c = PhotoImage(file="./extra/fichas/"+coin2+".gif")
        quien.config(image=jugar1c)
        quien.image = jugar1c
        app.deiconify()
        nombres.destroy()

    global app,ordenarfichas
    nombres = Toplevel(app)
    nombres.title("Color de Ficha")
    fotos = [0,1,2,3,4,5,6,7,8,9,0,11,12,13,14,15,16,17,18]
    fotos[1] = PhotoImage(file="./extra/fichas/bluecoin.gif")
    fotos[2] = PhotoImage(file="./extra/fichas/blackc.gif")
    fotos[6] = PhotoImage(file="./extra/fichas/fcbc.gif")
    fotos[7] = PhotoImage(file="./extra/fichas/rmc.gif")
    fotos[3] = PhotoImage(file="./extra/fichas/greenc.gif")
    fotos[8] = PhotoImage(file="./extra/fichas/lawc.gif")
    fotos[9] = PhotoImage(file="./extra/fichas/luffyc.gif")
    fotos[12] = PhotoImage(file="./extra/fichas/luigic.gif")
    fotos[10] = PhotoImage(file="./extra/fichas/mariocolitac.gif")
    fotos[11] = PhotoImage(file="./extra/fichas/mariowc.gif")
    fotos[4] = PhotoImage(file="./extra/fichas/pinkc.gif")
    fotos[0] = PhotoImage(file="./extra/fichas/redcoin.gif")
    fotos[5] = PhotoImage(file="./extra/fichas/yellowc.gif")
    fotos[13] = PhotoImage(file="./extra/fichas/4estrellasc.gif")
    fotos[14] = PhotoImage(file="./extra/fichas/balonclasicoc.gif")
    fotos[15] = PhotoImage(file="./extra/fichas/celeste.gif")
    fotos[16] = PhotoImage(file="./extra/fichas/konohac.gif")
    fotos[17] = PhotoImage(file="./extra/fichas/pythonc.gif")
    fotos[18] = PhotoImage(file="./extra/fichas/saprissac.gif")
    labels = ["Rojo","Azul","Negro","Verde","Rosado","Amarillo","FC Barcelona","Real Madrid","Trafalgar Law","Mugiwaras","Mario Colita","Mario World","Luigi's Mansion","4 Estrellas","Balon Clasico","Celeste","Konoha","Python Logo","Saprissa"]
    nombres.resizable(False,False)
    nombres.config(bg="white")
    app.withdraw()
    label1 = Label(nombres,text="Jugador 1: ",font=("Times 15 bold italic"),bg="white")
    label1.grid(row=0,column=0)
    label2 = Label(nombres,text="Jugador 2: ",font=("Times 15 bold italic"),bg="white")
    label2.grid(row=1,column=0)
    nom = Entry(nombres,bg="black",fg="white",font=("Times 15 bold italic"),insertbackground="red")
    nom2 = Entry(nombres,bg="black",fg="white",font=("Times 15 bold italic"),insertbackground="red")
    jugador1= StringVar(nombres)
    jugador1.set("Rojo")
    jugador2=StringVar(nombres)
    jugador2.set("Azul")
    mins = OptionMenu(nombres, jugador1,"Rojo","Azul","Negro","Verde","Rosado","Amarillo","FC Barcelona","Real Madrid","Trafalgar Law","Mugiwaras","Mario Colita","Mario World","Luigi's Mansion","4 Estrellas","Balon Clasico","Celeste","Konoha","Python Logo","Saprissa")
    mins.place(x=110,y=0)
    segs = OptionMenu(nombres, jugador2,"Rojo","Azul","Negro","Verde","Rosado","Amarillo","FC Barcelona","Real Madrid","Trafalgar Law","Mugiwaras","Mario Colita","Mario World","Luigi's Mansion","4 Estrellas","Balon Clasico","Celeste","Konoha","Python Logo","Saprissa")
    segs.place(x=110,y=28)
    bot = Button(nombres,text="Guardar Cambios",command=listo,bg="#FF9933",font=("Times 15 bold italic"))
    bot.grid(row=2,column=0,columnspan=2)
    botones = [[0,0,0,0],[0,0,0,0]]
    def moverfichas(lado=0):
        global ordenarfichas
        k=3
        k2=0
        ordenarfichas+=lado
        for j in range(0,4):
            botones[0][j].config(image=fotos[(ordenarfichas+j)%19])
            botones[0][j].image = fotos[j]
            botones[1][j].config(text=labels[(ordenarfichas+j)%19])
            k2+=1
    botones[0][0] = Label(nombres,image=fotos[0],bg="white")
    botones[0][0].image = fotos[0]
    botones[0][0].grid(row=3,column=0)
    botones[1][0] = Label(nombres,text=labels[0],bg="white")
    botones[1][0].grid(row=4,column=0)
    botones[0][1] = Label(nombres,image=fotos[1],bg="white")
    botones[0][1].image = fotos[1]
    botones[0][1].grid(row=3,column=1)
    botones[1][1] = Label(nombres,text=labels[1],bg="white")
    botones[1][1].grid(row=4,column=1)
    botones[0][2] = Label(nombres,image=fotos[2],bg="white")
    botones[0][2].image = fotos[2]
    botones[0][2].grid(row=3,column=2)
    botones[1][2] = Label(nombres,text=labels[2],bg="white")
    botones[1][2].grid(row=4,column=2)
    botones[0][3] = Label(nombres,image=fotos[3],bg="white")
    botones[0][3].image = fotos[3]
    botones[0][3].grid(row=3,column=3)
    botones[1][3] = Label(nombres,text=labels[3],bg="white")
    botones[1][3].grid(row=4,column=3)

    derecha =Button(nombres, text="Prev",font=("Times 15 bold italic"),bd=1,bg="white", command=lambda:[moverfichas(-1)])
    derecha.grid(row=5,column=0)
    izq =Button(nombres, text="Sig",font=("Times 15 bold italic"),bd=1,bg="white",command=lambda:[moverfichas(1)])
    izq.grid(row=5,column=3)
    nombres.protocol("WM_DELETE_WINDOW", lambda:[normal(),nombres.destroy(),fixrotacionfichas()])
def fixrotacionfichas():
    global ordenarfichas
    ordenarfichas =0
    return
#revisa si existe el documento de preferencias de imagenes, si no existe lo crea y lo pone por defecto en red/blue
##Entradas:null
##Salidas:null
##Restricciones:null
def fichasdefault():
    global largopartida,largoturno,ficha1,ficha2,coin1,coin2
    try:
        archivo = open("./extra/ui.pref", "r")
        lista = eval(archivo.readline())
        archivo.close()
        ficha1 = lista[0]
        ficha2 = lista[2]
        coin1=lista[1]
        coin2=lista[3]
    except:
        lista = ["roja","redcoin","azul","bluecoin"]
        ficha1 = lista[0]
        ficha2 = lista[2]
        coin1=lista[1]
        coin2=lista[3]
        archivo = open("./extra/ui.pref", "a")
        archivo.write(str(lista))
        archivo.close()
fichasdefault()
#Imagenes a usar en las fichas
jugar1c = PhotoImage(file="./extra/fichas/"+coin1+".gif")
jugar2c = PhotoImage(file="./extra/fichas/"+coin2+".gif")
    
#Menu de la app principal
men = Menu(app)
filebar = Menu(men,tearoff=0)
filebar.add_command(label="Tiempo por Partida",command=largopartida)
filebar.add_command(label="Tiempo por Turno",command=largoturnos)
filebar.add_command(label="Color de Fichas",command=cambiofichas)
men.add_cascade(label="Preferencias",menu=filebar)
men.add_command(label="Acerca de...",command=about)
men.add_command(label="Salir",command=app.destroy)
app.config(menu=men)
#Flechas de movimiento del MainFrame
up=PhotoImage(file="./extra/up.gif")
down=PhotoImage(file="./extra/down.gif")
leftt= PhotoImage(file="./extra/left.gif")
rightt= PhotoImage(file="./extra/right.gif")
#MainFramey caracteristicas
mainFrame = Toplevel(app)
mainFrame.resizable(False,False)
#Menu del MainFrame
menubar = Menu(mainFrame)
menubar.add_command(label="Guardar Partida",command=guardarpartida)
menubar.add_command(label="Salir",command=blank)
mainFrame.config(menu=menubar)
#asigna las flechas del mainframe para mover la matriz de botones
upper = Button(mainFrame, image=up,relief=GROOVE ,command=lambda:[aumentarV(posV+1)])
upper.grid(row=0, column=0)
boton[0][0]=upper
derecha =Button(mainFrame, image=leftt,relief=GROOVE, command=lambda:[aumentarH(posH-1,-1)])
derecha.grid(row=8,column=0)
boton[7][0]=derecha
izq =Button(mainFrame, image=rightt,relief=GROOVE, command=lambda:[aumentarH(posH+1,1)])
izq.grid(row=8,column=7)
boton[7][1]=izq
bajar = Button(mainFrame,image=down ,relief=GROOVE ,command=lambda:[aumentarV(posV-1)])
bajar.grid(row=8, column=3,columnspan=2)
boton[7][2]=bajar
#Nombre del jugador
quienjuega = Label(mainFrame,text=jugador1,font=("Times 15 italic bold"),width=10)
#Fichas del jugador actual
quien = Label(mainFrame,image=jugar1c)
quien.grid(row=6,column=8)
quienjuega.grid(row=8,column=8)
mainFrame.withdraw()
#Activa blank al cerrar la ventana MainFrame
mainFrame.protocol("WM_DELETE_WINDOW", blank)

#Pide los nombres del jugador 1/Jugador 2
##Entradas:2 nombres
##Salidas:mainFrame/app
##Restricciones:null
def selectname():
    def listo(event=0):
        global jugador1,jugador2,quienjuega,app,detener
        n1 = nom.get()
        n2 = nom2.get()
        if n1==n2:
            messagebox.showinfo(title="ERROR",message="Los nombres no pueden ser iguales")
            return
        if n1=="" or n2=="":
            messagebox.showinfo(title="ERROR",message="El nombre no puede ser vacio")
            return
        quienjuega.config(text=n1)
        jugador1 = n1
        jugador2 = n2
        crearbotones()
        crearindices()
        mainFrame.title(n1+" vs. "+n2)
        detener = False
        nombres.withdraw()
        mainFrame.deiconify()
    global app
    nombres = Toplevel(app)
    nombres.config(bg="white")
    app.withdraw()
    texto = "Nombre del Jugador "
    label1 = Label(nombres,text=texto+str(1),font=("Times 15 bold italic"),bg="white")
    label1.grid(row=0,column=0)
    label2 = Label(nombres,text=texto+str(2),font=("Times 15 bold italic"),bg="white")
    label2.grid(row=1,column=0)
    nom = Entry(nombres,bg="black",fg="white",font=("Times 15 bold italic"),insertbackground="red")
    nom2 = Entry(nombres,bg="black",fg="white",font=("Times 15 bold italic"),insertbackground="red")
    nom.grid(row=0,column=1)
    nom2.grid(row=1,column=1)
    nom.bind("<Return>",listo)
    nom2.bind("<Return>",listo)
    bot = Button(nombres,text="Iniciar Juego",command=listo,bg="#FF9933",font=("Times 15 bold italic"))
    bot.grid(row=2,column=0,columnspan=10)
    nombres.protocol("WM_DELETE_WINDOW", lambda:[normal(),nombres.destroy()])
##Muestra la ventana app
##Entradas:null
##Salidas:null
##Restricciones:null
def normal():
    global app
    app.deiconify()
##Pide el nombre del jugador en sigle player
##Entradas:Nombre en entry
##Salidas:null
##Restricciones:null
def singleplayer():
    def listo(event=0):
        global jugador1,jugador2,quienjuega,app,PC,detener
        n1 = nom.get()
        n2 = "CPU"
        if n1==n2:
            messagebox.showinfo(title="ERROR",message="El nombre CPU es unicamente para la Computadora")
            return
        if n1=="":
            messagebox.showinfo(title="ERROR",message="El nombre no puede ser vacio")
            return
        quienjuega.config(text=n1)
        PC = True
        jugador1 = n1
        jugador2 = n2
        crearbotones()
        crearindices()
        detener = False
        mainFrame.title(n1+" vs. "+n2)
        nombres.withdraw()
        mainFrame.deiconify()
    global app
    app.withdraw()
    nombres = Toplevel(app)
    nombres.resizable(False,False)
    nombres.config(bg="white")
    texto = "Nombre del Jugador "
    label1 = Label(nombres,text=texto+"  ",font=("Times 15 bold italic"),bg="white")
    label1.grid(row=0,column=0)
    nom = Entry(nombres,bg="black",fg="white",font=("Times 15 bold italic"),insertbackground="red")
    nom.grid(row=0,column=1)
    bot = Button(nombres,text="Iniciar Juego",command=listo,bg="#FF9933",font=("Times 15 bold italic"))
    bot.grid(row=2,column=0,columnspan=10)
    nom.bind("<Return>",listo)
    nombres.protocol("WM_DELETE_WINDOW", lambda:[normal(),nombres.destroy()])
##Muestra la ventana de records
##Entradas:Null
##Salidas:Null
##Restricciones:Null
def showrecords():
    global app
    app.withdraw()
    record = Toplevel(app,width=250)
    record.config(bg="#6699FF")
    record.title("Records")
    record.protocol("WM_DELETE_WINDOW", lambda:[normal(),record.destroy()])
    try:
        file = open("./extra/datos.txt","r")
        line = eval(file.readline())
        rows=1
        cols =0
        i = len(line)
        k=0
        result = []
        texto = Label(record,text="Records",font=("Times 15 bold italic"),bg="#6699FF",fg="white")
        texto.grid(row=0, column=1,columnspan=1)
        while len(result)<i:
            result+=[[[],[]]]
        for j in line:
            result[k][0] = Label(record,text=str(j[0])+":",font=("Times 15 bold italic"),bg="#6699FF",fg="white")
            result[k][0].grid(row=rows, column=cols)
            result[k][1] = Label(record,text=str(j[1]),font=("Times 15 bold italic"),bg="#6699FF",fg="white")
            result[k][1].grid(row=rows,column=cols+4)
            rows+=1
    except:
        texto = Label(record,text="Aun no hay records disponibles",font=("Times 15 bold italic"),fg="white",bg="#6699FF")
        texto.grid(row=0, column=0,columnspan=2)
#Guarda el tiempo de la partida/turno
largopartida = []
largoturno = []
#revisa si existe el documento de preferencias, si no existe lo crea y lo pone por defecto en 15min 00seg
##Entradas:null
##Salidas:null
##Restricciones:null
def changedefault():
    global largopartida,largoturno
    try:
        archivo = open("./extra/preferences.pref", "r")
        lista = eval(archivo.readline())
        archivo.close()
        largopartida = lista[0]
        largoturno = lista[1]
    except:
        lista = [["15","00"],["02","00"]]
        largopartida= lista[0]
        largoturno = lista[1]
        archivo = open("./extra/preferences.pref", "a")
        archivo.write(str(lista))
        archivo.close()
changedefault()
#Opciones de la ventana principal
Multi = Button(app,text="Multijugador",command=selectname,bg="red",font=("Arial 15 italic bold"),fg="white")
Multi.pack(fill=X,ipady=12)
cargar = Button(app,text="Cargar Partida",command=cargarpartida,bg="#33CC33",font=("Arial 15 italic bold"),fg="white")
cargar.pack(fill=X,ipady=12)
compu = Button(app,text="Un Jugador",command=singleplayer,bg="#6699FF",font=("Arial 15 italic bold"),fg="white")
compu.pack(fill=X,ipady=12)
rec = Button(app,text="Ver Records",command=showrecords,bg="#FF9933",font=("Arial 15 italic bold"),fg="white")
rec.pack(fill=X,ipady=12)
#Reloj del horario del servidor
##Entradas:null
##Salidas:null
##Restricciones:null
def tick():
    global time1
    time2 = time.strftime('%H:%M:%S')
    if time2 != time1:
        time1 = time2
        clock.config(text="Hora del Servidor:"+time2)
    clock.after(200, tick)
#cronometro que descuenta el tiempo para el largo de partida
##Entradas:2 int
##Salidas:null
##Restricciones:2 int
def cronometro(mins,segs):
    global chronometer,detener,tiempo
    mins = int(mins)
    segs= int(segs)
    segs-=1
    if detener:
        chronometer.after(1000, lambda:[normaldeten()])
        return
    if segs == -1:
        segs = 59
        mins-=1
    if mins ==-1:
        return 
    if segs<10:
        segs = "0"+str(segs)
        pass
    if mins<10:
        mins="0"+str(mins)
        pass
    if mins=="00" and segs=="00":
        return timesup()
    controlcronometro(str(mins),str(segs))
    chronometer.after(1000, lambda:[cronometro(int(mins),int(segs))])
#controla el cronometro a mostrarse y modifica las imagenes de numeros que aparecen en el MainFrame
##Entradas:2 strings con 2 numeros cada uno
##Salidas:null
##Restricciones:2 strings con 2 numeros cada uno
def controlcronometro(mins,segs):
    global min1,min2,seg1,seg2
    minmayor = mins[0]
    minmenor = mins[1]
    segsmayor = segs[0]
    segsmenor = segs[1]
    abrirminmayor = PhotoImage(file="./extra/"+minmayor+".gif")
    abrirminmenor = PhotoImage(file="./extra/"+minmenor+".gif")
    abrirsegmayor = PhotoImage(file="./extra/"+segsmayor+".gif")
    abrirsegmenor = PhotoImage(file="./extra/"+segsmenor+".gif")
    min1.config(image=abrirminmayor)
    min1.image = abrirminmayor
    min2.config(image=abrirminmenor)
    min2.image = abrirminmenor
    seg1.config(image=abrirsegmayor)
    seg1.image = abrirsegmayor
    seg2.config(image=abrirsegmenor)
    seg2.image = abrirsegmenor
    return
tiempo = "Tiempo restante: "
proximoturno = "Proximo Turno: "
#Dos puntos en medio del cronometro
dotdot= PhotoImage(file="./extra/_.gif")
#Variable que activa la actualizacion del cronometro y muestra tiempo restante
chronometer = Label(mainFrame,text=tiempo,fg="red",font="Times 15 italic")
chronometer.grid(row=0,column=8)
#Numeros del cornometro
min1 = Label(mainFrame)
min1.place(x=660,y=70)
min2 = Label(mainFrame)
min2.place(x=675,y=70)
doubledot = Label(mainFrame,image=dotdot)
doubledot.place(x=690,y=70)
seg1 = Label(mainFrame)
seg1.place(x=705,y=70)
seg2 = Label(mainFrame)
seg2.place(x=720,y=70)
time1 = ''

##Detecta el cambio de turno y resetea el cronometro de duracion de turno
##Entradas:Null
##Salidas:Null
##Restrucciones:Null
def normaldetenturno():
    global detenerturno,largoturnos,detenerturnototal
    detenerturno = False
    cronoturn(largoturno[0],largoturno[1])
    return
##Hace funionar el cronometro de la duracion de cada turno
##Entradas:2 string con numeros
##Salidas:Null
##Restricciones:solo 2 strings con numeros
def cronoturn(mins,segs):
    global chronoturno,detenerturno,tiempo,detenerturnototal
    mins = int(mins)
    segs= int(segs)
    segs-=1
    if detenerturnototal:
        detenerturnototal=False
        return controlturno(largoturno[0],largoturno[1])
    if detenerturno:
        chronoturno.after(10, lambda:[normaldetenturno()])
        return
    if segs == -1:
        segs = 59
        mins-=1
    if mins ==-1:
        return 
    if segs<10:
        segs = "0"+str(segs)
        pass
    if mins<10:
        mins="0"+str(mins)
        pass
    if mins=="00" and segs=="00":
        return timesupturn()
    controlturno(str(mins),str(segs))
    chronoturno.after(1000, lambda:[cronoturn(int(mins),int(segs))])
##Muestra mensaje de que se acabo el tiempo para jugar y cambia el turno
##Entradas:Null
##Salidas:Null
##Restricciones:Null
def timesupturn():
    global mainFrame,turno,jugador1,jugador2,detenerturno
    mainFrame.withdraw()
    winner = jugador1
    if turno:
        winner = jugador2
        pass
    messagebox.showinfo("Tiempo Fuera",message="Se a acabado el tiempo, ahora es el turno de "+winner)
    normaldetenturno()
    nextmov()
    return mainFrame.deiconify()
#controla el cronometro de turno a mostrarse y modifica las imagenes de numeros que aparecen en el MainFrame
##Entradas:2 strings con 2 numeros cada uno
##Salidas:null
##Restricciones:2 strings con 2 numeros cada uno
def controlturno(mins="01",segs="00"):
    global resturn1,resturn2,resturn3,resturn4
    minmayor = mins[0]
    minmenor = mins[1]
    segsmayor = segs[0]
    segsmenor = segs[1]
    abrirminmayor = PhotoImage(file="./extra/"+minmayor+".gif")
    abrirminmenor = PhotoImage(file="./extra/"+minmenor+".gif")
    abrirsegmayor = PhotoImage(file="./extra/"+segsmayor+".gif")
    abrirsegmenor = PhotoImage(file="./extra/"+segsmenor+".gif")
    resturn1.config(image=abrirminmayor)
    resturn1.image = abrirminmayor
    resturn2.config(image=abrirminmenor)
    resturn2.image = abrirminmenor
    resturn3.config(image=abrirsegmayor)
    resturn3.image = abrirsegmayor
    resturn4.config(image=abrirsegmenor)
    resturn4.image = abrirsegmenor
    return
##Variables del cronometro del turno
chronoturno = Label(mainFrame,text=proximoturno,fg="red",font="Times 15 italic")
chronoturno.place(x=660,y=160)
resturn1 = Label(mainFrame)
resturn1.place(x=660,y=200)
resturn2 = Label(mainFrame)
resturn2.place(x=675,y=200)
heredot = doubledot
heredot.place(x=690,y=200)
resturn3 = Label(mainFrame)
resturn3.place(x=705,y=200)
resturn4 = Label(mainFrame)
resturn4.place(x=720,y=200)
####################################
time1 = ''
#Reloj
clock = Label(app, fg="white",font=('times', 15, 'italic bold'), bg='black')
clock.pack(fil=X,ipady=5)
#Activa relo del servidor
tick()
#acomoda el cronometro con los valores de iniciar partida sin modificar el archivo en preferencias
controlcronometro(largopartida[0],largopartida[1])
controlturno(largoturno[0],largoturno[1])
app.mainloop()

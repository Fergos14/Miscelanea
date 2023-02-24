import matplotlib.pyplot as plt
#SE IMPORTA PARA GRAFICAR


def ordenacion_abscisas(a):
    if (a[0] > a[1]):  # a[0]=X1 / a[1]=X2
        temp = a[0]
        a[0] = a[1]
        a[1] = temp
    return a
    # FUNCION QUE ORDENA LOS VALORES DE LAS ABSCISAS (DE MENOR A MAYOR)

def actualizar_temporales(i, E, B):
    #I=El iterador de cada ronda (es decir de cada eje)
    # B= la matriz de los ejes [[#Abcisa,#Ordenada=0, ['E1','E2'], [Altura de E1, Altura de E2]]],
    # E= Los edificios temporales [[Edifcios],[Alturas]]
    for h in range(len(B[i][2])):
        if B[i][2][h] in E[0]:
            E[0].remove(B[i][2][h])
            E[1].remove(B[i][3][h])
        elif B[i][2][h] not in E[0]:
            E[0].append(B[i][2][h])
            E[1].append(B[i][3][h])
    return E
    # FUNCION QUÉ ACTUALIZA LOS EDIFICIOS TEMPORALES POR EJE

def input_corregido(mensaje):
    while True:
        try:
            rawinput = int(input(mensaje))
            if rawinput < 0:
                print("Valor erróneo")
                continue
        except ValueError:
            print("Valor erróneo")
            continue
        else:
            return rawinput
            break
    #FUNCION QUE PERMITE QUE LOS DATOS INGRESADOS NO SEAN STRING O NEGATIVO

class edificios:
    def __init__(self):
        self.Edificio = []
        for i in range(3):  # ENTRADA DEL X1, X2, y el Y
            if i < 2:
                dato = input_corregido(f"Ingrese el valor X{i + 1}: ")
            else:
                dato = input_corregido(f"Ingrese el valor de la altura : ")
            if i == 1:
                compara = (dato == self.Edificio[0])
                while compara == True:
                    dato = input_corregido("Ingrese valor diferente, el ancho no puede ser 0: ")
                    if dato != self.Edificio[0]:
                        compara = False
                # Validación para que el ancho no sea cero
            if i == 2:
                while dato <= 0:
                    dato = input_corregido("Ingrese valor diferente, la altura no puede ser menor o igual que 0: ")
                # Validación para que la altura no sea cero
            self.Edificio.append(dato)
        self.Edificio = ordenacion_abscisas(self.Edificio)
        # Ordenamiento del X1 y X2
        #EL EDIFICIO COMO [X1,X2,Y] ESTÁ CREADO


class ciudad():
    def __init__(self):
        n = input_corregido("Ingrese el número de edificios: ")
        # Los edificios se deben crear uno por uno
        if n==0:
            plt.plot()
            plt.show()
            exit()
        self.lista_edificios = []
        for i in range(n):  # AGREGA EDIFICIO Y LE AÑADE UN NOMBRE A CADA UNO (EL NOMBRE ES IMPORTANTE)
            print(f"Ingresar datos del {i + 1}° edificio")
            self.lista_edificios.append(edificios().Edificio)
            self.lista_edificios[i].append((f"Edificio {i + 1}"))
    # LA LISTA DE EDIFICIOS FUE CREADA

    def lista_ejes(self):  # TE DEVUELVE LA LISTA DE LOS EJES [[X1 , 0, ['E1','E2'...], [Altura de E1 (Y1), Altura de E2 (Y2)...]]...]
        lista_ejes = []
        for filas in range(len(self.lista_edificios)):  # Reconoce los ejes y crea la lista de ejes vacías (sin ningún dato)
            # EL BUCLE RECORRE TODOS LOS EDIFICIOS
            if [self.lista_edificios[filas][0], 0, [], []] not in lista_ejes: #Crea el eje para el X1 del edificio(si es que no hay)
                lista_ejes.append([self.lista_edificios[filas][0], 0, [], []])
            if [self.lista_edificios[filas][1], 0, [], []] not in lista_ejes:#Crea el eje para el X2 del edificio (si es que no hay)
                lista_ejes.append([self.lista_edificios[filas][1], 0, [], []])
        # EN ESTE PUNTO YA ESTÁ CREADA TODA LA MATRIZ DE EJES, PERO FALTA LLENAR CON LOS DATOS DE LOS EDIFICIOS Y SUS RESPECTIVAS ALTURAS
        for edifcios in range(len(self.lista_edificios)):  # Cuenta a la cantidad de edifcios de la ciudad
            #EL BUCLE RECORRE TODOS LOS EDIFICIOS
            for i in range(len(lista_ejes)):
                #EL BUCLE RECORRE A TODA LA LISTA DE EJES
                if lista_ejes[i][0] == self.lista_edificios[edifcios][0]:
                # Clasifica al punto X1 de un edificio(X1,X2,Y,"E") con un eje
                    lista_ejes[i][3].append(self.lista_edificios[edifcios][2])
                    # Agrega el nombre del edifcio ("E")
                    lista_ejes[i][2].append(self.lista_edificios[edifcios][3])
                    # Agrega a la altura del punto X1= Y1, (el X1 ya lo forma el eje)

                if lista_ejes[i][0] == self.lista_edificios[edifcios][1]:
                # Clasifica al punto X2 de un edificio con un eje
                    lista_ejes[i][3].append(self.lista_edificios[edifcios][2])
                    # Agrega el nombre del edifcio("E")
                    lista_ejes[i][2].append(self.lista_edificios[edifcios][3])
                    # Agrega a la altura del punto X2= Y1, (el X1 ya lo forma el eje)
                    # No necesariamente los puntos de los edifcios se clasifican en este eje, por ello recorre a todos los ejes
        lista_ejes = sorted(lista_ejes, key=lambda x: x[0])
        # Ordena la lista de los ejes por eje de menor a mayor
        return lista_ejes
    # LA LISTA DE EJES FUE CREADA

    def skyline(self):
        # cada vez que se agregue un punto al skyline sumar 1 al contador, para así no perder el último punto
        # lista_ejes= la matriz de los ejes [[#Abcisa,#Ordenada=0, ['E1','E2'], [Altura de E1, Altura de E2]]],
        # temporales= Los edificios temporales  [[Edificios], [Alturas]]
        # skyline= matriz del skyline
        # c= contador para no perder el último punto de la lista de skyline
        # Recordar que trabajamos con la máxima altura de cada eje -> max(lista_ejes[x][3])
        # Recordar que trabajamos con la máxima altura de cada la lista de temporales ->max(temporales[1])
        lista_ejes = self.lista_ejes()
        temporales = [[], []]
        skyline = []
        c = -1
        for i in range(len(lista_ejes)):
            # EL BUCLE RECORRE A TODA LA LISTA DE EJES
            if len(temporales[1]) == 0:
            #CUANDO NO HAY EDIFICIOS TEMPORALES EN EL EJE
                if skyline != []:
                    skyline.append([skyline[c][0], 0])
                    c = c + 1
                #Si es que no es el punto inicial, agrega el punto (abscisa del último punto del skyline, altura 0)
                skyline.append([lista_ejes[i][0], 0])
                #Agrega el punto (abscisa del eje, altura 0)
                skyline.append([lista_ejes[i][0], max(lista_ejes[i][3])])
                #Agrega el punto (abscisa del eje, altura máxima del eje)
                c = c + 2
            else:
            #CUANDO HAY EDIFICIOS TEMPORALES EN EL EJE
                if skyline[c][1] > max(temporales[1]):
                #Cuando la altura del edificio que se acabó es mayor al edificio temporal
                    skyline.append([skyline[c][0], max(temporales[1])])
                    # Agrega el punto que conecta con el edificio temporal
                    skyline.append([lista_ejes[i][0], max(temporales[1])])
                    # Luego agrega el punto de union entre edificio temporal  el otro edificio
                    if max(lista_ejes[i][3]) > max(temporales[1]):
                        skyline.append([lista_ejes[i][0], max(lista_ejes[i][3])])
                        c = c + 1
                        #Si es que la maxima altura del eje fuera mayor que la maxima altura de los edificios temporales, se agrega el punto (abscisa de eje, altura de eje)
                    c = c + 2
                else:
                #Cuando el edificio aún no termina (y el útlimo punto del skyline sigue mantiendo la mayor altura)
                    if skyline[c][1] > max(lista_ejes[i][3]):
                        pass
                        #No agrega puntos, sigue de largo
                    elif skyline[c][1] == max(lista_ejes[i][3]):
                        skyline.append([lista_ejes[i][0], max(lista_ejes[i][3])])
                        c = c + 1
                        #Agrega el punto del siguiente eje (abscisa de eje, altura de eje)
                    else:
                        skyline.append([lista_ejes[i][0], skyline[c][1]])
                        #Agrega el punto (abscisa de eje, altura de edificio temporal)
                        skyline.append([lista_ejes[i][0], max(lista_ejes[i][3])])
                        #Luego agrega el punto (abscisa de eje, altura de eje)
                        c = c + 2
            temporales = actualizar_temporales(i, temporales, lista_ejes)
        skyline.append([skyline[len(skyline) - 1][0], 0])
        #AGREGA AL PUNTO DE UNIÓN CON EL EJE X (PARA FINALIZAR EL SKYLINE)
        return skyline
    # LA LISTA DEL SKYLINE FUE CREADA

    def calcular_area(self):
        A = []
        x = self.lista_edificios
        for i in range(len(x)):
            A.append((x[i][1] - x[i][0]) * x[i][2])
        return A
    # LAS AREAS SON HALLADAS

    def calcular_perimetro(self):
        P = []
        x = self.lista_edificios
        for i in range(len(x)):
            P.append(2 * (x[i][1] - x[i][0]) + 2 * x[i][2])
        return P
    # EL PERIMETRO ESTÁ CALCULADO

    def calcular_datos(self):
        x = self.lista_edificios
        print("-----Datos-----")
        for i in range(len(x)):
            print(f"El área y perimetro del {self.lista_edificios[i][3]} son {self.calcular_area()[i]}u² y {self.calcular_perimetro()[i]}u respectivamente ")
        return("")
    #MUESTRA LOS DATOS DEL PERÍMETRO Y ARÉA DE CADA EDIFICIO AL USUARIO

    def graficar(self):
        fig, a = plt.subplots(2)
        #USAMOS SUBPLOTS PARA DIVIDIR AL GRÁFICO EN 2
        X = []
        Y = []
        Leyendas = []
        for i in range(len(self.skyline())):
            X.append(self.skyline()[i][0])
            Y.append(self.skyline()[i][1])
        a[0].plot(X, Y)
        a[0].set_title('Skyline')
        a[0].set_ylim(0, max(Y) * 1.25)
        a[0].set_xlim(0, max(X) * 1.25)
        #HEMOS GRAFICADO EL SKYLINE (Primer Plot)
        for i in range(len(self.lista_edificios)):
            X1 = [self.lista_edificios[i][0], self.lista_edificios[i][0], self.lista_edificios[i][1],
                  self.lista_edificios[i][1]]
            Y1 = [0, self.lista_edificios[i][2], self.lista_edificios[i][2], 0]
            a[1].plot(X1, Y1)
            Leyendas.append(self.lista_edificios[i][3])
        a[1].set_title('Ciudad')
        a[1].set_ylim(0, max(Y) * 1.25)
        a[1].set_xlim(0, max(X) * 1.25)
        a[1].legend(labels=Leyendas, loc='upper right')
        #HEMOS GRAFICADO CADA EDIFICIO POR SEPARADO (Segundo Plot)
        plt.show()
    # EL GRAFICO DEL SKYLINE Y EL GRAFICO DE LA CIUDAD SE MUESTRAN



x = ciudad()
y = x.lista_ejes()
z = x.skyline()
print(x.calcular_datos())
x.graficar()


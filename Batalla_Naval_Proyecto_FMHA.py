#Proyecto: Juego batalla naval

class Navio:
    def __init__(self, nombre, tamaño):
        self.nombre = nombre
        self.tamaño = tamaño
        self.posiciones = []
        self.golpes = 0

    def ubi_navio(self, start_fila, start_columna, direccion, tablero):
        posiciones = []
        if direccion == 'H':#horizontal
            if start_columna + self.tamaño > len(tablero[0]):
                return False
            for i in range(self.tamaño):
                if tablero[start_fila][start_columna + i] != ' ':
                    return False
                posiciones.append((start_fila, start_columna + i))
        elif direccion == 'V':#vertical
            if start_fila + self.tamaño > len(tablero):
                return False
            for i in range(self.tamaño):
                if tablero[start_fila + i][start_columna] != ' ':
                    return False
                posiciones.append((start_fila + i, start_columna))
        else:
            return False   

        for pos in posiciones:
            tablero[pos[0]][pos[1]] = self.nombre[0]
        self.posiciones = posiciones
        return True

    def golpe(self):
        self.golpes += 1
        return self.golpes == self.tamaño
    
class Fragatra(Navio):
    def __init__(self):
        super().__init__('Fragata', 2)

class Destructor(Navio):
    def __init__(self):
        super().__init__('Destructor', 3)

class Acorazado(Navio):
    def __init__(self):
        super().__init__('Acorazado', 4)

class jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tablero = [[' ' for _ in range(10)] for _ in range (10)]
        self.navios = []
        self.golpes = [[' ' for _ in range(10)] for _ in range (10)]

    def ubi_navios(self):
        navios = [Fragatra(), Destructor(), Acorazado()]
        for navio in navios:
            while True:
                print(f"{self.nombre}, coloca tu {navio.nombre} de tamaño {navio.tamaño}.")
                start_fila = int(input("Fila inicial: "))
                start_columna = int(input("Columna inicial: ")) 
                direccion = input("Direccion (H para horizontal, V para vertical): ").upper()
                if navio.ubi_navio(start_fila, start_columna, direccion, self.tablero):
                    self.navios.append(navio)
                    self.print_tablero(self.tablero)
                    break
                else:
                    print("Posicion invalida, ingresa cordenadas de nuevo")
                
    def print_tablero(self, tablero):
        for fila in tablero:
            print(" ".join(fila))
        print()

    def ataque(self, oponente):
        while True:
            print(f"{self.nombre}, elige una posicion para atacar")
            fila = int(input('Fila: '))
            columna = int(input('Columna: '))
            if 0 <= fila < 10 and 0 <= columna < 10:
                if oponente.tablero[fila][columna] == ' ':
                    print("Impacto No acertado :c")
                    self.golpes[fila][columna] = 'A'
                    oponente.tablero[fila][columna] = 'A'
                    break
                elif oponente.tablero[fila][columna] != 'A':
                    print("Impacto Acertado")
                    self.golpes[fila][columna] = 'T'
                    for navio in oponente.navios:
                        if (fila, columna) in navio.posiciones:
                            if navio.golpe():
                                print(f"Destruido, has hundido en {navio.nombre}")
                            break
                    oponente.tablero[fila][columna] = 'T'
                    break
                else:
                    print("Posicion ya atacada, elige otras coordenadas.")
            else:
                print("Posicion de ataque no valida, elige otras cordenadas") 

    def todos_navios_hundidos(self):
        return all(navio.golpes == navio.tamaño for navio in self.navios)   

#Inicio de datos del jugador
print("Bienvenido al juego de Batalla Naval contra la IA!")
player1 = input("Escriba su nombre Capitan: ")
player2 = input("Escriba su nombre Capitan: ")

class BatallaNaval:
    def __init__(self):
        self.jugador1 = jugador(player1)
        self.jugador2 = jugador(player2)

    def juego(self):
        print("Capitan " + player1 + " coloque su flota.") 
        self.jugador1.ubi_navios()
        print("Capitan " + player2 + " coloque su flota.") 
        self.jugador2.ubi_navios()
        
        jugador_actual = self.jugador1
        oponente = self.jugador2

        while True:
            jugador_actual.ataque(oponente)
            if oponente.todos_navios_hundidos():
                print(f"Â¡{jugador_actual.nombre} ha ganado el juego!")
                break
            jugador_actual, oponente = oponente, jugador_actual

# Crear una instancia y ejecutar para programar
game = BatallaNaval()
game.juego()
class Carro:

    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidad=0
        self.encendido = False
        self.historial_velocidad = [0]


    def mostrar_estado(self):
        print("================================")
        print("Estado del carro:")
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Ano:", self.ano)
        print("Velocidad:", self.velocidad, " km/h")
        print("Encendido:", self.encendido)
        print("Historial de velocidad:", self.historial_velocidad)
        print("================================")
        print("")

    def encender(self):
        print("Modelo:", self.modelo)
        print("Variable encendido:", self.encendido)
        if self.encendido == True:
            print("El carro ya está encendido ya puedes trabajar en el.")
        else:
            self.encendido = True
            print("El carro ha sido encendido.")
        
        print("================================")
        print("")

    def acelerar(self, cantidad):
        # if de vanguardia
        if not self.encendido or cantidad <= 0:
            print("El carro está apagado. No se puede acelerar. o la cantidad sea mayor a 0")
            return
        
        ##Aqui
        for alias in range(cantidad):
            self.velocidad += 10
            self.historial_velocidad.append(self.velocidad)
            print("Acelerando... Velocidad actual:", self.velocidad, " km/h")

    
    def frenar(self):
        # if de vanguardia
        if not self.encendido or self.velocidad <= 0:
            print("El carro está apagado. No se puede frenar. o la velocidad es menor o igual a 0")
            return

        while self.velocidad >0:
            self.velocidad -= 10
            self.historial_velocidad.append(self.velocidad)
            print("Frenando... Velocidad actual:", self.velocidad, " km/h")
        

        

        

    
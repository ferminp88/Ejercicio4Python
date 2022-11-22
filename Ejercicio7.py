
class Alumno:

    def initialize(self, nombre ,nota):
        self.nombre=nombre
        self.nota=nota

    def imprimir(self):
        print("Nombre: ",self.nombre)
        print("Nota: ",self.nota)


    def resultado(self):
        if self.nota < 4:
            print("No ha aprobado")
        else:
            print("Ha aprobado")

alumno=Alumno()

alumno.initialize("Carlos",4)

alumno.imprimir()
alumno.resultado()



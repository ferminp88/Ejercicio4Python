import operaciones.sumador.suma
import operaciones.divisor.dividir
import operaciones.multiplicador.multiplica
import operaciones.restador.resta



def main():
    suma = operaciones.sumador.suma.suma(2, 4)
    divide = operaciones.divisor.dividir.divisor(1, 2)
    resta = operaciones.restador.resta.resta(2, 4)
    multi = operaciones.multiplicador.multiplica.multi(2, 5)

    print(suma, divide, resta, multi)


if __name__ == '__main__':
    main()

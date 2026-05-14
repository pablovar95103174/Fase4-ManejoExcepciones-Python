class Calculadora:

    def division(self, num1, num2):
        try:
            resultado = num1 / num2
            return resultado

        except ZeroDivisionError:
            return "Error: No se puede dividir entre cero"

        except TypeError:
            return "Error: Debe ingresar valores numéricos"

        finally:
            print("Operación finalizada")


calculadora = Calculadora()

print(calculadora.division(10, 2))
print(calculadora.division(5, 0))
print(calculadora.division(8, "a"))

import sympy as sp

class Function:
    def __init__(self, expression):
        self.expression = sp.sympify(expression)
        self.variables = list(self.expression.free_symbols)

    def calculate_derivative(self):
        derivative = sp.diff(self.expression, self.variables[0])
        return derivative

def main():
    while True:
        try:
            expression = input("Por favor, insira a função (em termos de x): ")
            func = Function(expression)
            derivative = func.calculate_derivative()
            print("A derivada da função é:", derivative)
        except (sp.SympifyError, ValueError, TypeError) as e:
            print("Erro ao processar a expressão:", e)
            print("Certifique-se de que a expressão está correta e bem formatada.")
        option = input("Continuar [S/n]: ").strip().lower()
        if option != 's':
            break

if __name__ == "__main__":
    main()

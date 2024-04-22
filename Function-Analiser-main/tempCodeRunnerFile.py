import sympy as sp
import matplotlib.pyplot as plt

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
            plot_function_and_derivative(func, derivative)
        except (sp.SympifyError, ValueError, TypeError) as e:
            print("Erro ao processar a expressão:", e)
            print("Certifique-se de que a expressão está correta e bem formatada.")
        option = input("Continuar [S/n]: ").strip().lower()
        if option != 's':
            break

def plot_function_and_derivative(func, derivative):
    x_vals = sp.linspace(-10, 10, 400)
    func_lambda = sp.lambdify(func.variables[0], func.expression, 'numpy')
    derivative_lambda = sp.lambdify(func.variables[0], derivative, 'numpy')
    func_values = func_lambda(x_vals)
    derivative_values = derivative_lambda(x_vals)
    
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.plot(x_vals, func_values, label='Função original')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Função original')
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(x_vals, derivative_values, label='Derivada')
    plt.xlabel('x')
    plt.ylabel("f'(x)")
    plt.title('Derivada')
    plt.legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()

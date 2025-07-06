# > FUNÇÕES

# 1.O que são funções?
# Funções são blocos de código que realizam uma tarefa específica e podem ser reutilizados em diferentes partes do programa. Elas ajudam a organizar o código, tornando-o mais legível e modular.

# 2. Criação de funções

# Função inicial

def saudacao():
    print('Olá, seja bem-vindo!')


saudacao()

# 3. Função com parâmetros


def saudacao(nome):
    print(f'Olá, {nome}, seja bem-vindo!')


saudacao('Matheus')

# 4. Função com pârâmetros default


def saudacao(nome, curso='Python'):
    print(f'Olá, {nome}, seja bem-vindo!')
    print(f'Você está no curso de {curso}.')


saudacao('Matheus', 'c++')


# 5. Função com retorno

def soma(a, b):
    
    return a + b
    #print(f'A soma de {a} + {b} é igual a {a + b}')

resultado= soma(10, 20)

print(f'O resultado da soma é: {resultado}')


def calculadora(num1, num2, operacao='soma'):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        return num1 / num2
    else:
        return 'Operação inválida!'
    
    
resultado_calculo = calculadora(10, 5, '+')

print(f'O resultado da operação é: {resultado_calculo}')
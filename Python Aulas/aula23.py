"""
**************************************************
AULA 22
**************************************************        
        TRATAMENTO DE ERROS E EXCEÇÕES
        Existem erros e exceções:

        Erros:
        - Erro de Sintaxe
        
        Exceções:
        - NameError
        - ValueError
        - ZeroDivisionError
        - TypeError
        - IndexError
        - KeyError
        - ModuleNotFoundError
        - etc.
"""
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    div = a/b
#except Exception:
    #print('Infelizmente tivemos um problema :(')
    #print(f'O problema encontrado foi {Exception.__class__}')
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except (ZeroDivisionError):
    print('Não é possível dividir um número por zero!')
except(KeyboardInterrupt):
    print('\nO usuário preferiu não informar os dados!')
except Exception:
    print(f'O erro encontrado foi {Exception.__cause__}')
else:
    print(f'O resutado é {div:.1f}')
finally:
    print('Volte sempre! Muito obrigado!')
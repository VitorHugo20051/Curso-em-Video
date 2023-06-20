try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b

except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Você não pode dividir por zero.')
except KeyboardInterrupt:
    print('O usuário preferiu não digitar nada.')
else:
    print(f'O resultado é {r:.1f}.')
finally:
    print('Volte sempre! Muito obrigado!')
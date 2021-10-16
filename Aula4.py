# Condicionais
# if, elif e else

numero_de_atrasos = 2
if numero_de_atrasos >= 3:
    print('Você está suspenso')
elif numero_de_atrasos == 1:
    print('Pode entrar, porém, caso tome mais 2 faltas, irá ser suspenso')
elif numero_de_atrasos == 2:
    print('Pode entrar, porém, caso tome mais 1 falta, irá ser suspenso')
else:
    print('Pode entrar')

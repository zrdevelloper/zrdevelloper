# Hi, it's my first project, sorry is very simple project
# I am learning python, rate please

# By Caio
# I'm From Brazil! 😎


# Calculator Very Ultra Mega Simple !

# Iremos Guardar O Primeiro Numero Na Memoria.
# We will save the first number in memory.
num1 = float(input("Insira o numero que deseja: "))

# Aqui Vamos Guardar O Segundo Numero.
# Here we'll save the second number.
num2 = float(input("insira seu subnumero: "))

# Agora Selecione A Operação.
# Now Select Operation.
operacao = input("Selecione Uma Operação (+, -, *, /, **, % ): ")


if operacao == "+":
    resultado = num1 + num2
    print ("Resultado: ", resultado)
    
elif operacao == "-":
    resultado = num1 - num2
    print ("Resultado: ", resultado)
    
elif operacao == "*":
    resultado = num1 * num2
    print ("Resultado: ", resultado)
    
elif operacao == "/":
    resultado = num1 / num2
    print ("Resultado: ", resultado)

elif operacao == "**":
    resultado = num1 ** num2
    print ("Resultado: ", resultado)
    
elif operacao == "%":
    resultado = num1 % num2
    print ("Resultado: ", resultado)
    
else: 
    print ("Operação Invalida! ")


# Obrigado Por Testar! 
# Se Encontrar Um Erro, Avisar-me  é Claro Se Quiser Pode Arrumar, Muito Obrigado ! 😎
    
# Thanks For Trying! 
#If you find an error, let me know, of course, if you want to fix it, thank you very much! 😎


# Crie uma variável chamada base_price para armazenar o preço base do ingresso do filme e defina seu valor como 15. 
# Crie outra variável chamada age para armazenar a idade do usuário e defina seu valor como 21.

base_price = 15
age = 21

# Crie uma variável chamada seat_type para armazenar o tipo de assento que o usuário selecionou e defina seu valor para a string Gold. 
# Crie outra variável chamada show_time para armazenar o horário do filme e defina seu valor para a string Evening.

seat_type = "Gold"
show_time = "Evening"

# Crie uma declaração if para verificar se age é maior que 17. 
# Dentro do corpo da declaração if, imprima User is eligible to book a ticket. 
# Isso imprimirá a mensagem somente quando a idade do usuário for maior que 17.
# Lembre-se de indentar o corpo da instrução if e cercar a mensagem com aspas simples ou duplas dentro da chamada print().

if age > 17:
    print("User is elegible to book a ticket.")
'''else:
    print("User isn\'t elegible to book a ticket.")'''

# Crie uma declaração if para verificar se age é maior ou igual a 21. 
# Dentro do corpo da declaração if, imprima User is eligible for Evening shows.

if age >= 21:
    print("User is eligible for Evening shows.")
#else:
#    print("User ins\'t eligible for Evening shows.")

# Agora, adicione uma cláusula else à sua declaração if e imprima User is not eligible for Evening shows dentro do corpo do else. 
# Isso será impresso somente quando a condição na declaração if for falsa.

else:
    print('User is not eligible for Evening shows')

# Crie uma variável chamada is_member para indicar se o usuário é um membro e defina seu valor como True.
# Abaixo da variável is_member crie outra variável chamada is_weekend para indicar se a exibição do filme é no fim de semana e defina seu valor como False. 

''' is_member = True '''
is_member = False
is_weekend = False

# Crie uma variável chamada discount e defina seu valor como 0. 
# Isso armazenará o desconto que o usuário recebe no ingresso do filme.

discount = 0

# Crie uma declaração if para verificar se is_member é verdadeiro. 
# Dentro do corpo da declaração if, atualize o valor de discount para 3 e imprima User qualifies for membership discount no terminal.

#if is_member is True:
#    discount = 3
#    print("User qualifies for membership discount no terminal.")

'''if is_member:
    discount = 3
    print("User qualifies for membership discount")'''

# Adicione uma cláusula else à sua declaração if e imprima User does not qualify for membership discount dentro do corpo do else.
# Você também quer exibir o valor atualizado de discount. 
# Abaixo da declaração if...else, use a chamada print() para exibir uma mensagem que mostre Discount: seguido do valor atualizado de discount. 
# Depois, verifique a saída no terminal.

#else:
#    print("User does not qualify for membership discount")

#print("Discount: " + (str(discount)))

'''else:
    print("User does not qualify for membership discount")

print('Discount:', discount)'''

# O desconto de associação deve ser aplicado apenas aos membros se a age for maior ou igual a 21.
# Use o operador and para combinar a condição existente da sua declaração if com outra condição que verifica se age é maior ou igual a 21.

if is_member and age >= 21:
    discount = 3
    print('User qualifies for membership discount')
else:
    print('User does not qualify for membership discount')
print('Discount:', discount)

# Agora altere o valor da variável is_member para False pois o usuário não é um membro.
# Depois disso, você verá que o valor de discount agora permanece 0, porque ambas as condições devem ser satisfeitas para que o desconto seja aplicado.

# Agora crie uma variável chamada extra_charges e defina-a como 0. 
# Isso representará cobranças extras a serem aplicadas ao ingresso do filme nos finais de semana.
# Então, crie uma declaração if para verificar se is_weekend é verdadeiro. 
# Dentro do corpo da declaração if, atualize o valor de extra_charges para 2 e imprima Extra charges will be applied no terminal.

extra_charges = 0

''' if is_weekend is True: '''
#if is_weekend:
#    extra_charges = 2
#    print("Extra charges will be applied")

# Agora, adicione uma cláusula else à sua declaração if e imprima No extra charges will be applied dentro do corpo do else. 
# Isso imprimirá a mensagem somente quando a condição de cobranças extras for falsa.
# Então, abaixo da cláusula else, use a chamada print() para exibir uma mensagem que mostra Extra charges: seguida do valor atualizado de extra_charges e verifique a saída no terminal.

''' if is_weekend:
    extra_charges = 2
    print('Extra charges will be applied')
else:
    print("No extra charges will be applied")

print('Extra charges:', extra_charges) '''

# Cobranças extras também devem ser aplicadas se o show for à noite. 
# Use o operador or para combinar a condição existente da sua declaração if com uma segunda condição que verifica se show_time é igual à string Evening.

if is_weekend or show_time == "Evening":
    extra_charges = 2
    print('Extra charges will be applied')
else:
    print('No extra charges will be applied')
print('Extra charges:', extra_charges)

# Agora você verificará se o usuário satisfaz as condições para reservar um ingresso de cinema. 
# Usuários com idade 21 ou acima podem sempre reservar ingressos sem quaisquer restrições.
# Crie uma declaração if para verificar se age é maior ou igual a 21. 
# Dentro do corpo da declaração if, imprima Ticket booking condition satisfied no terminal.
# Então, adicione uma cláusula else à sua declaração if e imprima Ticket booking failed due to restrictions dentro do corpo do else.

''' if age >= 21: print("Ticket booking condition satisfied") 
else: print("Ticket booking failed due to restrictions") '''

#if age >= 21:
#    print('Ticket booking condition satisfied')
#else:
#    print('Ticket booking failed due to restrictions')

# Usuários entre 18 e 21 podem reservar ingressos, mas somente quando o show_time não for Evening.
# Use o operador and para construir uma expressão que verifica se age é maior ou igual a 18 e show_time não é Evening. 
# Use o operador or para combiná-lo com a condição existente da última instrução if. Não crie novas variáveis.

''' if age >= 21:
    print('Ticket booking condition satisfied')
elif age >= 18 and show_time == False:
    print('Ticket booking condition satisfied')
else:
    print('Ticket booking failed due to restrictions') '''

#if age >= 21 or age >= 18 and show_time != 'Evening':
#    print('Ticket booking condition satisfied')
#else:
#    print('Ticket booking failed due to restrictions')


# Há mais uma exceção às regras de reserva. 
# Usuários entre 18 e 21 podem reservar shows noturnos se forem membros.
# Agora, adicione outra condição à sua declaração if existente usando o operador or para verificar se is_member é verdadeiro.
''' if condition1 and (condition2 or condition3):
    # Code to execute if conditions evaluate to True
else:
    # Code to execute if conditions evaluate to False '''
# Use os parênteses () para agrupar as condições show_time != 'Evening' e is_member juntas conforme mostrado no exemplo acima.

''' if age >= 21 or age >= 18 and (show_time != 'Evening' or is_member):
    print('Ticket booking condition satisfied')
else:
    print('Ticket booking failed due to restrictions') '''


# Agora você calculará as taxas de serviço com base no tipo de assento que o usuário selecionou.
# Ainda dentro do corpo do seu último if, crie uma variável chamada service_charges e defina-a como 0.
# Então, crie uma declaração if aninhada para verificar se seat_type é igual a Premium. 
# Dentro do corpo da declaração if, atualize o valor de service_charges para 5.

''' if age >= 21 or age >= 18 and (show_time != 'Evening' or is_member):
    print('Ticket booking condition satisfied')

    service_charges = 0

    if seat_type == "Premium":
        service_charges = 5
    else:
        service_charges = 1

else:
    print('Ticket booking failed due to restrictions') '''

# Adicione uma declaração elif à sua declaração if...else e verifique se seat_type é igual a Gold. 
# Dentro do corpo da declaração elif, atualize o valor de service_charges para 3.
# Abaixo da declaração if...elif..else, use a chamada print() para exibir uma mensagem que mostra Service charges: seguida do valor atualizado de service_charges. 
# Então, verifique a saída no terminal.

''' if age >= 21 or age >= 18 and (show_time != 'Evening' or is_member):
    print('Ticket booking condition satisfied')

    service_charges = 0
    if seat_type == 'Premium':
        service_charges = 5
    
    elif seat_type == "Gold":
        service_charges = 3

    else:
        service_charges = 1
    
    print('Service charges:', service_charges)

else:
    print('Ticket booking failed due to restrictions') '''

# Nesta etapa final, você calculará o preço final do ingresso do filme usando os valores calculados nas etapas anteriores.
# O preço final do ingresso é calculado somando as cobranças extras e as taxas de serviço ao preço base e depois subtraindo o desconto.
# No final do corpo do seu último if, calcule o preço final do ingresso e armazene-o em uma variável chamada final_price.
# Finalmente, imprima uma mensagem que mostre Final price of ticket: seguido do valor de final_price.

if age >= 21 or age >= 18 and (show_time != 'Evening' or is_member):
    print('Ticket booking condition satisfied')

    service_charges = 0
    if seat_type == 'Premium':
        service_charges = 5
    elif seat_type == 'Gold':
        service_charges = 3
    else:
        service_charges = 1
    print('Service charges:', service_charges)

    final_price = base_price + extra_charges + service_charges - discount
    
    print('Final price of ticket:', final_price)

else:
    print('Ticket booking failed due to restrictions')
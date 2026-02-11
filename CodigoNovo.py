# base_price = 15
base_price = input("Digite o valor base do ticket: ")

# age = 21
age = input("Digite a idade do cliente: ")

seat_type = 'Gold'
show_time = 'Evening'

if int(age) > 17:
    print('User is eligible to book a ticket')

if int(age) >= 21:
    print('User is eligible for Evening shows')
else:
    print('User isn\'t eligible for Evening shows')

is_member = False
is_weekend = False

discount = 0
if is_member and int(age) >= 21:
    discount = 3
    print('User qualifies for membership discount')
else:
    print('User does not qualify for membership discount')
print('Discount:', discount)


extra_charges = 0
if is_weekend or show_time == 'Evening':
    extra_charges = 2
    print('Extra charges will be applied')
else:
    print('No extra charges will be applied')
print('Extra charges:', extra_charges)

if int(age) >= 21 or int(age) >= 18 and (show_time != 'Evening' or is_member):
    print('Ticket booking condition satisfied')

    service_charges = 0
    if seat_type == 'Premium':
        service_charges = 5
    elif seat_type == 'Gold':
        service_charges = 3
    else:
        service_charges = 1
    print('Service charges:', service_charges)

    final_price = int(base_price) + extra_charges + service_charges - discount
    
    print('Final price of ticket:', final_price)

else:
    print('Ticket booking failed due to restrictions')
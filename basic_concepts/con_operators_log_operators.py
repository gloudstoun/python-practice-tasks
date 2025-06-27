age = int(input("Введите свой возраст: "))
has_ticket_str = input("У вас есть билет? (да/нет): ")

if has_ticket_str.lower() == 'да':
    has_ticket = True
else:
    has_ticket = False

if age >= 18 and has_ticket:
    print("Добро пожаловать в клуб!")
elif age < 18:
    print("Вы слишком молоды для входа.")
else:
    print("У вас нет билета.")



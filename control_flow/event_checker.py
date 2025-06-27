def can_enter_event(age, has_ticket, has_invitation):



    '''
    age (целое число) - возраст человека.

    has_ticket (булево значение True/False) - наличие билета.

    has_invitation (булево значение True/False) - наличие специального приглашения.

    '''

    if (age >= 18 and has_ticket) or (age < 18 and has_invitation):
        return True
    else:
        return False

print("--- Проверка входа на мероприятие ---")
print(f"Возраст 20, билет True, приглашение False: {can_enter_event(20, True, False)}")
print(f"Возраст 17, билет True, приглашение False: {can_enter_event(17, True, False)}")
print(f"Возраст 16, билет False, приглашение True: {can_enter_event(16, False, True)}")
print(f"Возраст 25, билет False, приглашение False: {can_enter_event(25, False, False)}")
print(f"Возраст 18, билет True, приглашение True: {can_enter_event(18, True, True)}")
print(f"Возраст 10, билет False, приглашение False: {can_enter_event(10, False, False)}")
print(f"Возраст 30, билет False, приглашение True: {can_enter_event(30, False, True)}")
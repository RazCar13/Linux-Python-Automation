def ro_cnp_interpreter(id_number):

    # Valideaza lungimea
    if len(id_number) != 13:
        return {'error': 'Lungime invalida'}

    # Valideaza format
    if not id_number.isdigit():
        return {'error': 'CNP invalid, doar caractere numerice'}

    # Extrage info
    gen_digit = int(id_number[0])
    year_digit = int(id_number[1:3])
    month_digit = int(id_number[3:5])
    day_digit = int(id_number[5:7])
    county_code = int(id_number[7:9])
    order_number = int(id_number[9:12])
    control_digit = int(id_number[12])

    # Determina gen
    gen = 'Barbat' if gender_digit % 2 == 1 else 'Femeie'

    return {
        'gen': gen,
        'birth_date': f'{year_digit + 1900}-{month_digit:02d}-{day_digit:02d}',
        'county_code': county_code,
        'order_number': order_number,
        'control_digit': control_digit
    }


def ro_id_validator(func):
    
    #Decorator 
  
    def wrapper(id_number):
        # Valideza lungime
        if len(id_number) != 13:
            return {'error': 'Invalid ID number length'}

        # Valideaza format
        if not id_number.isdigit():
            return {'error': 'Invalid ID number format (numeric characters only)'}

        # Apeleaza functie
        return func(id_number)

    return wrapper


# Aplica decorator pe functie
@ro_id_validator
def decorated_ro_cnp_interpreter(id_number):

    # Extrage info
    gen_digit = int(id_number[0])
    year_digit = int(id_number[1:3])
    month_digit = int(id_number[3:5])
    day_digit = int(id_number[5:7])
    county_code = int(id_number[7:9])
    order_number = int(id_number[9:12])
    control_digit = int(id_number[12]) % 2

    # Determina gen
    gen = 'Barbat' if gen_digit % 2 == 1 else 'Femeie'

    return {
        'gen': gen,
        'data_nasterii': f'{year_digit + 1900}-{month_digit:02d}-{day_digit:02d}',
        'codul_tarii': county_code,
        'numar_ordine': order_number,
        'cifra_verificare': control_digit
    }

# Introdu CNP:
id_number = "1970103324786"
result = decorated_ro_cnp_interpreter(id_number)
print(result)

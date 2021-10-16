import re


def process_message(message, response_array, response):
    # Dividir los caracteres especiales
    list_message = re.findall(r"[\w']+|[.,!?;]", message.lower())

    # Score de el numero de palabras
    score = 0
    for word in list_message:
        if word in response_array:
            score = score + 1

    # Regresa el score y las palabras
    return [score, response]


def get_response(message):
    # Nuestras respuestas (base de conocimiento)
    response_list = [
        process_message(message, ['ola', 'hola', 'que tal la vida'], 'Kuchau'),
        process_message(message, ['adiós', 'hasta', 'luego'], 'Adios :D!'),
        process_message(message, ['como', 'estas'], 'Hago lo que puedo'),
        process_message(message, ['tu', 'nombre'], 'Yo soy la Sinapsis de los Avocados!'),
        process_message(message, ['ayuda'], 'Veamos que podemos hacer...')

    ]

    # Comprueba la mejor respuesta
    response_scores = []
    for response in response_list:
        response_scores.append(response[0])

    # Get the max value for the best response and store it into a variable
    winning_response = max(response_scores)
    matching_response = response_list[response_scores.index(winning_response)]

    # Return the matching response to the user
    if winning_response == 0:
        bot_response = 'Sip, no se que escribiste, pero digamos que vuelvelo a intentar'
    else:
        bot_response = matching_response[1]

    print('Respuesta:', bot_response)
    return bot_response

# Test your system
# get_response('What is your name bruv?')
# get_response('Can you help me with something please?')
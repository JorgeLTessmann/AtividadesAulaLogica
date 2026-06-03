def input_idade(msg, mini, maxi):
    while  True:
        try:
            idade = int(input(msg))
            if mini <= idade <= maxi:
                break
            else:
                print(f"Entrada fora di intervalo [{mini}, {maxi}]")
        except Exception as e:
            print("Idade deve ser apenas um numero inteiro!")
            print(f"Erro: {e}")
    return idade

def input_float(msg):

    while True:
        try:
            valor = float(input(msg))
            break
        except Exception as e:
            print("Altura deve ser um numero decimal!")
            print(f"Error {e}")
    return valor

def input_int(msg):
    while True:
        try:
            valor = int(input(msg))
            break
        except Exception as e:
            print("Idade deve ser apenas um numero inteiro!")
            print(f"Erro: {e}")
    return valor

def input_nome(msg):
    while True:
        nome = input(msg).strip()
        for letra in nome:
            if letra == " ":
                dois_nomes = True
        if dois_nomes:
            break
        else:
            print("Precisa de, no minimo, dois nomes")
        return nome

import random
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_symbols=True):
    characters = string.ascii_lowercase  # Começamos com letras minúsculas
    if use_uppercase:
        characters += string.ascii_uppercase  # Adiciona letras maiúsculas se permitido
    if use_digits:
        characters += string.digits  # Adiciona números se permitido
    if use_symbols:
        characters += string.punctuation  # Adiciona símbolos se permitido

    # Agora, criamos a senha escolhendo caracteres aleatórios
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    print("Bem-vindo ao Gerador de Senhas!")

    length = int(input("Digite o comprimento desejado para a senha: "))
    use_uppercase = input("Incluir letras maiúsculas? (s/n): ").lower() == 's'
    use_digits = input("Incluir números? (s/n): ").lower() == 's'
    use_symbols = input("Incluir símbolos? (s/n): ").lower() == 's'

    password = generate_password(length, use_uppercase, use_digits, use_symbols)
    print(f"Sua senha gerada é: {password}")


    def check_password_strength(password):
        length_criteria = len(password) >= 8
        uppercase_criteria = any(char.isupper() for char in password)
        lowercase_criteria = any(char.islower() for char in password)
        digit_criteria = any(char.isdigit() for char in password)
        symbol_criteria = any(char in string.punctuation for char in password)

        if all([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, symbol_criteria]):
            return "Forte"
        elif all([length_criteria, lowercase_criteria, digit_criteria]):
            return "Média"
        else:
            return "Fraca"


    # No final do script, adicione:
    strength = check_password_strength(password)
    print(f"A força da sua senha é: {strength}")

def save_password(password):
    with open("senhas.txt", "a") as file:
        file.write(password + "\n")
    print("Senha salva em senhas.txt")

# Pergunte ao usuário se deseja salvar a senha:
save = input("Deseja salvar essa senha? (s/n): ").lower() == 's'
if save:
    save_password(password)

def generate_passphrase(words=4):
    with open("palavras_comuns.txt", "r") as file:
        word_list = file.read().splitlines()
    passphrase = '-'.join(random.choice(word_list) for _ in range(words))
    return passphrase

# Adicionar opção ao menu
use_passphrase = input("Deseja gerar uma senha baseada em frase? (s/n): ").lower() == 's'
if use_passphrase:
    password = generate_passphrase()
else:
    password = generate_password(length, use_uppercase, use_digits, use_symbols)

import pyperclip

# No final do script, após gerar a senha:
pyperclip.copy(password)
print("A senha foi copiada para a área de transferência!")



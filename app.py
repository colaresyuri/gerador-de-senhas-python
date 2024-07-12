
import random
import string

def gerar_senha_simples(tamanho):
    # Caracteres permitidos: letras maiúsculas, minúsculas e dígitos
    caracteres = string.ascii_letters + string.digits

    # Gera a senha escolhendo caracteres aleatórios da lista de caracteres
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

    # Função da main
def main():
    while True:
        tamanho = int(input("Digite a quantidade desejada de caracteres para a senha: "))
        senha = gerar_senha_simples(tamanho)
        print(f"Sua senha gerada é: {senha}")
        
        # Pergunta ao usuário se deseja gerar uma nova senha
        nova_senha = input("Você deseja gerar uma nova senha? (sim(s)/não(n)): ").strip().lower()
        
        # Verifica se o usuário quer gerar uma nova senha
        if nova_senha == 'sim' or nova_senha == 's':
            continue  # Volta ao início do loop para gerar outra senha
        
        # Verifica se o usuário quer encerrar o programa
        elif nova_senha == 'não' or nova_senha == 'n':
            break  # Encerra o loop e o programa
        
        else:
            print("Resposta inválida. Por favor, responda com 'sim(s)' ou 'não(n)'.")

if __name__ == "__main__":
    main()


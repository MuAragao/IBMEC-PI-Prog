import csv  # Importar o módulo csv é necessário para ler e escrever em arquivos CSV

# Função para imprimir menu
def imprimir_menu():
    print("Menu:")
    print("1. Parte do nome do cliente")
    print("2. Número do caso e informações detalhadas")
    print("3. Despesa total")
    print("4. Receita total")
    print("5. Caso com maior despesa")
    print("6. Caso com maior receita")
    print("7. Salvar dados do cliente em arquivo")
    print("8. Sair")
    return int(input("Digite o número da opção desejada: "))

# Função para solicitar parte do nome do cliente e imprimir nomes correspondentes
def parte_nome_cliente(parte_nome):
    with open('registro.csv', mode='r', newline='') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=';')  # Adicione o delimitador aqui
        print(next(csvreader).keys())  # Imprime as chaves do dicionário
        for row in csvreader:
            if parte_nome.lower() in row['Cliente'].lower():
                print(f"Cliente: {row['Cliente']}")

# Função para solicitar número do caso e imprimir informações
def numero_caso(numero):
    with open('registro.csv', mode='r', newline='') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=';')  # E aqui
        print(next(csvreader).keys())  # Imprime as chaves do dicionário
        for row in csvreader:
            if numero == int(row['Caso']):
                print(f"Nome do cliente: {row['Cliente']}")
                print(f"Despesa: {row['Despesa']}")
                print(f"Receita: {row['Receita']}")
                print(f"Diferença: {float(row['Receita']) - float(row['Despesa'])}")

# Funções para calcular totais e imprimir
def calcular_totais():
    with open('registro.csv', mode='r', newline='') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=';')
        despesa_total = 0
        receita_total = 0
        for row in csvreader:
            try:
                despesa_total += float(row['Despesa'])
                receita_total += float(row['Receita'])
            except KeyError:
                print(f"KeyError ocorreu na linha: {row}")
        print(f"Despesa total: {despesa_total}")
        print(f"Receita total: {receita_total}")

# Funções para encontrar o caso com maior despesa e receita
def maior_despesa():
    with open('registro.csv', mode='r', newline='') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=';')  # E aqui
        print(next(csvreader).keys())  # Imprime as chaves do dicionário
        maior_despesa = 0
        nome_cliente = ''  # Inicializar a variável nome_cliente
        for row in csvreader:
            if float(row['Despesa']) > maior_despesa:
                maior_despesa = float(row['Despesa'])
                nome_cliente = row['Cliente']
        print(f"Nome do cliente com maior despesa: {nome_cliente}")
        print(f"Despesa: {maior_despesa}")

def maior_receita():
    with open('registro.csv', mode='r', newline='') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=';')  # E aqui
        print(next(csvreader).keys())  # Imprime as chaves do dicionário
        maior_receita = 0
        nome_cliente = ''  # Inicializar a variável nome_cliente
        for row in csvreader:
            if float(row['Receita']) > maior_receita:
                maior_receita = float(row['Receita'])
                nome_cliente = row['Cliente']
        print(f"Nome do cliente com maior receita: {nome_cliente}")
        print(f"Receita: {maior_receita}")

# Função para salvar dados do cliente em arquivo
def salvar_dados_cliente(nome_cliente):
    with open('registro.csv', mode='r', newline='') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=';')  # E aqui
        print(next(csvreader).keys())  # Imprime as chaves do dicionário
        with open(f'{nome_cliente}_casos.csv', mode='w', newline='') as outfile:
            fieldnames = ['Cliente', 'Caso', 'Despesa', 'Receita']
            csvwriter = csv.DictWriter(outfile, fieldnames=fieldnames)
            csvwriter.writeheader()
            for row in csvreader:
                if nome_cliente.lower() == row['Cliente'].lower():
                    csvwriter.writerow(row)

# Função principal que usa o menu para chamar as outras funções
def main():
    menu_escolhido = imprimir_menu()
    while menu_escolhido != 8:
        if menu_escolhido == 1:
            parte_nome_cliente(input("Digite parte do nome do cliente: "))
        elif menu_escolhido == 2:
            numero_caso(int(input("Digite número do caso: ")))
        elif menu_escolhido == 3 or menu_escolhido == 4:
            calcular_totais()
        elif menu_escolhido == 5:
            maior_despesa()
        elif menu_escolhido == 6:
            maior_receita()
        elif menu_escolhido == 7:
            salvar_dados_cliente(input("Digite nome completo do cliente para salvar: "))
        menu_escolhido = imprimir_menu()

# Chamando a função principal
if __name__ == "__main__":
    main()
    

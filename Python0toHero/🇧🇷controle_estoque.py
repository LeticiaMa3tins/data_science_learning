# Escolha : Dicionário de Dicionários.
# Usar o nome do produto como chave principal permite buscas e atualizações rápidas. 
# O dicionário interno para cada produto facilita o armazenamento de múltiplas informações.

estoque = {
    "teclado": {
        "quantidade": 25,
        "preco": 349.90
    },
    "smartphone": {
        "quantidade": 50,
        "preco": 120.00
    },
    "monitor": {
        "quantidade": 10,
        "preco": 1550.00
    }
}
while True:
    print("--- Menu ---")
    print("1 - Visualizar Estoque Atual")
    print("2 - Registrar Entrada de Produto")
    print("3 - Registrar Saída de Produto")
    print("4 - Sair")
    
    opcao = input("Selecione uma opção (1-4): ")



 

# A estrutura de controle de fluxo (if/elif).

    if opcao == '1':
        print("--- Relatório de Estoque Atual ---")
        # O .items(), é um método nativo do python que permite pegar a chave (nome) e o valor (dicionário interno) ao mesmo tempo, colocando os valores 
        #automaticamente nas variáveis nome_produto e detalhes, respectivamente.MUITO MAIS FÁCIL QUE C#.
        for nome_produto, detalhes in estoque.items():
            print(f"Produto: {nome_produto} | Qtd: {detalhes['quantidade']} | Preço: R$ {detalhes['preco']:.2f}")
#Aqui o produto_busca recebe o nome do produto que o usuário deseja registrar a entrada.
# O programa verifica se o produto existe no estoque usando a chave do dicionário.





    elif opcao == '2':
        print("--- Registrar Entrada de Produto ---")
        produto_busca = input("Digite o nome do produto: ")

        # Verificação de existência
        if produto_busca in estoque:
            quantidade_entrada = int(input("Digite a quantidade que está entrando: "))
            estoque[produto_busca]['quantidade'] += quantidade_entrada
            print(f"Sucesso! O produto '{produto_busca}' agora tem {estoque[produto_busca]['quantidade']} unidades.")
        else:
            print("Erro: Produto não encontrado.")




            
    elif opcao == '3':
            print("--- Registrar Saída de Produto ---")
            produto_busca = input("Digite o nome do produto: ")
            
            # Validação 1: O produto existe na base de dados?
            if produto_busca in estoque:
                quantidade_saida = int(input("Digite a quantidade de saída: "))
                
                # Validação 2: A matemática do estoque suporta a transação?
                if estoque[produto_busca]['quantidade'] >= quantidade_saida:
                    # Executa a dedução ( -= é a mesma coisa que x = x - y )
                    estoque[produto_busca]['quantidade'] -= quantidade_saida
                    print(f"Sucesso! Saída de {quantidade_saida} unidades de '{produto_busca}' registrada.")
                    print(f"Estoque restante: {estoque[produto_busca]['quantidade']}")
                else:
                    # Falha na Validação 2
                    print(f"Erro: Estoque insuficiente. Temos apenas {estoque[produto_busca]['quantidade']} unidades.")
            else:
                # Falha na Validação 1
                print("Erro: Produto não encontrado.")    






    elif opcao == '4':
            print("Encerrando o sistema...")
            print("bye bye!!")
            break  # Interrompe o loop while True e finaliza o programa
            
    else:
            # O 'fallback' que captura qualquer entrada diferente de 1, 2, 3 ou 4
            print("[ERRO] Opção inválida! Por favor, escolha um número entre 1 e 4.")

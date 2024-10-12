def ler_csv(arquivo_csv): 
    dados_csv = []                                        # cria uma lista em branco
    try:                                                  # tratamento de erro
        with open(arquivo_csv, newline='') as massa:      # com o arquivo --> informa o nome e o apelido massa
                                                          # newline seria o caracter de final de linha
            tabela = csv.reader(massa, delimiter=',')     # com os dados do arquivo, menos o cabeçalho
                                                          # informando que o separador é a virgula
            next(tabela)                                  # serve aqui para pular a linha de cabeçalho ( copiar e colar a mesma linha para pular as linhas que quer)
            for linha in tabela:                          # para cada linha na tabela
                dados_csv.append(linha)                   # guardando os dados separados para uso
        return dados_csv                                  # devolver os dados para serem usados no teste
    except FileNotFoundError:                             # tratatamento de erro arquivo n encontrado
        print(f'Arquivo não encontrado: {arquivo_csv}')   # mensagem de erro de arquivo n encontrado
    except Exception as fail:                             # qualquer erro n previsto
        print(f'Falha imprevista: {fail}')                # mensagem de erro q voltará do sistema

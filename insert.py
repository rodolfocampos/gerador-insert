from produto import Produto


def busca_produtos_no_arquivo():
    with open("produtos.txt") as arquivo:
        produtos = []
        for linha in arquivo:
            linha = linha.split("|")
            produto = Produto(linha[0], linha[1], linha[2], linha[3].strip())
            produtos.append(produto)
        arquivo.close()
    return produtos


def criar_insert_sql(lista_produtos, id_inicial):
    lista_script = []
    for produto in lista_produtos:
        sql = "INSERT INTO sw_publico.produto(id_produto, status_entidade, nome, codigo, preco, " \
              "id_grupo_produto, preco_pontos, pontos_ganhos, ind_site)\nVALUES ({}, 'A', '{}', {}, {}, 1, {}, {}, 'S');".format(
            id_inicial, produto.nome, id_inicial, produto.preco, produto.preco_pontos, produto.pontos_ganhos)
        id_inicial += 1
        lista_script.append(sql)
    return lista_script


def gravar_arquivo_sql(lista_script):
    with open("insert.sql", 'w') as arquivo_sql:
        for script in lista_script:
            arquivo_sql.write(script)
            arquivo_sql.write("\n")

        arquivo_sql.close()


lista_produtos = busca_produtos_no_arquivo()
# colocar o valor do id produto inicial para incrementar
lista_script = criar_insert_sql(lista_produtos, 10000)
gravar_arquivo_sql(lista_script)

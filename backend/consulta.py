def query(connection, query):
    cursor = connection.cursor()
    linhas = None
    try:
        cursor.execute(query)
        linhas = cursor.fetchall()
        teste = {}
        teste1 = {}
        for pos,linha in enumerate(linhas):
            for posicao,column in enumerate(cursor.description):
                teste1.update({column[0]:linha[posicao]})
            teste.update({pos:teste1})

        return teste
        # for posicao,linha in teste.items():
        #     print ('linha: '+str(posicao))
        #     print ('-------------------')
        #     for chave,valor in linha.items():
        #         print (str(chave)+':'+str(valor))
        #
        #     print (teste[0]['id'])
        #     print (teste[0]['nome'])
        #     print (teste[0]['sobrenome'])

    except Error as e:
        print("ocorreu um erro")

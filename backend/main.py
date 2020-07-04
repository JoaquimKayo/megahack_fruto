import conexao
import consulta
import json

def listar_tarefas(connection):
    select_users = "SELECT * from teste1"
    users = consulta.query(connection, select_users)
    print (users)
    return TAREFAS

if __name__ == "__main__":
    conexao = conexao.criar_conexao()
    
    #listar_tarefas(conexao)

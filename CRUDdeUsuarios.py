import MySQLdb

#Selecionar a db
host = "localhost"
user = "aplicacao"
password = "12345"
db = "escola_curso"
port = "3306"

#variável de conexão
con = MySQLdb.connect(host, user, password, db)
con.select_db(db)

#variável de cursor
c = con.cursor(MySQLdb.cursors.DictCursor)

#Função de seleção de aluno
def select(fields, tables, where=None):
	global c

	query = "SELECT " + fields + " FROM " + tables
	if (where):
		query = query + " WHERE " + where
	c.execute(query)
	return c.fetchall()

#   Exemplo de utilização da função
#     print(select("nome, cpf", "alunos", "id_aluno = 4"))

#Função de inserir aluno
def insert(values, table, fields=None):

    global c, con 

    query = "INSERT INTO " + table 
    if (fields):
        query = query + " (" + fields + ") "

    query = query + " VALUES " + ",".join(["(" + v + ")" for v in values])
    
    #Comandos para poder fazer a alteração dentro da tabela
    c.execute(query)
    con.commit()

# Para inserir dados deve-se declarar uma variável values com todos os elementos que se deve ser adcionado no aluno, e após isso utilizar:
#   print(insert(values, "alunos")) por exemplo.


#Função de atualizar dados do aluno
def update(sets, table, where=None):
    global c,con

    query = "UPDATE " + table
    query = query + " SET " + ",".join([field + " = '" + value + "'"  for field, value in sets.items()])

    if (where):
        query = query + " WHERE " + where

    #Comandos para poder fazer a alteração dentro da tabela
    c.execute(query)
    con.commit()
    
#   Exemplo de utilização da função
#     print(update({"nome":"thiago", "cidade":"curitiba"}, "alunos", "id_aluno = 1"))


#Função para deletar aluno
def delete(table, where):
    global c, con

    query = "DELETE FROM " + table + " WHERE " + where

    #Comandos para poder fazer a alteração dentro da tabela
    c.execute(query)
    con.commit()


    #Exemplo de utilização da função
#     print(delete("alunos", "id_aluno = 10"))

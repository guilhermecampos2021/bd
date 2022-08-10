"""
https://www.udemy.com/course/python-mysql/learn/lecture/12662988?start=240#questions
Código extraido das aulas ministrada pelo Prof. Pedro Magalhaes Martins com algumas adaptações
https://www.udemy.com/user/pedro-magalhaes-martins/

O Banco de Dados foi criado no MySQL Workbench
"""
"""
import mysql.connector
connection = mysql.connector.connect(host='localhost',
                                         database='escola_curso',
                                         user='root',
                                         password='1234')
c = connection.cursor( )
"""
import mysql.connector
connection = mysql.connector.connect(host='localhost',
                                         database='pessoal',
                                         user='root',
                                         password='1234')
c = connection.cursor( )




"""
##############################
Funcao SELECT
##############################
"""

def select(fields,tables, where = None):
    global c
    query = "SELECT " + fields + " FROM " + tables
    if(where):
        query = query +" WHERE " + where

    c.execute(query)
    return c.fetchall()

#result = select("idalunos,nome,cpf","alunos")
#print(result)

#result = select("idalunos,nome,cpf","alunos","idalunos = 2")
#print(result)

result = select("*","pessoa","id_pessoa=3")
print(result)

#print(len(result))
#print(type(result))
print("O nome escolhido foi " + result[0][1] + " que nasceu dia " + result[0][4] )

""""
##############################
Funcao INSERT
##############################
"""


def insert(values,table,fields = None):
    global c,connection
    query = "INSERT INTO " + table
    if (fields):
        query = query + " (" + fields + ") "
    query = query + " VALUES " + ",".join(["(" + v + ")" for v in values])
    print(query)
    c.execute(query)
    connection.commit()

"""
DADOS E FUNCAO INSERT

values =[
    "DEFAULT, 'Joao Pedro','12345678901'",
    "DEFAULT, 'Maria Pedro','12345678901'"]

insert(values,"alunos")
print(select("*","alunos"))

"""

"""
##############################
Funcao UPDATE
##############################
"""

def update(sets,table, where = None):
    global c, connection

    query = "UPDATE " + table
    query = query + " SET " + ",".join([field + " = '" + value + "'" for field,value in sets.items()])
    if (where):
        query = query + " WHERE " + where
    print(query)
    c.execute(query)
    connection.commit()


"""
Dados para UPDATE

#aluno3 = select("*", "alunos","idalunos=3")
#print(aluno3)
update({"nome":"João Martins"},"alunos","idalunos = 3")
aluno3 = select("*", "alunos","idalunos=3")
print(aluno3)
"""

"""
##############################
Funcao DELETE
##############################
"""

def delete(table, where):
    global connection ,c

    query = "DELETE FROM " + table + " WHERE " + where
    c.execute(query)
    connection.commit()


"""
Dados para DELETE

aluno4 = select("*", "alunos","idalunos=11")
print(aluno4)

print(delete("alunos","idalunos=11"))

aluno4 = select("*", "alunos","idalunos=11")
print(aluno4)

"""

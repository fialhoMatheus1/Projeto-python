import mysql.connector
from Conexao import Conexao

class Model:
    def __init__(self):
            self.db_connection = Conexao()  # Abrindo a conexao com o banco de dados
            self.db_connection = self.db_connection.conectar()  # Método que realizar a conexão com o BD
            self.con = self.db_connection.cursor()  # Navegação no banco de dados
    def inserir(self, nome, ingrediente, preparo, link):
        try:
            sql = "insert into catalogo(codigo, nome, igrediente, preparo, link) values('','{}','{}', '{}', '{}')".format(nome, ingrediente, preparo, link)
            self.con.execute(sql)
            self.db_connection.commit()#Insere o dado no banco de dados
            return "{} linha afetada".format(self.con.rowcount)
        except Exception as erro:
            return erro

    def selecionar(self):
        try:
            sql = "select * from catalogo"
            self.con.execute(sql)
            msg = ""
            for (codigo, nome, ingrediente, preparo, link) in self.con:
                msg = msg + "\n\nCódigo: {}, \nNome: {}, \nIngredientes: {}:, \nModo de Preparo: {}, \nLink em libras: {}".format(codigo, nome, ingrediente, preparo, link)
            return msg
        except Exception as erro:
            return erro

    def atualizar(self, campo, novoDado, cod):
        try:
            sql = "update catalogo set {} = '{}' where codigo = '{}'".format(campo, novoDado, cod)
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} linha(s) atualizada(s)!".format(self.con.rowcounts)
        except Exception as erro:
            return erro

    def excluir(self, cod):
        try:
            sql = "delete from catalogo where codigo = '{}'".format(cod)
            self.con.execute(sql)
            self.db_connection.commit()
            print("{} linha(s) afetada(s)!!".format(self.con.rowcount))
        except Exception as erro:
            return erro

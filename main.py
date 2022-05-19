import cherrypy
import mysql.connector
import pandas as pd
from datetime import date
import os

class cadastro(object):
    @cherrypy.expose
    def index(self):
        self.con = mysql.connector.connect(

        host="host",
        user="user",
        password="password",
        database="database",
        
        # database -> placas = GRN LOCAL USUARIO MOVIMENTACAO VEZES

        self.cursor = self.con.cursor()
        return open("index.html")

    @cherrypy.expose
    def SAIDA_F(self, *args,**kwargs):
        print("saida apertada")
        GRN_S = cherrypy.request.params.get('GRN_S')
        PESSOA_S = cherrypy.request.params.get('PESSOA_S')
        LINHA_S = cherrypy.request.params.get('LINHA_S')

        comando = f"SELECT * FROM placas WHERE GRN = '{GRN_S}'"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()

        if str(resultado) == "[]":

            return """
        <html>
        <head>
        <script lang="javascript">
        alert('!!!PLACA NÃO CADASTRADA!!!')
        window.location.href = "http://127.0.0.1:8080/"
        </script>
        </head>
        <body></body>
        </html>
        """
            


        else:

            comando = f"SELECT LOCAL FROM placas WHERE GRN = '{GRN_S}'"
            self.cursor.execute(comando)
            resultado = self.cursor.fetchall()

            if str(resultado) != "[('ESTOQUE',)]":
                return """
        <html>
        <head>
        <script lang="javascript">
        alert('!!!PLACA SEM ENTRADA!!!')
        window.location.href = "http://127.0.0.1:8080/"
        </script>
        </head>
        <body></body>
        </html>
        """

            data = date.today()

            if LINHA_S == "1" or LINHA_S == "2" or LINHA_S == "3" or LINHA_S == "4" or LINHA_S == "5":

                comando = f"SELECT VEZES FROM placas WHERE GRN = '{GRN_S}'"
                self.cursor.execute(comando)
                resultado = self.cursor.fetchall()
                new = int(str(resultado)[2]) + 1

                if new >= 10:
                    return """
        <html>
        <head>
        <script lang="javascript">
        alert('!!!CICLO DA PLACA COMPLETO!!!')
        window.location.href = "http://127.0.0.1:8080/"
        </script>
        </head>
        <body></body>
        </html>
        """

                comando = f"UPDATE placas SET VEZES = '{new}' WHERE GRN = '{GRN_S}'"
                self.cursor.execute(comando)
                self.con.commit()


                comando = f"UPDATE placas SET LOCAL = '{LINHA_S.upper()}' WHERE GRN = '{GRN_S}'"
                self.cursor.execute(comando)
                self.con.commit()

                comando = f"UPDATE placas SET USUARIO = '{PESSOA_S.upper()}' WHERE GRN = '{GRN_S}'"
                self.cursor.execute(comando)
                self.con.commit()

                comando = f"UPDATE placas SET MOVIMENTACAO = '{data}' WHERE GRN = '{GRN_S}'"
                self.cursor.execute(comando)
                self.con.commit()
                return """
        <html>
        <head>
        <script lang="javascript">
        alert('!!!SAIDA REALIZADA COM SUCESSO!!!')
        window.location.href = "http://127.0.0.1:8080/"
        </script>
        </head>
        <body></body>
        </html>
        """

            else:
                
                return """
        <html>
        <head>
        <script lang="javascript">
        alert('!!!LINHA INVALIDA!!!')
        window.location.href = "http://127.0.0.1:8080/"
        </script>
        </head>
        <body></body>
        </html>
        """



            return open("index.html")

    @cherrypy.expose
    def ENTRADA_F(self, *args,**kwargs):

        print("entrada apertada")
        GRN_E = cherrypy.request.params.get('GRN_E')
        print(GRN_E)
        comando = f"SELECT * FROM placas WHERE GRN = '{GRN_E}'"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        print(resultado)

        if str(resultado) == "[]":
            return """
        <html>
        <head>
        <script lang="javascript">
        alert('!!!PLACA NÃO CADASTRADA!!!')
        window.location.href = "http://127.0.0.1:8080/"
        </script>
        </head>
        <body></body>
        </html>
        """
        
        else:
            comando = f"SELECT LOCAL FROM placas WHERE GRN = '{GRN_E}'"
            self.cursor.execute(comando)
            resultado = self.cursor.fetchall()
            if str(resultado) == "[('ESTOQUE',)]":
               return """
        <html>
        <head>
        <script lang="javascript">
        alert('!!!PLACA JÁ POSSUI ENTRADA!!!')
        window.location.href = "http://127.0.0.1:8080/"
        </script>
        </head>
        <body></body>
        </html>
        """

            comando = f"UPDATE placas SET LOCAL = 'ESTOQUE' WHERE GRN = '{GRN_E}'"
            self.cursor.execute(comando)
            self.con.commit()

            return """
        <html>
        <head>
        <script lang="javascript">
        alert('!!!ENTRADA REALIZADA COM SUCESSO!!!')
        window.location.href = "http://127.0.0.1:8080/"
        </script>
        </head>
        <body></body>
        </html>
        """

    @cherrypy.expose
    def CADASTRO_F(self, *args,**kwargs):
        print("cadastro apertado")
        GRN_C = cherrypy.request.params.get('GRN_C')
        print(GRN_C)

        if not GRN_C.startswith("PLACATESTE") or len(GRN_C) != 12:
            return """
            <html>
            <head>
            <script lang="javascript">
            alert('!!!GRN INVALIDO!!!')
            window.location.href = "http://127.0.0.1:8080/"
            </script>
            </head>
            <body></body>
            </html>
            """    

        comando = f'SELECT * FROM placas WHERE GRN="{GRN_C}"'
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        data = date.today()
        if str(resultado) == "[]":
            comando = f"INSERT INTO placas (GRN, LOCAL, USUARIO, MOVIMENTACAO, VEZES) VALUES ('{GRN_C}', 'ESTOQUE', 'ESTOQUE', '{data}', '0')"
            self.cursor.execute(comando)
            self.con.commit()
            print("CADASTRO REALIZADO COM SUCESSO!")
        else:
            print("!!!PLACA JÁ CADASTRADA!!!")
            return """
            <html>
            <head>
            <script lang="javascript">
            alert('!!!PLACA JÁ CADASTRADA!!!')
            window.location.href = "http://127.0.0.1:8080/"
            </script>
            </head>
            <body></body>
            </html>
            """    
        return """
        <html>
        <head>
        <script lang="javascript">
        alert('!!!CADASTRADA COM SUCESSO!!!')
        window.location.href = "http://127.0.0.1:8080/"
        </script>
        </head>
        <body></body>
        </html>
        """  

    @cherrypy.expose
    def PLACAS_F(self):
        comando = f"SELECT * FROM placas"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        df = pd.DataFrame(resultado)
        print(df)
        df.to_excel("placas.xlsx")

        return cherrypy.lib.static.serve_file(os.path.abspath("placas.xlsx"), "application/x-download", "placas.xlsx")

cherrypy.config.update(
    {'server.socket_host': '0.0.0.0'} )   
cherrypy.quickstart(cadastro())

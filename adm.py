import mysql.connector
import pandas as pd

con = mysql.connector.connect(

        host="localhost",
        user="root",
        password="Leafy2022!",
        database="banco_teste",
        
        # banco_teste -> placas = GRN LOCAL USUARIO MOVIMENTACAO VEZES
)

cursor = con.cursor()

while True:

    comando = f"SELECT * FROM placas"
    cursor.execute(comando)
    df = pd.DataFrame(cursor.fetchall())
    print(df)
    print("----------------------------------------------------------")

    op = input("Deseja remover qual GRN? ")
    try:    
        comando = f"DELETE FROM placas WHERE GRN='{op}'"
        cursor.execute(comando)
        con.commit()
        print("REMOVIDO COM SUCESSO")

    except:
        print("Não foi possivel realizar a ação")

    print("----------------------------------------------------------")

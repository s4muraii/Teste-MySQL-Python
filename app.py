import mysql.connector

# Conectando ao banco de dados
conexao = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="quitanda"
)

if conexao.is_connected():
    print ("Conectado ao banco de dados")

# Criando um cursor
cursor = conexao.cursor()

# Selecionando os dados da tabela
cursor.execute("SELECT * FROM produtos")

# Inserindo dados na tabela
resultados = cursor.fetchall()

# Imprimindo os resultados
for linha in resultados:
    print(linha)

# Fechando o cursor
cursor.close()

# Fechando a conexão
conexao.close()
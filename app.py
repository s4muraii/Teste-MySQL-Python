import mysql.connector

# Conectando ao banco de dados
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="senha",
    database="nome_do_banco"
)

if conexao.is_connected():
    print("Conectado ao banco de dados")

# Criando um cursor
cursor = conexao.cursor()

# Selecionando os dados da tabela
cursor.execute("SELECT * FROM escolas")

# Inserindo dados na tabela
resultados = cursor.fetchall()

# Imprimindo os resultados
for linha in cursor:
    print(linha)

# Fechando o cursor
cursor.close()

# Fechando a conexão
conexao.close()
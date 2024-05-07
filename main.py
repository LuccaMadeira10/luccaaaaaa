
from Database import Database
from MatchDatabase import MatchDatabase

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://34.230.40.111:7687", "neo4j", "sale-nickel-prerequisite")
db.drop_all()

# Criando uma instância da classe JogoDatabase para interagir com o banco de dados
jogo_db = MatchDatabase(db)

# Criando alguns Playeres
jogo_db.create_Player("Lucca")
jogo_db.create_Player("Roger")
jogo_db.create_Player("Gab")

# Criando algumas Matchs e suas relações com os Playeres
jogo_db.create_Match("Partida 1", "Lucca")
jogo_db.create_Match("Partida 2", "Roger")
jogo_db.create_Match("Partida 3", "Gab")

# Atualizando o nome de um Player
jogo_db.update_Player("Gab", "Gabriel")

jogo_db.insert_Player_Match("Lucca", "Partida 2")
jogo_db.insert_Player_Match("Lucca", "Partida 3")
jogo_db.insert_Player_Match("Roger", "Partida 1")
jogo_db.insert_Player_Match("Gabriel", "Partida 1")

jogo_db.insert_Player_Match("Gabriel", "Partida 3")
jogo_db.insert_Player_Match("Roger", "Partida 2")
jogo_db.insert_Player_Match("Roger", "Partida 3")

jogo_db.set_winner("Partida 1", "Roger")

print("Winner of Partida 1:", jogo_db.get_winner("Partida 1"))

# Deletando um Player e uma Match
jogo_db.delete_Match("História")

# Imprimindo
print("Players:")
print(jogo_db.get_Player())
print("Matchs:")
print(jogo_db.get_Match())

# Fechando a conexão com o banco de dados
db.close()
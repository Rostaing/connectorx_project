# ---------------- POSTGRESQL --------------- #
import connectorx as cx
import os
from dotenv import load_dotenv
from urllib.parse import quote_plus # Importer pour gérer les caractères spéciaux

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Récupérer les variables d'environnement
db_user = os.getenv("DB_USER") # J'ai renommé pour éviter la confusion avec l'utilisateur système
db_password = os.getenv("DB_PASSWORD")
db_server = os.getenv("DB_SERVER")
db_port = os.getenv("DB_PORT")
db_database = os.getenv("DB_DATABASE")

# --- Vérification que toutes les variables ont bien été chargées ---
required_vars = [db_user, db_password, db_server, db_port, db_database]
if not all(required_vars):
    print("Erreur : Une ou plusieurs variables d'environnement sont manquantes.")
    print("Veuillez vérifier votre fichier .env et les noms des variables :")
    print("DB_USER, DB_PASSWORD, DB_SERVER, DB_PORT, DB_DATABASE")
    exit() # Arrête le script si une variable est manquante

# --- Construction de la chaîne de connexion (plus robuste) ---
# 'quote_plus' encode les caractères spéciaux dans le mot de passe
password_encoded = quote_plus(db_password)

conn_str = f"postgresql://{db_user}:{password_encoded}@{db_server}:{db_port}/{db_database}" # PostgreSQL

# Définir la requête SQL
query = "SELECT * FROM salaire"

try:
    # Utiliser un bloc try...except pour attraper les erreurs de connexion ou de requête
    print("Tentative de connexion à la base de données...")
    df = cx.read_sql(conn=conn_str, query=query)
    print("Connexion réussie et données récupérées !")
    print(df)

except Exception as e:
    print(f"Une erreur est survenue : {e}")


# ---------------- MYSQL --------------- #
# import connectorx as cx
# import os
# from dotenv import load_dotenv
# from urllib.parse import quote_plus # Importer pour gérer les caractères spéciaux

# # Charger les variables d'environnement depuis le fichier .env
# load_dotenv()

# # Récupérer les variables d'environnement
# db_user = os.getenv("DB_USER") # J'ai renommé pour éviter la confusion avec l'utilisateur système
# # db_password = os.getenv("DB_PASSWORD")
# db_server = os.getenv("DB_SERVER")
# db_port = os.getenv("DB_PORT")
# db_database = os.getenv("DB_DATABASE")

# conn_str = f"mysql://{db_user}:@{db_server}:{db_port}/{db_database}" # MySQL

# # Définir la requête SQL
# query = "SELECT * FROM salaire_emp"

# try:
#     # Utiliser un bloc try...except pour attraper les erreurs de connexion ou de requête
#     print("Tentative de connexion à la base de données...")
#     df = cx.read_sql(conn=conn_str, query=query)
#     print("Connexion réussie et données récupérées !")
#     print(df)

# except Exception as e:
#     print(f"Une erreur est survenue : {e}")
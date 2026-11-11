import sqlite3
from pathlib import Path

# Descubra o diretório principal do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# Monte o caminho do banco de dados
DB_PATH = BASE_DIR / "toptech.db"


def conectar():
    conexao = sqlite3.connect(DB_PATH)
    return conexao
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente
load_dotenv()

def main():
    print("Script de execução determinístico rodando...")
    # Lógica de negócio (API, File system, etc) deve ocorrer aqui

if __name__ == "__main__":
    main()

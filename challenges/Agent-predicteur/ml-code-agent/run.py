from app.agent import CodeAgent
from app.executor import CodeExecutor

def main():
    filename = 'data/train.csv'
    target_column = 'Survived'

    agent = CodeAgent()
    executor = CodeExecutor()

    print("🧠 Génération du code par le LLM...")
    code = agent.generate_code(filename, target_column)

    print("\n----- CODE GÉNÉRÉ -----\n")
    print(code)
    print("\n----- FIN DU CODE -----\n")

    print("💻 Exécution du code généré...")
    try:
        output = executor.execute_code(code)
        print("=== Résultat de l'exécution ===")
        print(output)
    except Exception as e:
        print("Erreur lors de l'exécution du code :")
        print(e)

if __name__ == "__main__":
    main()

from app.agent import CodeAgent
from app.executor import CodeExecutor

def main():
    filename = 'data/train.csv'
    target_column = 'Survived'

    agent = CodeAgent()
    executor = CodeExecutor()

    print("🧠 Génération du code par le LLM...")
    code = agent.generate_code(filename, target_column)
    print("💻 Exécution du code généré...")
    output = executor.execute_code(code)
    print("=== Résultat de l'exécution ===")
    print(output)

if __name__ == "__main__":
    main()

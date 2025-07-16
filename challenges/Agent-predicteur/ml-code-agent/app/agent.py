import subprocess
import re

class CodeAgent:
    def __init__(self):
        pass

    def extract_code(self, text: str) -> str:
        """
        Extrait le code Python d'une réponse contenant des blocs de code Markdown.
        """
        code_blocks = re.findall(r"```(?:python)?\n(.*?)```", text, re.DOTALL)
        if code_blocks:
            return code_blocks[0].strip()
        else:
            return text.strip()

    def generate_code(self, filename: str, target_column: str) -> str:
        prompt = f"""
Tu es un assistant Python expert en Machine Learning et en manipulation de données avec Pandas et Scikit-learn.

Écris un script Python complet et exécutable, sans aucune explication ni texte supplémentaire, qui :

- charge le fichier CSV '{filename}' en utilisant `pandas.read_csv`.
- effectue un nettoyage des données de manière **robuste et conforme aux bonnes pratiques de Pandas** :
    * Pour les colonnes numériques **'Age', 'Fare', 'Pclass', 'SibSp', 'Parch'**, remplace les valeurs manquantes par la médiane de la colonne. **Utilise la syntaxe `.loc`** pour une affectation sécurisée et éviter les avertissements `SettingWithCopyWarning`.
    * Encode la colonne **'Sex'** : remplace 'female' par 0 et 'male' par 1. Gère les valeurs manquantes s'il y en a en les remplaçant par une valeur par défaut (par exemple, le mode).
    * Encode la colonne **'Embarked'** : utilise `sklearn.preprocessing.LabelEncoder` pour la transformer en valeurs numériques (0, 1, 2...). Gère les valeurs manquantes s'il y en a en les remplaçant par le mode avant l'encodage.
    * Supprime les colonnes de texte non utiles telles que 'Name', 'Ticket', 'Cabin'.
- S'assure que toutes les colonnes utilisées comme features sont bien numériques après le nettoyage et l'encodage.
- Utilise précisément les colonnes **['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']** comme features (X) et la colonne **'{target_column}'** comme cible (y).
- Divise les données en un ensemble d'entraînement (80%) et un ensemble de test (20%) en utilisant `sklearn.model_selection.train_test_split` avec `random_state=42`.
- Entraîne un `RandomForestClassifier` (avec `random_state=42`) sur l'ensemble d'entraînement.
- Calcule et affiche la précision (accuracy) du modèle sur l'ensemble de test en utilisant `sklearn.metrics.accuracy_score`.

Fournis **uniquement le code Python**. Ne mets aucun commentaire (sauf si absolument essentiel pour une logique complexe), aucun texte explicatif avant ou après, et n'utilise pas de blocs Markdown autour du code. Le code doit être directement exécutable.
"""

        try:
            result = subprocess.run(
                ["ollama", "run", "llama2"],  # N'oubliez pas de remplacer "llama2" si votre modèle est différent
                input=prompt,
                capture_output=True,
                text=True,
                timeout=120,  # Augmenté le timeout pour une génération de code plus longue
                check=True,
                encoding='utf-8'
            )
            raw_response = result.stdout
            code = self.extract_code(raw_response)
            return code

        except subprocess.CalledProcessError as e:
            return f"Erreur Ollama : Le processus a retourné un code d'erreur. Stderr : {e.stderr}"
        except subprocess.TimeoutExpired:
            return "Erreur : La génération du code a expiré. Le modèle Ollama a pris trop de temps."
        except Exception as e:
            return f"Une erreur inattendue s'est produite lors de la génération du code : {e}"
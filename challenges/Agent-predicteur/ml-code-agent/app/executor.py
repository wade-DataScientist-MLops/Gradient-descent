import subprocess
import sys
import tempfile
import os

class CodeExecutor:
    def __init__(self):
        pass

    def execute_code(self, code: str) -> str:
        tmp_filename = None
        try:
            with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as tmp_file:
                tmp_file.write(code)
                tmp_filename = tmp_file.name

            result = subprocess.run(
                [sys.executable, tmp_filename],
                capture_output=True,
                text=True,
                timeout=120,
                check=True
            )
            return result.stdout

        except subprocess.CalledProcessError as e:
            return f"Erreur lors de l'exécution du code :\n{e.stderr}"

        except subprocess.TimeoutExpired:
            return "Erreur : délai d'exécution dépassé."

        except Exception as e:
            return f"Erreur inconnue : {str(e)}"

        finally:
            if tmp_filename and os.path.exists(tmp_filename):
                os.remove(tmp_filename)

BASE_PROMPT = """
Tu es un expert en data science. Génère du code Python pour :

1. Charger un dataset CSV nommé '{filename}'
2. Prédire la colonne '{target}'
3. Faire du feature engineering automatiquement
4. Créer un modèle de classification (RandomForest de préférence)
5. Afficher la précision (accuracy)

Donne uniquement du code exécutable, sans texte, ni commentaire.
"""

BASE_PROMPT = """
Tu es un expert en data science. Génère du code Python pour :

1. Charger un dataset CSV nommé '{filename}'
2. Prédire la colonne '{target}'
3. Nettoyer les données en remplaçant les valeurs manquantes sans utiliser inplace dans fillna
4. Encoder automatiquement les variables catégorielles avec LabelEncoder (convertir en str avant encodage)
5. Supprimer les colonnes ['Name', 'Ticket', 'Cabin'] uniquement si elles existent, sans provoquer d'erreur
6. Créer un modèle de classification (RandomForest de préférence)
7. Séparer les données en train/test (80/20)
8. Afficher la précision (accuracy)

Donne uniquement du code Python exécutable, sans texte ni commentaire.
"""

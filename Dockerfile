# Utilise une image Python officielle
FROM python:3.11-slim-bullseye

# Définit le répertoire de travail dans le conteneur
WORKDIR /app

# Définit les variables d'environnement
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHON UNBUFFERED 1

# Installe les dépendances système nécessaires
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copie et installe les dépendances Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie le projet dans le conteneur
COPY . .

# Expose le port 8000
EXPOSE 8000

# Commande pour lancer l'application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

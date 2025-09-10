[![Build Status](https://github.com/Razvan-drb/Python_13_OC/actions/workflows/ci.yml/badge.svg)](https://github.com/Razvan-drb/Python_13_OC/actions)
[![Documentation Status](https://readthedocs.org/projects/python-13-oc/badge/?version=latest)](https://python-13-oc.readthedocs.io/)
[![Coverage](https://img.shields.io/badge/coverage-93%25-brightgreen)](https://github.com/Razvan-drb/Python_13_OC/actions)

# Orange County Lettings


## ✨ Fonctionnalités

- ✅ Gestion des propriétés (lettings) et adresses
- ✅ Profils utilisateurs avec villes favorites  
- ✅ Interface d'administration Django
- ✅ Gestion des erreurs 404/500 personnalisées
- ✅ Monitoring des erreurs avec Sentry
- ✅ Déploiement continu CI/CD

Application de location de biens immobiliers.

## 🚀 Déploiement

L'application est déployée sur Render : https://python-13-oc.onrender.com/

Cette application est déployée automatiquement grâce à un pipeline CI/CD. Pour les instructions détaillées de déploiement, les procédures et les guides de gestion, veuillez consulter la [Documentation de Déploiement](https://your-render-url.onrender.com/deployment.html) dans notre documentation complète.

Copier le .env_dist dans un fichier ".env" et remplir les variables d'environment

### Fonctionnalités Clés :
- **CI/CD Automatisé** avec GitHub Actions
- **Containerisation Docker** avec intégration Docker Hub
- **Déploiement Cloud** sur la plateforme Render
- **Tests automatiques** et contrôles de qualité
- **Déploiements sans temps d'arrêt**

### Liens Rapides :
- [Pipeline CI/CD](https://github.com/Razvan-drb/Python_13_OC/actions)
- [Dépôt Docker Hub](https://hub.docker.com/repository/docker/spartacus33/oc-lettings-app/general)


## 📚 Documentation

La documentation technique est disponible sur ReadTheDocs : https://python-13-oc-lettings.readthedocs.io/en/latest/

## 🛠️ Technologies utilisées

- Django 3.0
- Python 3.11
- SQLite
- Sentry (monitoring d'erreurs)
- Docker
- GitHub Actions (CI/CD)
- Render (hébergement)

## 📦 Installation locale

1. Cloner le repository :

git clone https://github.com/Razvan-drb/Python_13_OC.git
cd Python_13_OC

    Créer un environnement virtuel :

bash

python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

    Installer les dépendances :


pip install -r requirements.txt

    Lancer l'application :


python manage.py runserver


🧪 Tests et qualité de code

    Linting : flake8

    Tests : python manage.py test

    Couverture de test : >80% (actuellement 93%)

📊 Pipeline CI/CD

Le pipeline GitHub Actions exécute automatiquement :

    Tests unitaires et d'intégration

    Vérification de la couverture de code

    Linting avec flake8

🐛 Monitoring des erreurs

Les erreurs sont monitorées avec Sentry : https://sentry.io/

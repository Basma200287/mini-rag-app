# pfe-mini-rag

Ceci est une implémentation minimale du modèle RAG pour la réponse aux questions.

## Exigences
Python 3.8 ou version la plua récente 
### Installation de Python en utilisant Miniconda
1) Télécharge et installe Miniconda à partir d’ici(https://www.anaconda.com/download)
2) Crée un nouvel environnement en utilisant la commande suivante
```bash
$ conda create -n mini-rag python=3.8
```
3) Activer l'environnement 
``` bash 
$ coda activate mini-rag 
```
### (optionnel) configure ta ligne de commande pour une meilleure fiabilité
```bash 
$ export PS1="\[\033[01;32m\]\u@\h:\w\n\[\033[00m\]\$ " 
```
# Installation 
## Installer les packages (bibliothèques) nécessaires au projet 
``` bash 
$ pip install -r requirements.txt
```
### Configurer les variables d’environnement 
```bash 
$ cp .env.exemple .env
```
Définissez vos variables d’environnement dans le fichier '.env', comme la valeur de 'OPENAI_API_KEY'.
## Lancer le serveur FastAPI
``` bash
$ uvicorn main:app --reload --host 0.0.0.0 --port 5000 
```
## Run Docker Compose Services

```bash
$ cd docker 
$ cp .env.exemple .env
```
update `.env` with your credentials
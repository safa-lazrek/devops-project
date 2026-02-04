FROM python:3.11-slim

WORKDIR /app

# Copier les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier l'application
COPY app/ .

# Exposer le port
EXPOSE 5000

# Commande de démarrage
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]

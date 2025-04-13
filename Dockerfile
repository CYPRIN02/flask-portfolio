# 🔧 Image de base avec Python
FROM python:3.11-slim

# 📦 Dépendances système utiles
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# 🦀 Installe Rust (pour packages comme tokenizers/orjson)
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"

# 📁 Répertoire de l'app
WORKDIR /app

# 🔄 Copie les fichiers du projet
COPY . .

# 📦 Installe les dépendances Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 🌐 Expose le port utilisé par Flask/Gunicorn
EXPOSE 8000

# 🚀 Commande de lancement avec Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:create_app()"]

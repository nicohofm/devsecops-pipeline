# Verwende ein offizielles Python-Image als Basis
FROM python:3.9-slim

# Setze das Arbeitsverzeichnis im Container
WORKDIR /app

# Kopiere die Anwendungsdateien in das Arbeitsverzeichnis
COPY . /app

# Installiere die Abhängigkeiten
RUN pip install --no-cache-dir -r requirements.txt

# Exponiere den Port, auf dem die App läuft
EXPOSE 5000

# Definiere den Befehl, der ausgeführt wird, wenn der Container startet
CMD ["python", "app3.py"]


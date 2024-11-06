# Verwende ein offizielles Python-Image als Basis
FROM python:3.9-slim

# Setze das Arbeitsverzeichnis im Container
WORKDIR /app

# Kopiere die Anwendungsdateien in das Arbeitsverzeichnis
COPY . /app

# Exponiere den Port, auf dem die App läuft
EXPOSE 5000

# Definiere den Befehl, der ausgeführt wird, wenn der Container startet
CMD ["python", "app1.py"]
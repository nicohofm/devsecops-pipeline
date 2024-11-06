# Verwende ein offizielles Python-Image als Basis
FROM python:3.8-slim

# Setze das Arbeitsverzeichnis
WORKDIR /devsecops-pipeline

# Kopiere die requirements.txt und installiere die Abhängigkeiten
COPY src/app3/requirements.txt /devsecops-pipeline/

RUN pip install --no-cache-dir -r requirements.txt

# Kopiere den Code von app3
COPY src/app3 /devsecops-pipeline/src/app3

# Setze den Startbefehl für app3
CMD ["python", "/devsecops-pipeline/src/app3/app.py"]

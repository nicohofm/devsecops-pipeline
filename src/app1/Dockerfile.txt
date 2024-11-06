# Verwende ein offizielles Python-Image als Basis
FROM python:3.8-slim

# Setze das Arbeitsverzeichnis
WORKDIR /devsecops-pipeline

# Kopiere die requirements.txt und installiere die Abhängigkeiten
COPY src/app1/requirements.txt /devsecops-pipeline/

RUN pip install --no-cache-dir -r requirements.txt

# Kopiere den Code von app1
COPY src/app1 /devsecops-pipeline/src/app1

# Setze den Startbefehl für app1
CMD ["python", "/devsecops-pipeline/src/app1/app.py"]


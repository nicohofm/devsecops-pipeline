# Verwende ein offizielles Python-Image als Basis
FROM python:3.8-slim

# Setze das Arbeitsverzeichnis
WORKDIR /devsecops-pipeline

# Kopiere die requirements.txt und installiere die Abhängigkeiten
COPY src/app2/requirements.txt /devsecops-pipeline/

RUN pip install --no-cache-dir -r requirements.txt

# Kopiere den Code von app2
COPY src/app2 /devsecops-pipeline/src/app2

# Setze den Startbefehl für app2
CMD ["python", "/devsecops-pipeline/src/app2/app.py"]

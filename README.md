|[![Python package](https://github.com/bylickilabs/SystemAnalyzer-2.0/actions/workflows/python-package.yml/badge.svg)](https://github.com/bylickilabs/SystemAnalyzer-2.0/actions/workflows/python-package.yml)| ![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python) |![NumPy](https://img.shields.io/badge/Powered%20by-NumPy-013243?logo=numpy) |
|---|---|---|

# System Analyzer – Installationsanleitung

|![sysanalyzer2](https://github.com/user-attachments/assets/9c543377-9d02-438e-93e1-6d9dec29bc62)|
|---|

---

## Überblick

**System Analyzer** ist eine moderne Systemanalyse-Anwendung, entwickelt in **Python** mit **NumPy** als leistungsfähige Grundlage für numerische Analysen und Statistik.  
Das Tool kombiniert Systeminformationen, Statistikfunktionen und eine Web-API – ideal für Power User, Monitoring, IT und Entwicklung.

---

## Voraussetzungen

- **Python 3.8 oder neuer**  
  Download: [https://www.python.org/downloads/](https://www.python.org/downloads/)
- **pip** (Python Package Installer, i.d.R. bereits enthalten)

---

## Installation

1. **Projektdatei herunterladen**  
   Speichere die Datei `system_analyzer.py` an einem beliebigen Ort, z. B. auf den Desktop.

2. **Benötigte Python-Bibliotheken installieren**  
   Öffne ein Terminal/PowerShell und führe folgenden Befehl aus:

```yarn
pip install numpy psutil flask matplotlib
```

> NumPy wird hierbei für alle numerischen Analysen, Statistik und Datenaggregation eingesetzt.

3. Script ausführen
  - Systeminfos (CLI):
 
```yarn
python system_analyzer.py --cli
python system_analyzer.py --stats
python system_analyzer.py --api
```

> Die API ist dann auf http://127.0.0.1:5000 erreichbar.

---

## Hinweise
  - NumPy ist das Kernmodul für Statistik, mathematische Berechnungen und Analysen in diesem Projekt.

> Die Anwendung nutzt außerdem:
- psutil: Zugriff auf Systemmetriken (CPU, RAM, Prozesse etc.)
- Flask: Bereitstellung der Web-API
- matplotlib: Grafische Ausgaben (Diagramme)

> Es werden keine Daten an externe Server übertragen – alles läuft lokal auf deinem Rechner.

---


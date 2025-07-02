# Extrator de Áudio MP3 de Vídeo em Python

Este script permite extrair o áudio de um vídeo e salvá‑lo como um arquivo MP3.

## Pré‑requisitos

- Python 3.7 ou superior
- [ffmpeg](https://ffmpeg.org/) instalado e acessível no PATH

## Instalação

1. Clone este repositório ou faça o download:
   ```bash
   git clone <url-do-repo>
   cd extract_audio_project

## Crie e ative um ambiente virtual:
```bash
python3 -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```
## Instale as dependências:
```bash
pip install -r requirements.txt
```
## Uso
```bash
python extract_audio.py "WhatsApp Video 2025-07-01 at 20.39.25.mp4"
```
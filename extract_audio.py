import argparse
from moviepy.editor import VideoFileClip
import os


def extract_audio(input_path: str, output_path: str) -> None:
    """
    Extrai o áudio do vídeo em `input_path` e salva como MP3 em `output_path`.
    """
    # Carrega o vídeo
    video = VideoFileClip(input_path)
    # Extrai e salva o áudio
    video.audio.write_audiofile(output_path)
    video.close()


def main():
    parser = argparse.ArgumentParser(
        description="Extrai o áudio de um vídeo e converte para MP3"
    )
    parser.add_argument(
        "input",
        help="WhatsApp Video 2025-07-01 at 20.39.25.mp4"
    )
    parser.add_argument(
        "output",
        nargs="?",
        help="arquivo MP3 (padrão: mesmo nome do vídeo com extensão .mp3)"
    )
    args = parser.parse_args()

    input_path = args.input
    if args.output:
        output_path = args.output
    else:
        base, _ = os.path.splitext(input_path)
        output_path = base + ".mp3"

    print(f"Extraindo áudio de '{input_path}' para '{output_path}'...")
    extract_audio(input_path, output_path)
    print("Concluído!")


if __name__ == "__main__":
    main()
import yt_dlp

def baixar_audio(url, caminho_destino=r'C:\Users\celio\Music'):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',  # Seleciona o melhor áudio disponível
            'outtmpl': f'{caminho_destino}/%(title)s.%(ext)s',  # Local de salvamento
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',  # Extrai apenas o áudio
                'preferredcodec': 'mp3',  # Converte para MP3
                'preferredquality': '192',  # Qualidade do áudio (opcional)
            }],
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download do áudio concluído!")
    except Exception as e:
        print(f"Erro ao baixar áudio: {e}")

url = input("Digite a URL do vídeo: ")
baixar_audio(url)

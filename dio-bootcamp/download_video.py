import yt_dlp


# Função para baixar o vídeo
def baixar_video(url, caminho_destino=""):
    try:
        # Configuração para baixar o vídeo
        ydl_opts = {
            'outtmpl': f'{caminho_destino}/%(title)s.%(ext)s',  # Salva o vídeo no caminho especificado
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print(f"Download concluído! Vídeo salvo em: {caminho_destino}")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")


# Solicita a URL do vídeo
url_video = input("Digite a URL aqui: ")

# Caminho para salvar o vídeo
caminho = r'C:\Users\celio\Videos'

# Chama a função para baixar o vídeo
baixar_video(url_video, caminho)

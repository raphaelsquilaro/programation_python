import customtkinter as ctk
from pytubefix import YouTube
import os

# Configurações visuais
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class AppDownloader(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Python YouTube Downloader")
        self.geometry("500x350")

        # --- Interface (UI) ---
        self.label_titulo = ctk.CTkLabel(self, text="Baixar Vídeo do YouTube", font=("Roboto", 24, "bold"))
        self.label_titulo.pack(pady=20)

        self.entry_url = ctk.CTkEntry(self, placeholder_text="Cole o link do vídeo aqui...", width=400)
        self.entry_url.pack(pady=10)

        self.btn_download = ctk.CTkButton(self, text="Iniciar Download", command=self.download_video)
        self.btn_download.pack(pady=20)

        # Feedback para o usuário
        self.label_status = ctk.CTkLabel(self, text="", font=("Roboto", 14))
        self.label_status.pack(pady=10)

        self.label_progresso = ctk.CTkLabel(self, text="")
        self.label_progresso.pack(pady=5)

    def download_video(self):
        url = self.entry_url.get()
        
        if not url:
            self.label_status.configure(text="Erro: Insira uma URL válida!", text_color="red")
            return

        self.label_status.configure(text="Processando... aguarde.", text_color="yellow")
        self.update() # Força a interface a atualizar o texto antes de começar

        # --- APLICAÇÃO DOS CONCEITOS ---
        try:
            # 1. Criando o objeto YouTube (Função da biblioteca)
            yt = YouTube(url, on_progress_callback=self.progresso_check)
            
            # 2. Buscando a maior resolução (Lógica de filtragem)
            video_stream = yt.streams.get_highest_resolution()
            
            self.label_status.configure(text=f"Baixando: {yt.title[:40]}...", text_color="white")
            
            # 3. Fazendo o download na pasta do usuário (Downloads)
            caminho_destino = os.path.join(os.path.expanduser("~"), "Downloads")
            video_stream.download(output_path=caminho_destino)

            self.label_status.configure(text="Download Concluído com Sucesso! ✅", text_color="green")
            self.label_progresso.configure(text=f"Salvo em: {caminho_destino}")

        except Exception as e:
            # Captura erros de link inválido, falta de internet, etc.
            self.label_status.configure(text=f"Erro ao baixar: Link inválido ou protegido", text_color="red")
            print(f"Erro real: {e}")

    def progresso_check(self, stream, chunk, bytes_remaining):
        # Função para calcular a porcentagem do download
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        porcentagem = (bytes_downloaded / total_size) * 100
        self.label_progresso.configure(text=f"Progresso: {int(porcentagem)}%")
        self.update()

if __name__ == "__main__":
    app = AppDownloader()
    app.mainloop()
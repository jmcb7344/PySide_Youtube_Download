# This Python file uses the following encoding: utf-8
import sys
from gui_PySide import View
from pytube import YouTube
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog


class Ventana(QWidget, View):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.buscar.clicked.connect(self.buscar_video)
        self.descargar.clicked.connect(self.descarga)
        self.salir.clicked.connect(self.close)
        self.SAVE_PATH = ''
        self.comentario.setText("Bienvenido")

    def buscar_video(self):
        try:
            url = self.link.text()
            video = YouTube(url)
            self.comentario_2.setText(f'{video.title}')
            self.seleccion.setEnabled(True)
            self.seleccion.setStyleSheet(u"color: black; background-color: #fff;")
            self.comentario.setText('...')
        except Exception as e:
            self.comentario_2.setText(str(e))

    def descarga(self):

        url = self.link.text() 
        video = YouTube(url)
        self.comentario.setText('Descargando...')

        if self.SAVE_PATH == '':
            self.SAVE_PATH = QFileDialog.getExistingDirectory(self, "Guardar", ".")

        try:
            if self.seleccion.currentText() == 'Descargar mejor calidad':
                down_video = video.streams.get_highest_resolution()
                file_size = down_video.filesize
                down_video.download(output_path=self.SAVE_PATH)
                self.comentario.setText(' Descarga completada '.center(50, '-'))

            elif self.seleccion.currentText() =='Descargar menor calidad':
                down_video = video.streams.get_lowest_resolution()
                down_video.download(output_path=self.SAVE_PATH)
                self.comentario.setText(' Descarga completada '.center(50, '-'))

            elif self.seleccion.currentText() == 'Descargar MP3':
                nombre = video.title + '.mp3'
                down_video = video.streams.get_audio_only()
                down_video.download(output_path=self.SAVE_PATH, filename=nombre)
                self.comentario.setText(' Descarga completada '.center(50, '-'))

            
        
        except Exception as e:
            self.comentario.setText(str(e))
        

    def close(self):
        sys.exit()

if __name__ == "__main__":
    app = QApplication([])
    widget = Ventana()
    widget.show()
    sys.exit(app.exec())

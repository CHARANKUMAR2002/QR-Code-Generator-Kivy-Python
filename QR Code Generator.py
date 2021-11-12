from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
import pyqrcode
from kivy.core.window import Window


Builder.load_file("QR Code Generator.kv")


class MyLayout(Widget):

    Window.size = (360,460)

    def gen(self):
        link = self.ids.code.text
        filename = self.ids.file.text
        qr = pyqrcode.create(link)
        qr.png(filename, scale=4)
        self.ids.code.text = ""
        self.ids.file.text = ""




class QRCodeGenerator(App):
    def build(self):
        return MyLayout()

if __name__ == "__main__":
    QRCodeGenerator().run()
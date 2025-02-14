import qrcode
import PIL

link = "http://dnd2024.wikidot.com"

nome_arquivo = "qr_code.png"


qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4
)


qr.add_data(link)

qr.make(fit=True)

imagem = qr.make_image()

imagem.save(nome_arquivo)

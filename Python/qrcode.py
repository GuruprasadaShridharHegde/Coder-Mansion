import io
import qrcode
qr = qrcode.QRCode()
qr.add_data(" Welcome to coder Mansion ")
f = io.StringIO()
qr.print_ascii(out=f)
f.seek(0)
print(f.read())
import qrcode

# mesajul care apare dupa scanare
data = "Tema facuta de Iancu Andrei-Nicolae - grupa 1021- Seria E"

# creez un QR (cred ca e bine cu versiunea 1?)
qr = qrcode.QRCode(
    version=1, # marimea qr-ului (am ales 1)
    error_correction=qrcode.constants.ERROR_CORRECT_L, # corectie la cod
    box_size=10, # patratelele din QR (cred)
    border=4 # marginea qr-ului
)

# adaug informatia in QR
qr.add_data(data)
qr.make(fit=True)

# fac imaginea QR-ului, negru pe alb
img = qr.make_image(fill="black", back_color="white")

# salvez codul generat pe calculator, dar poate e bine si alt format?
img.save("codqr.png")

print("Codul QR e gata si s-a salvat ca 'codQR.png'")

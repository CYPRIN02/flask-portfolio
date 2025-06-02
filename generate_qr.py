import qrcode

# Lien vers portefolio ou LinkedIn
url = "https://www.linkedin.com/in/andrianantenaina-princy-r-649594151/"  # ou "https://flask-portfolio-thic.onrender.com/"

# Créer le QR code
img = qrcode.make(url)

# Sauvegarder l'image
img.save("app/static/images/qr_site.png")

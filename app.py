from flask import Flask, request, render_template, send_from_directory
from PIL import Image
import io
import os

app = Flask(__name__, template_folder='')

# Définissez le répertoire où vous stockerez temporairement les images traitées
UPLOAD_FOLDER = 'uploads'
app.config[''] = UPLOAD_FOLDER

# Page d'accueil
@app.route('/')
def index():
    return render_template('index.html')

# Traitement de l'image
@app.route('/upload', methods=['POST'])
def upload():
    if 'image' in request.files:
        image = request.files['image']
        if image.filename != '':
            # Traitement de l'image (exemple : conversion en noir et blanc)
            img = Image.open(image)
            img = img.convert('L')  # Convertir en noir et blanc

            # Enregistrez l'image traitée dans le répertoire d'uploads
            processed_image_path = os.path.join(app.config[''], 'processed_image.png')
            img.save(processed_image_path, 'PNG')

            return render_template('index.html')

    return "Erreur lors du traitement de l'image."

# Route pour afficher l'image traitée
@app.route('/display_image')
def display_image():
    processed_image_path = os.path.join(app.config[''], 'processed_image.png')
    return send_from_directory(app.config[''], 'processed_image.png')

if __name__ == '__main__':
    os.makedirs(app.config[''], exist_ok=True)
    app.run(debug=True)

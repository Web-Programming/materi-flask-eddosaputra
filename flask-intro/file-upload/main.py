from flask import Flask, request, redirect, url_for, jsonify
import os 
import time

UPLOAD_FOLDER = 'static/uploads'
#ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return 'file upload demo'

@app.route('/uploadfile', methods=['GET','POST'])
def uploadfile():
    if request.method == 'POST':
        # Cek jika ada file yang diunggah
        foto = request.files['foto']
        if foto:
            # Mengambil timestamp saat ini untuk menambahkan ke nama file
            timestamp = str(int(time.time()))
        
            # Mengambil ekstensi file asli
            ext = foto.filename.split('.')[-1]
            # Menambahkan ekstensi ke nama file unik
            unique_filename = f"{timestamp}.{ext}"
            # Menyimpan file dengan nama unik
            foto_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
            foto.save(foto_path)
            # meyimpan path relatif dengan menggunakan
            foto_path = f'uploads/{unique_filename}' # Menyimpan path relatif dengan menggunakan
            data = {
            "status" : "Success",
            "message" : "Data berhasil diupload",
             }
            return jsonify(data)
        else:
            foto_path = None
            # Pesan konfirmasi
            data = {
            "status" : "Success",
            "message" : "Data berhasil diupload",
            }
            return jsonify(data)
        
    # JSON empty
    data = {
    "status" : "Failed",
    "message" : "Pick a foto to upload",
    }
    return jsonify(data) 

#pip install Flask-RESTful




#keep this as is
if __name__ == '__main__':
    app.run(debug=True)
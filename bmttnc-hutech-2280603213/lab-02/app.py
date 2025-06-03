from pydoc import text
from flask import Flask, app, render_template, request, json, jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher

app = Flask(__name__)

# router routes for home page
@app.route('/')
def home():
    return render_template("index.html")

# router routes for caesar cipher
@app.route('/caesar')
def caesar():
    return render_template("caesar.html")

@app.route('/caesar/encrypt', methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    caesar = CaesarCipher()
    encrypt_text = caesar.encrypt_text(text, key)
    return f"Encrypted: <strong>{encrypt_text}</strong>"

@app.route('/caesar/decrypt', methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    caesar = CaesarCipher()
    decrypt_text = caesar.decrypt_text(text, key)
    return f"Decrypted: <strong>{decrypt_text}</strong>"

# router routes for vigenere cipher
@app.route('/vigenere')
def vigenere():
    return render_template("vigenere.html")

@app.route('/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    vigenere = VigenereCipher()
    encrypt_text = vigenere.vigenere_encrypt(text, key)
    return f"Encrypted: <strong>{encrypt_text}</strong>"

@app.route('/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    vigenere = VigenereCipher()
    decrypt_text = vigenere.vigenere_decrypt(text, key)
    return f"Decrypted: <strong>{decrypt_text}</strong>"

# router routes for railfence cipher
@app.route('/railfence')
def railfence():
    return render_template("railfence.html")

@app.route('/railfence/encrypt', methods=['POST'])
def railfence_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    railfence = RailFenceCipher()
    encrypt_text = railfence.rail_fence_encrypt(text, key)
    return f"Encrypted: <strong>{encrypt_text}</strong>"

@app.route('/railfence/decrypt', methods=['POST'])
def railfence_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    railfence = RailFenceCipher()
    decrypt_text = railfence.rail_fence_decrypt(text, key)
    return f"Decrypted: <strong>{decrypt_text}</strong>"

# router routes for playfair cipher
@app.route('/playfair')
def playfair():
    return render_template("playfair.html")

@app.route('/playfair/creatematrix', methods=['POST'])
def playfair_creatematrix():
    matrixKey = request.form['matrixKey']
    playfair = PlayFairCipher()
    playfair_matrix = playfair.create_playfair_matrix(matrixKey)
    matrix_html = "<table class='table table-bordered text-center table-sm'>"
    for row in playfair_matrix:
        matrix_html += "<tr>" + "".join(f"<td>{char}</td>" for char in row) + "</tr>"
    matrix_html += "</table>"
    return f"<h4>Matrix for key '{matrixKey.upper()}'</h4>" + matrix_html

@app.route('/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    playfair = PlayFairCipher()
    matrix = playfair.create_playfair_matrix(key)
    encrypt_text = playfair.playfair_encrypt(text, matrix)
    return f"Encrypted: <strong>{encrypt_text}</strong>"

@app.route('/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    playfair = PlayFairCipher()
    matrix = playfair.create_playfair_matrix(key)
    decrypt_text = playfair.playfair_decrypt(text, matrix)
    return f"Decrypted: <strong>{decrypt_text}</strong>"

# main function
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5050, debug=False)


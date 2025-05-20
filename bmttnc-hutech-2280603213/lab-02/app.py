from pydoc import text
from flask import Flask, app, render_template, request, json
from cipher.caesar import CaesarCipher

app = Flask(__name__)

# router routes for home page
@app.route('/')
def home():
    return render_template("index.html")

# router routes for caesar cipher
@app.route('/caesar')
def caesar():
    return render_template("caesar.html")

@app.route('/encrypt', methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    Caeser = CaesarCipher()
    encrypt_text = Caeser.encrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypt_text}"


@app.route('/decrypt', methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    Caeser = CaesarCipher()
    decrypt_text = Caeser.decrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypt_text}"

# main function
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5050, debug=True)


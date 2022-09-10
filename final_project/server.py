from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator", static_folder="static")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    result_text = translator.english_to_french(textToTranslate)
    return request.args.get('translated_text', result_text)

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    result_text = translator.french_to_english(textToTranslate)
    return request.args.get('translated_text', result_text)

@app.route("/")
def renderIndexPage():
    return render_template("index.html")
   

if __name__ == "__main__":
    app.run(debug=True, port=8080)

from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator", static_folder="static")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    result_jsonstr = translator.english_to_french(textToTranslate)
    tttyyy = result_jsonstr["translations"]
    ttteee = tttyyy[0]
    tttrrr = ttteee["translation"]
    return request.args.get('translated_text', tttrrr)

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    result_jsonstr = translator.french_to_english(textToTranslate)
    tttyyy = result_jsonstr["translations"]
    ttteee = tttyyy[0]
    tttrrr = ttteee["translation"]
    return request.args.get('translated_text', tttrrr)

@app.route("/")
def renderIndexPage():
    return render_template("index.html")
   

if __name__ == "__main__":
    app.run(debug=True, port=8080)

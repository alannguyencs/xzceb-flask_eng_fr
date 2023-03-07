from machine_translation import translator
from flask import Flask, render_template, request
import json
# import machine_translation

app = Flask("Web Translator")

@app.route("/englishToSpanish")
def englishToSpanish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    return "Translated text to Spanish"

@app.route("/spanishToEnglish")
def spanishToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    return "Translated text to English"

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    translated_text = translator.english_to_french(textToTranslate)
    return translated_text

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    translated_text = translator.french_to_english(textToTranslate)
    return translated_text

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

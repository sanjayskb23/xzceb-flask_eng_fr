from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    frenchtext=translator.english_to_french(textToTranslate)

    # Write your code here

    return frenchtext

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    englishtext=translator.french_to_english(textToTranslate)
    return englishtext

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    print('Hi This is translator page by Sanjay Bharti')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

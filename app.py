import os
import openai
import pytesseract
from PIL import Image
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = "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"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        image = request.files['file']
        img = Image.open(image)
        extracted_text = pytesseract.image_to_string(img)

        chatgpt_response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=extracted_text,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.5
        )

        result = chatgpt_response.choices[0].text.strip()
        return render_template('index.html', extracted_text=extracted_text, result=result)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

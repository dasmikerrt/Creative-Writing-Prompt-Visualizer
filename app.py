from flask import Flask, render_template, request, jsonify
import requests
import urllib.parse

app = Flask(__name__)

def generate_prompt():
    prompt = "Generate a unique and imaginative writing prompt."
    url = f"https://text.pollinations.ai/{urllib.parse.quote(prompt)}"
    response = requests.get(url)
    return response.text.strip()

def generate_image(prompt):
    encoded = urllib.parse.quote(prompt)
    image_url = f"https://image.pollinations.ai/prompt/{encoded}?model=flux&width=1024&height=1024"
    return image_url

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    prompt = generate_prompt()
    image = generate_image(prompt)
    return jsonify({"prompt": prompt, "image_url": image})

if __name__ == '__main__':
    app.run(debug=True)

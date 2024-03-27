from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from openai import OpenAI
import os
import io

app = Flask(__name__)

pre_prompt = "Write comprehensive unit tests in Python for the following code:"

client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = os.getenv('API_KEY')
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    input_code = request.json['code']
    output_code = my_action(input_code)  # Replace with your actual function

    return jsonify({'outputCode': output_code})

def my_action(code):

    completion = client.chat.completions.create(
    model="meta/codellama-70b",
    messages=[{"role":"user","content": pre_prompt + code}],
    temperature=0.1,
    top_p=1,
    max_tokens=1024,
    stream=True
    )

    output_buffer = io.StringIO()

    for chunk in completion:
        if chunk.choices[0].delta.content is not None:
            cur_line = chunk.choices[0].delta.content
            output_buffer.write(cur_line)  # Write to string buffer

    return output_buffer.getvalue()


if __name__ == '__main__':
    app.run(debug=True)

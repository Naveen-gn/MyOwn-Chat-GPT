from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = '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'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_input},
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    bot_response = response['choices'][0]['message']['content']

    return jsonify({"response": bot_response})

if __name__ == '__main__':
    app.run(debug=True)

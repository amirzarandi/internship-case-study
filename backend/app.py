from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:4528@localhost/instalily'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)

from models.knowledge import Knowledge
db.Model = Knowledge.__class__

@app.route('/ask_chat_embedding', methods=['GET'])
def ask_chat_embedding_route():
    from integration import ask_chat_embed
    user_input = request.args.get('input')
    history = request.args.get('history')

    try:
        history = eval(history) if history else []
    except Exception as e:
        return jsonify({"error": f"Invalid history format: {e}"}), 400

    response = ask_chat_embed(user_input, history)

    return jsonify({"response": response})

@app.route('/ask_chat_langchain', methods=['GET'])
def ask_chat_langchain_route():
    from integration import ask_chat_langchain
    user_input = request.args.get('input')
    history = request.args.get('history')

    try:
        history = eval(history) if history else []
    except Exception as e:
        return jsonify({"error": f"Invalid history format: {e}"}), 400

    response = ask_chat_langchain(user_input, history)

    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
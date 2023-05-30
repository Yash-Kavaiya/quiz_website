from flask import Flask, render_template, request, jsonify
from database import engine, load_jobs_from_db

app = Flask(__name__)


@app.route('/')
def hello_world():
  quiz = load_jobs_from_db()
  return render_template('index.html', exam=quiz)


@app.route('/api')
def list_quiz():
  quiz = load_jobs_from_db()
  return jsonify(quiz)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)

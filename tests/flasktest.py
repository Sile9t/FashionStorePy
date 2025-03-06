from flask import Flask

app = Flask(__name__)

@app.before_first_request
def before_first_request_func():
    print("Этот код выполняется перед первым запросом.")

@app.route('/')
def home():
    return "Привет, мир!"

if __name__ == "__main__":
    app.run(debug=True)

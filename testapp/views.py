from testapp import app


@app.route('/')
def index():
    return 'Hello World!'

# developブランチ

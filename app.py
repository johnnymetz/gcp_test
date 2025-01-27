from flask import Flask

app = Flask(__name__)
app.config.from_object('config.ProductionConfig')

from views import *

if __name__ == '__main__':
    app.run()

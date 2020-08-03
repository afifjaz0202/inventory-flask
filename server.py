import peeweedbevolve # new; must be imported before models
from flask import Flask, render_template, request
from models import db, Store

app = Flask(__name__)

@app.before_request
def before_request():
    db.connect()

@app.after_request
def after_request(response):
    db.close()
    return response

@app.cli.command() # new
def migrate(): # new 
    db.evolve(ignore_tables={'base_model'}) # new

@app.route("/")
def index():
    # with this code, your need to directly type in /store
    store_name = request.args.get('store_name')
    print(store_name)
    newstore = Store(name = store_name)
    newstore.save()
    return render_template('index.html', store_name = store_name)

@app.route("/store")
def store():
    return render_template('store.html')

if __name__ == '__main__':
    app.run(debug = True)
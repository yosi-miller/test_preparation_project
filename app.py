from flask import Flask

from database.repository import get_black_list

app = Flask(__name__)

@app.route('/')
def hello_world():
   return get_black_list()



if __name__ == '__main__':
   app.run(debug=True)
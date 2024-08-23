

from flask import Flask

app= Flask(__name__)

def gfg():
   return "geeksforgeeks"
app.add_url_rule('/', 'g2g', 'gfg')

from flask import Flask
app = Flask(__name__)

@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name

if __name__ == '__main__':
   app.run()

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello, yaqeen!'

if __name__ =="__main__":
  app.run(host='0.0.0.0', port=8080) #run Flask server

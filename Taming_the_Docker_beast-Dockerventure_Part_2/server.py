from flask import Flask
import os

server = Flask(__name__)

color = os.environ['color']

@server.route("/")
def hey():
  return "Hey there my favourite color is: {}!".format(color)

if __name__ == "__main__":
   server.run(host='0.0.0.0')
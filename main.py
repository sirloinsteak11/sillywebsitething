from replit import web
from flask import Flask, jsonify
from data_fetch import get_random_tweet

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
  return "FUUUUUUUUUUUCCCCCKKK RAAAAAHHHHHH"

@app.route('/api/random_twit_like', methods=['GET'])
async def get_krisnard_data():
  #tweet = get_random_tweet()
  krisnard_data = {
    'url': "tweet"
  }
  return jsonify(krisnard_data)

@app.route('/api/random_gel', methods=['GET', 'POST'])
async def get_random_gel():
  return 0
  


# if the file is being executed directly and not as a module...
if __name__ == "__main__":
  web.run(app)
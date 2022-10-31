from data_fetch import get_random_tweet
from flask import jsonify

def makeJson():
  return jsonify(get_random_tweet())
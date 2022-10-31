import random
import tweepy as tw
from pygelbooru import Gelbooru
import os

gel_api_key = os.environ['gel_api_key']
gel_id_key = os.environ['gel_id_key']

blacklist = [
  'gore', 'rape', 'futa', 'loli', 'guro', 'snuff', 'amputation', 'pregnant'
]

# API keyws that yous saved earlier
bearer_token = os.environ['bearer_token']
auth = tw.OAuth2BearerHandler(bearer_token = os.environ['bearer_token'])

# Authenticate to Twitter
api = tw.API(auth=auth)
tclient = tw.Client(bearer_token)

# gets specified user
user_id = os.environ['twit_user_id']

# hello gelbooru
gelbooru = Gelbooru(gel_api_key, gel_id_key)

#empty variables
tweet_list = []

# @app.route("/api/random_twit_like", methods=["GET"])
def get_random_tweet():
  response = tclient.get_liked_tweets(user_id, media_fields=['preview_image_url,url'], expansions=['attachments.media_keys'], max_results=5)

  #dataFile = open('data.txt', 'w')

  for tweet in response.data:
    tweets = tweet.id
    tweet_list.append(tweets)
  liked_post = random.choice(tweet_list)
  post_data = api.get_status(liked_post)
  post_media_data = post_data.extended_entities
  pmd2 = post_media_data.get('media')
  return pmd2[0].get('media_url')

  #url = tweet_list.get("preview_image_url")
    
  #dataFile.close()

# @app.route ("/api/random_gel", methods=["GET,POST"])
async def get_random_gelbooru(tags):
  msgcontent = tags.replace('!gel', ' ')
  search2 = msgcontent.strip()
  results = await gelbooru.random_post(tags=search2, exclude_tags=blacklist)
  if not results:
    return 'no results found!!!'
  else:
    return results

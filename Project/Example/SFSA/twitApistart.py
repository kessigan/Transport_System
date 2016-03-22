# from TwitterAPI import TwitterAPI
# 
# 
# SEARCH_TERM = '#flarrow'
# 
# # auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
# # auth.set_access_token(access_token, access_token_secret)
# # auth = tweepy.OAuthHandler("YFo9dsquIXJVfWRlNaZD47IF6", "0U33ZOIIVJatZR2pG4JKuHHAxaWYu5CRE2gAppKw7GomEyLjRh")
# # auth.set_access_token("2306462186-D2LXwTUb57Pu7vsJSgvGPZcT0P271pLZXQIRk8Z", "BlDuNoeCSfYkrHDPx4EcbfXo4WsUtufgCHlnuT6ZXVnsT")
# 
# CONSUMER_KEY = "YFo9dsquIXJVfWRlNaZD47IF6"
# CONSUMER_SECRET = "0U33ZOIIVJatZR2pG4JKuHHAxaWYu5CRE2gAppKw7GomEyLjRh"
# ACCESS_TOKEN_KEY = "2306462186-D2LXwTUb57Pu7vsJSgvGPZcT0P271pLZXQIRk8Z"
# ACCESS_TOKEN_SECRET = "BlDuNoeCSfYkrHDPx4EcbfXo4WsUtufgCHlnuT6ZXVnsT"
# 
# 
# api = TwitterAPI(CONSUMER_KEY,
#                  CONSUMER_SECRET,
#                  ACCESS_TOKEN_KEY,
#                  ACCESS_TOKEN_SECRET)
# 
# r = api.request('search/tweets', {'q': SEARCH_TERM})
# 
# for item in r:
#     print(item['text'] if 'text' in item else item)
# 
# print('\nQUOTA: %s' % r.get_rest_quota())

from TwitterAPI import TwitterAPI
import csv
from pymongo import MongoClient


TRACK_TERM = '#flarrow'
TRACK_TERM2 = '#RememberingMandela'
TRACK_TERM3 = '#tvd'
TRACK_TERM4 = '#theoriginals'
TRACK_TERM5 = '#scienceforum'
TRACK_TERM6 = '#SFSA2015'
TRACK_TERM7 = '#SFSA'

#Linda
# CONSUMER_KEY = "YFo9dsquIXJVfWRlNaZD47IF6"
# CONSUMER_SECRET = "0U33ZOIIVJatZR2pG4JKuHHAxaWYu5CRE2gAppKw7GomEyLjRh"
# ACCESS_TOKEN_KEY = "2306462186-D2LXwTUb57Pu7vsJSgvGPZcT0P271pLZXQIRk8Z"
# ACCESS_TOKEN_SECRET = "BlDuNoeCSfYkrHDPx4EcbfXo4WsUtufgCHlnuT6ZXVnsT"

#gary
CONSUMER_KEY = "EbFSxnAlbNcLHKSuO8J8xIR2p"
CONSUMER_SECRET = "aSipx4fYBZlbigcckbLExb2K38D96jHc5xbVJddbNjA8wt7aKS"
ACCESS_TOKEN_KEY = "605737172-p8gGJumLoB7Nh7wpFRAaiH2s17uXopHCMLJeh59x"
ACCESS_TOKEN_SECRET = "tuV7u3oBU8oUZFDdFt2OxHo2l39LcuzfEPRcqKVmeeZng"


# try:
api = TwitterAPI(CONSUMER_KEY,
                 CONSUMER_SECRET,
                 ACCESS_TOKEN_KEY,
                 ACCESS_TOKEN_SECRET)

# r = api.request('statuses/filter', {'track': [TRACK_TERM,TRACK_TERM2,TRACK_TERM3,TRACK_TERM4], 'locations' : '16,-46,38,-22'})
r = api.request('statuses/filter', {'track': [TRACK_TERM6, TRACK_TERM7,TRACK_TERM5]})
#create the client on localhost
client = MongoClient('localhost:27017')
 
#create database WorkshopDB
db = client.TweetsDB
 
#drop collection workshopData if in existence
# db.tweetsDBCollection.drop()
 


for item in r:
    tweet_dict = {}
    if 'text' in item:
        tweet_dict["text"] = item["text"]
    if 'user' in item:
        if 'screen_name' in item["user"]:
            tweet_dict["screen_name"] = item["user"]["screen_name"]
        if 'name' in item["user"]:
            tweet_dict["name"] = item["user"]["name"]
    if 'created_at' in item:
        tweet_dict["created_at"] = item["created_at"]
    if 'coordinates' in item:
        tweet_dict["coordinates"] = item["coordinates"]
        
    #add each individual row as a document to the collection in the DB
    db.tweetsDBCollection.insert( tweet_dict )

# except TwitterAPI.TwitterError.TwitterConnectionError:
#         # temporary interruption, re-try request
#         pass
    
#     else item


# {       u'contributors': None, 
#         u'truncated': False, 
#         u'text': u'RT @Makanya_BP: #cuttingedge these people should be arrested, abduction is a crime... Abducting a child for cultural purposes is not a defe\u2026', 
#         u'is_quote_status': False, 
#         u'in_reply_to_status_id': None, 
#         u'id': 672510330606649346L, 
#         u'favorite_count': 0, 
#         u'source': u'<a href="http://twitter.com/#!/download/ipad" rel="nofollow">Twitter for iPad</a>', 
#         u'retweeted': False, 
#         u'coordinates': None, 
#         u'timestamp_ms': u'1449173932111', 
#         u'entities': {u'user_mentions': [{u'id': 2943347056L, u'indices': [3, 14], u'id_str': u'2943347056', u'screen_name': u'Makanya_BP', u'name': u'Bonginkosi'}], 
#         u'symbols': [], 
#         u'hashtags': [{u'indices': [16, 28], u'text': u'cuttingedge'}], 
#         u'urls': []}, 
#         u'in_reply_to_screen_name': None, 
#         u'id_str': u'672510330606649346', 
#         u'retweet_count': 0, 
#         u'in_reply_to_user_id': None, 
#         u'favorited': False, 
#         u'retweeted_status': {
#                               u'contributors': None, 
#                               u'truncated': False, 
#                               u'text': u'#cuttingedge these people should be arrested, abduction is a crime... Abducting a child for cultural purposes is not a defence...', 
#                               u'is_quote_status': False, 
#                               u'in_reply_to_status_id': None, 
#                               u'id': 672503263929999368L, 
#                               u'favorite_count': 1, 
#                               u'source': u'<a href="http://twitter.com/download/android" rel="nofollow">Twitter for Android</a>', 
#                               u'retweeted': False, 
#                               u'coordinates': None, 
#                               u'entities': {u'user_mentions': [], 
#                                             u'symbols': [], 
#                                             u'hashtags': [{u'indices': [0, 12], u'text': u'cuttingedge'}], 
#                                             u'urls': []}, 
#                                u'in_reply_to_screen_name': None, 
#                                u'id_str': u'672503263929999368', 
#                                u'retweet_count': 5, 
#                                u'in_reply_to_user_id': None, 
#                                u'favorited': False, 
#                                u'user': {u'follow_request_sent': None, 
#                                          u'profile_use_background_image': True, 
#                                          u'default_profile_image': False, 
#                                          u'id': 2943347056L, 
#                                          u'verified': False, 
#                                          u'profile_image_url_https': u'https://pbs.twimg.com/profile_images/666320860668633088/kgqYVPSV_normal.jpg', 
#                                          u'profile_sidebar_fill_color': u'000000', 
#                                          u'profile_text_color': u'000000', 
#                                          u'followers_count': 3423, 
#                                          u'profile_sidebar_border_color': u'000000',
#                                          u'id_str': u'2943347056', 
#                                          u'profile_background_color': u'4A913C', 
#                                          u'listed_count': 19, 
#                                          u'profile_background_image_url_https': u'https://pbs.twimg.com/profile_background_images/565396277974683648/ZEcas3UF.jpeg', 
#                                          u'utc_offset': 7200, 
#                                          u'statuses_count': 31637, 
#                                          u'description': u'I am a nobody...', 
#                                          u'friends_count': 4472, 
#                                          u'location': u'Ixopo ', 
#                                          u'profile_link_color': u'DD2E44', 
#                                          u'profile_image_url': u'http://pbs.twimg.com/profile_images/666320860668633088/kgqYVPSV_normal.jpg', 
#                                          u'following': None, 
#                                          u'geo_enabled': True, 
#                                          u'profile_background_image_url': u'http://pbs.twimg.com/profile_background_images/565396277974683648/ZEcas3UF.jpeg', 
#                                          u'name': u'Bonginkosi', 
#                                          u'lang': u'en', 
#                                          u'profile_background_tile': True, 
#                                          u'favourites_count': 10, u'screen_name': u'Makanya_BP', u'notifications': None, 
#                                          u'url': None, u'created_at': u'Sat Dec 27 05:17:21 +0000 2014', u'contributors_enabled': False, 
#                                          u'time_zone': u'Pretoria', u'protected': False, u'default_profile': False, u'is_translator': False}, 
#                               u'geo': None, 
#                               u'in_reply_to_user_id_str': None, 
#                               u'lang': u'en', u'created_at': u'Thu Dec 03 19:50:47 +0000 2015', 
#                               u'filter_level': u'low', u'in_reply_to_status_id_str': None, u'place': None
#                               }, 
#         u'user': {u'follow_request_sent': None, 
#                   u'profile_use_background_image': True, 
#                   u'default_profile_image': False, 
#                   u'id': 877419326, u'verified': False, 
#                   u'profile_image_url_https': u'https://pbs.twimg.com/profile_images/660039864944091136/ufMW3hPe_normal.jpg', 
#                   u'profile_sidebar_fill_color': u'DDEEF6', u'profile_text_color': u'333333', u'followers_count': 449, 
#                   u'profile_sidebar_border_color': u'FFFFFF', u'id_str': u'877419326', 
#                   u'profile_background_color': u'C0DEED', u'listed_count': 13, 
#                   u'profile_background_image_url_https': u'https://pbs.twimg.com/profile_background_images/452798759856918529/uIpHsbQS.jpeg', 
#                   u'utc_offset': None, u'statuses_count': 31498, 
#                   u'description': u'Lord of the Kraal || Ndimhle || Jurist || Writer || IG: @pat_lambz', 
#                   u'friends_count': 304, 
#                   u'location': u'Pretoria', 
#                   u'profile_link_color': u'0084B4', 
#                   u'profile_image_url': u'http://pbs.twimg.com/profile_images/660039864944091136/ufMW3hPe_normal.jpg', 
#                   u'following': None, u'geo_enabled': True, u'profile_banner_url': u'https://pbs.twimg.com/profile_banners/877419326/1446392676', 
#                   u'profile_background_image_url': u'http://pbs.twimg.com/profile_background_images/452798759856918529/uIpHsbQS.jpeg', 
#                   u'name': u'Wu-Gambino', 
#                   u'lang': u'en', 
#                   u'profile_background_tile': True, 
#                   u'favourites_count': 1625, 
#                   u'screen_name': u'GambuZitha', 
#                   u'notifications': None, 
#                   u'url': None, u'created_at': u'Sat Oct 13 09:20:52 +0000 2012', 
#                   u'contributors_enabled': False, u'time_zone': None, 
#                   u'protected': False, u'default_profile': False, u'is_translator': False
#                   }, 
#         u'geo': None, 
#         u'in_reply_to_user_id_str': None, 
#         u'lang': u'en', 
#         u'created_at': u'Thu Dec 03 20:18:52 +0000 2015', 
#         u'filter_level': u'low', 
#         u'in_reply_to_status_id_str': None, 
#         u'place': None
# }

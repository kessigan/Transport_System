from pymongo import MongoClient
import nltk
from nltk.corpus import stopwords
from collections import defaultdict
from nltk.tokenize import RegexpTokenizer
import collections
from collections import defaultdict
from time import gmtime, strftime, strptime
import pandas as pd
import datetime
import pytz
from email.utils import parsedate_tz, mktime_tz
import json
import generateGeneralJsonData


def convert(data):
    if isinstance(data, basestring):
        return str(data)
    elif isinstance(data, collections.Mapping):
        return dict(map(convert, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(convert, data))
    else:
        return data

def generateTwitterText():

    client = MongoClient()
    db = client.TweetsDB

    all_tweets = []

    all_cursor = db.tweetsDBCollection.find()
    for doc in all_cursor:
        paras = doc
        all_tweets.append(paras)

    tweet_list = []

    for i in range(len(all_tweets)):
        entry = all_tweets[i]
        tweet = entry['text']
        tweet_enc = tweet.encode('ascii', 'ignore')
        tweet_list.append(tweet_enc) 

    return tweet_list


def generateTableData():

    client = MongoClient()
    db = client.TweetsDB

    all_tweets = []

    all_cursor = db.tweetsDBCollection.find()
    for doc in all_cursor:
        paras = doc
        all_tweets.append(paras)

    tweet_list = []
#     range(100,-1,-1)
    for i in range(len(all_tweets)-1,0,-1):
    	table_row = []
        entry = all_tweets[i]
        tweet = entry['text']
        user_name = entry['screen_name']
        tweet_enc = tweet.encode('ascii', 'ignore')
        user_name_enc = user_name.encode('ascii', 'ignore')
        table_row.append(user_name_enc)
        table_row.append(tweet_enc)
        tweet_list.append(table_row) 


    return tweet_list


def generateLineChartData():

    client = MongoClient()
    db = client.TweetsDB

    all_tweets = []

    all_cursor = db.tweetsDBCollection.find()
    for doc in all_cursor:
        paras = doc
        all_tweets.append(paras)

    dates_list = []
    
    for i in range(len(all_tweets)):
#         Thu Dec 03 21:13:55 +0000 2015
        
        table_row = []
        entry = all_tweets[i]
        date_entr = entry['created_at']
        date_entr_enc = convert(date_entr)
#         dt = datetime.datetime.fromtimestamp(date_entr_enc, pytz.timezone('Africa/Johannesburg'))
#         print dt
        timestamp = mktime_tz(parsedate_tz(date_entr_enc))
        s = str(datetime.datetime.fromtimestamp(timestamp))
        s1 = datetime.datetime.strptime(s, "%Y-%m-%d %H:%M:%S")
#         print ("after", s)
#         date_entr_enc = date_entr_enc[:20] + date_entr_enc[25:]
        
#         new_datetime_entry =  datetime.datetime.strptime(date_entr_enc, "%a %b %d %H:%M:%S %Y")
#         new_datetime_entry_str =  datetime.datetime.strftime(new_datetime_entry, "%Y-%m-%d %H:%M:%S")
# #         print ("the one", new_datetime_entry_str)
#         new_datetime_entry_str = new_datetime_entry_str[:-3]
        s_str = s[:-3]

        new_date = date_entr[:16] + " " + date_entr[20:]

#         dates_list.append(new_datetime_entry_str)
        dates_list.append(s_str)
    

    d = defaultdict(int)
    for date in dates_list:
        d[date] += 1
     
    freq_count = d.items() 
    
    freq_count_enc = freq_count
    
    freq_count_enc = convert(freq_count)
    
    freq_count_enc.sort()

    
    timeline_format_data = []
    for inf in freq_count_enc:
        row_dict = {}
        row_dict["date"] = inf[0]
        row_dict["visits"] = inf[1]
        timeline_format_data.append(row_dict)
    
    
    
    
    return timeline_format_data 

def generateMapData():

    client = MongoClient()
    db = client.TweetsDB

    all_tweets = []

    all_cursor = db.tweetsDBCollection.find()
    for doc in all_cursor:
        paras = doc
        all_tweets.append(paras)

    dates_list = []
    
    long_lat_values = []
    for i in range(len(all_tweets)):
#         Thu Dec 03 21:13:55 +0000 2015
        long_lat_dict = {}
        table_row = []
        entry = all_tweets[i]
        date_entr = entry['coordinates']
        if date_entr != None:
            long_lat_dict["lat"] = date_entr['coordinates'][0]
            long_lat_dict["long"] = date_entr['coordinates'][1]
#             long_lat_dict["text"] = entry['text']
#             long_lat_dict["screen_name"] = entry['screen_name']
            long_lat_values.append(long_lat_dict)    
    
    
    return long_lat_values 

def getKeyWordsTalk(tweet): 
    dec_8_morning_plenary_session = ["Phil", "Mjwara", "Naledi", "Pandor", "Opening", "address", 
                             "Keynote", "message", "Nkosazana", "Dlamini-Zuma", "Special", "address", "Koji", "Omi",
                             "Prof Gordon McBean", "Heide Hackmann", "Jean-Claude Burgelman", "Forum", "lecture",
                             "Vote", "on", "behalf", "of", "participants", "Vote", "thanks"]
    dec_8_morning_plenary_session1 = []
    for dec in dec_8_morning_plenary_session:
        dec_8_morning_plenary_session1.append(dec.lower())
     
    dec_8_after_tea_plenary_session = ["Plenary", "panel", "discussion", "Science", "Technology", "Innovation", "Response", "Climate", "Change", "COP-21", "comes",  "Pretoria", 
                              "Cheryl", "de","la", "Rey", "Introductory", "lecture", "Bob", "Scholes",
                             "Tanya" ,"Abrahamse", "Ulla", "Engelmann", "Sir", "Peter", "Gluckman", "Arun", "Kulshreshtha",
                             "Dr", "Pavel", "Kabat", "Crain", "Soudien", "Gordon", "McBean"]
    dec_8_after_tea_plenary_session1 = []
    for dec in dec_8_after_tea_plenary_session:
        dec_8_after_tea_plenary_session1.append(dec.lower())
     
    dec_8_first_cycle_1_key_words = ["Responding",  "Societal", "Challenges", "Science", "Cities", "Urbanisation", "Philip", "Harrison", "Geci", "Karuri-Sebina", "Elsona" "Van" "Huyssteen"] 
    dec_8_first_cycle_1_key_words1 = []
    for dec in dec_8_first_cycle_1_key_words:
        dec_8_first_cycle_1_key_words1.append(dec.lower())
    
    dec_8_first_cycle_2_key_words = ["Skills", "Knowledge", "Economy", "Non", "Traditional", "STI", "Partnerships", "Women",  "Stem", "Philanthropy", "Nkosazana", "Dlamini-Zuma", "Savannah", "Maziya", "Precious", "Moloi-Motsepe", "Bhekinkosi", "Moyo"]
    dec_8_first_cycle_2_key_words1 = []
    for dec in dec_8_first_cycle_2_key_words:
        dec_8_first_cycle_2_key_words1.append(dec.lower())
    
    dec_8_first_cycle_3_key_words = ["Showcasing", "South", "African", "Science", "Palaeosciences", "Powerful", "Outreach", "Tool", "Social", "Cohesion", "Environmental", "Conservation", "Palaeosciences", "Powerful", "Outreach", "Tool", "Robert", "Blumenschine", "Sinethemba", "Foba", "Andrea", "Leenen", "Sandile", "Matsheni", "Sibongiseni", "Ntshebe"]
    dec_8_first_cycle_3_key_words1 = []
    for dec in dec_8_first_cycle_3_key_words:
        dec_8_first_cycle_3_key_words1.append(dec.lower())
    
    dec_8_first_cycle_4_key_words = ["African", "Eyes", "Sky", "Space", "Science", "Responding", "Society's", "Needs", "Sandile", "Malinga", "Stuart", "Martin", "Humbulani", "Mudau", "Patrick", "Ndhlovu", "Jane", "Olwoch", "Lerato", "Senoko", "Robert", "van", "Zyl"]
    dec_8_first_cycle_4_key_words1 = []
    for dec in dec_8_first_cycle_4_key_words:
        dec_8_first_cycle_4_key_words1.append(dec.lower())
    
    dec_8_first_cycle_5_key_words = ["Science", "Agenda", "Africa", "Creatively", "Destroying", "Africa", "Rethinking", "Inclusion", "Integration", "Sustainable", "Development", "Technology","Innovation", "Bitrina", "Diyamett", "Jelel", "Ezzine", "Frank", "Lekaba", "Erika", "Kraemer", "Mbula", "Liepollo", "Lebohang", "Pheko"]
    dec_8_first_cycle_5_key_words1 = []
    for dec in dec_8_first_cycle_5_key_words:
        dec_8_first_cycle_5_key_words1.append(dec.lower())
    
    dec_8_first_cycle_6_key_words = ["Science",  "Society", "Conversation", "Systems", "Analysis", "Government", "Planning",  "Pavel" "Kabat", "Mary", "Scholes", "Ruth", "Stewart", "Harsha", "Dayal"]
    dec_8_first_cycle_6_key_words1 =[]
    for dec in dec_8_first_cycle_6_key_words:
        dec_8_first_cycle_6_key_words1.append(dec.lower())
    
    dec_8_first_cycle_7_key_words = ["Science", "Indaba", "Science", "Centres",  "Outreach", "Programs", "Tandem", "Development", "People",  "Programs", "Science", "Centres", "Outreach", "Programs", "Tandem", "Development", "People", "Programs", "Graham", "Walker", "Leapotswe", "Bantsi", "MJ", "Schwartz", "Michael", "Ellis"] 
    dec_8_first_cycle_7_key_words1 = []
    for dec in dec_8_first_cycle_7_key_words:
        dec_8_first_cycle_7_key_words1.append(dec.lower())
    
    dec_8_first_cycle_8_key_words = ["Science", "Indaba", "II", "Preparing",  "Careers", "Exist", "Yet", "Yasuo", "Kishimoto", "Romilla", "Maharaj", "Daisuke", "Mizoguchi", "Romain", "Murenzi", "Masafumi", "Nagao"]   
    dec_8_first_cycle_8_key_words1 = []
    for dec in dec_8_first_cycle_8_key_words:
        dec_8_first_cycle_8_key_words1.append(dec.lower())
    
    dec_8_second_cycle_1_key_words = ["Biophysics", "Underpins", "BioDesign", "Vibrant", "Bioeconomy", "Musa", "Mhlanga","William","Rae"] 
    dec_8_second_cycle_1_key_words1 =  []
    for dec in dec_8_second_cycle_1_key_words:
        dec_8_second_cycle_1_key_words1.append(dec.lower())
    
    dec_8_second_cycle_2_key_words = ["MOOCS", "Challenges", "Opportunities", "Education", 'Africa', "Rumbidzai", "Chindanya", "Bernie", "Fanaroff", "Mamadou", "Lamine", "Ndiaye", "Rachel", "Prinsloo"]
    dec_8_second_cycle_2_key_words1 =  []
    for dec in dec_8_second_cycle_2_key_words:
        dec_8_second_cycle_2_key_words1.append(dec.lower())
    
    dec_8_second_cycle_3_key_words = ["Fast", "3D", "Printing", "Metal", "Parts", "Aerospace", "Medical", "Nomfuneko", "Majaja", "Michael", "Serapelo", "Michele", "Truscott", "Marius", "Vermeulen", "George", "Vicatos"]
    dec_8_second_cycle_3_key_words1 =  []
    for dec in dec_8_second_cycle_3_key_words:
        dec_8_second_cycle_3_key_words1.append(dec.lower())
    
    dec_8_second_cycle_4_key_words = ["Exploring", "Exciting", "Potential", "BRICS", "Partnership", "Astronomy", "Hugo", "Barbosa", "Yashwant", "Gupta", "Sergey", "Salikhov", "Xue", "Suijian", "Ted", "Williams"]
    dec_8_second_cycle_4_key_words1 =  []
    for dec in dec_8_second_cycle_4_key_words:
        dec_8_second_cycle_4_key_words1.append(dec.lower())
    
    dec_8_second_cycle_5_key_words = ["Next", "Einstein", 'Initiative', "Transforming", "African", "Thokozani", "Majozi", "Tolu", "Oni", "Janusz", "Paweska", "Alta", "Schutte", "Arun", "Sharma"]
    dec_8_second_cycle_5_key_words1 =  []
    for dec in dec_8_second_cycle_5_key_words:
        dec_8_second_cycle_5_key_words1.append(dec.lower())
    
    dec_8_second_cycle_6_key_words = ["International", "Partnership", "Government", "Science", 'Advice', "Julie", "Maxton", "Romain", "Murenzi", "Daya", "Reddy"]
    dec_8_second_cycle_6_key_words1 =  []
    for dec in dec_8_second_cycle_6_key_words:
        dec_8_second_cycle_6_key_words1.append(dec.lower())
    
    dec_8_second_cycle_7_key_words = ["Climate", "Change", "Unique", "Regional", "Earth", "System", "Luthando", "Dziba", "Francois", "Engelbrecht", "Xolisa", "Ngwadla", "Andrea", "Rother", "Bob", "Scholes", "Stephan", "Woodborne"] 
    dec_8_second_cycle_7_key_words1 =  []
    for dec in dec_8_second_cycle_7_key_words:
        dec_8_second_cycle_7_key_words1.append(dec.lower())
    
    dec_8_second_cycle_8_key_words = ["Governing", "Science", "Technology", "Innovation", "Secure", "Sustainable", "Development", "Goals", "SDGS", "Dialogues", "Practical", "Actions","Bitrina", "Diyamett", "Felix", "Xavier", "Estico", "Erika", "Kraemer-Mbula", "Philippe", "Mawoko", "Mammo", "Muchie", "Segomotso", "Tire", "Godber", "Tumushabe"]
    dec_8_second_cycle_8_key_words1 =  []
    for dec in dec_8_second_cycle_8_key_words:
        dec_8_second_cycle_8_key_words1.append(dec.lower())

    count_all_dict = {}
    count_all_dict["dec_8_morning_plenary_session"] = 0
    count_all_dict["dec_8_after_tea_plenary_session"] = 0
    
    count_all_dict["dec_8_first_cycle_1_key_words"] = 0
    count_all_dict["dec_8_first_cycle_2_key_words"] = 0
    count_all_dict["dec_8_first_cycle_3_key_words"] = 0
    count_all_dict["dec_8_first_cycle_4_key_words"] = 0
    count_all_dict["dec_8_first_cycle_5_key_words"] = 0
    count_all_dict["dec_8_first_cycle_6_key_words"] = 0
    count_all_dict["dec_8_first_cycle_7_key_words"] = 0
    count_all_dict["dec_8_first_cycle_8_key_words"] = 0
    
    count_all_dict["dec_8_second_cycle_1_key_words"] = 0
    count_all_dict["dec_8_second_cycle_2_key_words"] = 0
    count_all_dict["dec_8_second_cycle_3_key_words"] = 0
    count_all_dict["dec_8_second_cycle_4_key_words"] = 0
    count_all_dict["dec_8_second_cycle_5_key_words"] = 0
    count_all_dict["dec_8_second_cycle_6_key_words"] = 0
    count_all_dict["dec_8_second_cycle_7_key_words"] = 0
    count_all_dict["dec_8_second_cycle_8_key_words"] = 0
    
    tokenizer = RegexpTokenizer(r'\w+') 
    tweet_tokens = tokenizer.tokenize(tweet)
    
#     print dec_8_first_cycle_2_key_words1
    
         
    for tweet_token in tweet_tokens:
#         print tweet_token.lower()
        if tweet_token.lower() in dec_8_morning_plenary_session1:
            count_all_dict["dec_8_morning_plenary_session"] = count_all_dict["dec_8_morning_plenary_session"] + 1
        if tweet_token.lower() in dec_8_after_tea_plenary_session:
            count_all_dict["dec_8_after_tea_plenary_session"] = count_all_dict["dec_8_after_tea_plenary_session"] + 1
    
        if tweet_token.lower() in dec_8_first_cycle_1_key_words1:
            count_all_dict["dec_8_first_cycle_1_key_words"] = count_all_dict["dec_8_first_cycle_1_key_words"] + 1
        if tweet_token.lower() in dec_8_first_cycle_2_key_words1:
            count_all_dict["dec_8_first_cycle_2_key_words"] = count_all_dict["dec_8_first_cycle_2_key_words"] + 1
        if tweet_token.lower() in dec_8_first_cycle_3_key_words1:
            count_all_dict["dec_8_first_cycle_3_key_words"] = count_all_dict["dec_8_first_cycle_3_key_words"] + 1
        if tweet_token.lower() in dec_8_first_cycle_4_key_words1:
            count_all_dict["dec_8_first_cycle_4_key_words"] = count_all_dict["dec_8_first_cycle_4_key_words"] + 1
        if tweet_token.lower() in dec_8_first_cycle_5_key_words1:
            count_all_dict["dec_8_first_cycle_5_key_words"] = count_all_dict["dec_8_first_cycle_5_key_words"] + 1
        if tweet_token.lower() in dec_8_first_cycle_6_key_words1:
            count_all_dict["dec_8_first_cycle_6_key_words"] = count_all_dict["dec_8_first_cycle_6_key_words"] + 1
        if tweet_token.lower() in dec_8_first_cycle_1_key_words1:
            count_all_dict["dec_8_first_cycle_7_key_words"] = count_all_dict["dec_8_first_cycle_7_key_words"] + 1
        if tweet_token.lower() in dec_8_first_cycle_1_key_words1:
            count_all_dict["dec_8_first_cycle_8_key_words"] = count_all_dict["dec_8_first_cycle_8_key_words"] + 1
            
        if tweet_token.lower() in dec_8_second_cycle_1_key_words1:
            count_all_dict["dec_8_second_cycle_1_key_words"] = count_all_dict["dec_8_second_cycle_1_key_words"] + 1
        if tweet_token.lower() in dec_8_second_cycle_2_key_words1:
            count_all_dict["dec_8_second_cycle_2_key_words"] = count_all_dict["dec_8_second_cycle_2_key_words"] + 1
        if tweet_token.lower() in dec_8_second_cycle_3_key_words1:
            count_all_dict["dec_8_second_cycle_3_key_words"] = count_all_dict["dec_8_second_cycle_3_key_words"] + 1
        if tweet_token.lower() in dec_8_second_cycle_4_key_words1:
            count_all_dict["dec_8_second_cycle_4_key_words"] = count_all_dict["dec_8_second_cycle_4_key_words"] + 1
        if tweet_token.lower() in dec_8_second_cycle_5_key_words1:
            count_all_dict["dec_8_second_cycle_5_key_words"] = count_all_dict["dec_8_second_cycle_5_key_words"] + 1
        if tweet_token.lower() in dec_8_second_cycle_6_key_words1:
            count_all_dict["dec_8_second_cycle_6_key_words"] = count_all_dict["dec_8_second_cycle_6_key_words"] + 1
        if tweet_token.lower() in dec_8_second_cycle_7_key_words1:
            count_all_dict["dec_8_second_cycle_7_key_words"] = count_all_dict["dec_8_second_cycle_7_key_words"] + 1
        if tweet_token.lower() in dec_8_second_cycle_8_key_words1:
            count_all_dict["dec_8_second_cycle_8_key_words"] = count_all_dict["dec_8_second_cycle_8_key_words"] + 1
        
    return count_all_dict
#         sort_keys = sorted(count_all_dict, key=count_all_dict.get, reverse=True)
#         print sort_keys
            
            
        
    
    
#     tokenizer = RegexpTokenizer(r'\w+') 
#     tweet_tokens = tokenizer.tokenize(tweet)
# 
#     count_dec_8_morning_plenary_session = 0
#     for tweet_token in tweet_tokens:
#         if tweet_token in dec_8_morning_plenary_session:
#             count_dec_8_morning_plenary_session = count_dec_8_morning_plenary_session + 1
#             
#     count_dec_8_after_tea_plenary_session = 0
#     for tweet_token in tweet_tokens:
#         if tweet_token in dec_8_after_tea_plenary_session:
#             count_dec_8_after_tea_plenary_session = count_dec_8_after_tea_plenary_session + 1
#             
#     count_dec_8_dec_8_first_cycle = []
#     for i in range(0,7):
#         count_dec_8_dec_8_first_cycle.append(0)
#       
#     for tweet_token in tweet_tokens:
#         if tweet_token in dec_8_first_cycle_1_key_words:
#             count_dec_8_dec_8_first_cycle[0] = count_dec_8_dec_8_first_cycle[0] + 1
#         if tweet_token in dec_8_first_cycle_2_key_words:
#             count_dec_8_dec_8_first_cycle[1] = count_dec_8_dec_8_first_cycle[1] + 1
#         if tweet_token in dec_8_first_cycle_3_key_words:
#             count_dec_8_dec_8_first_cycle[2] = count_dec_8_dec_8_first_cycle[2] + 1
#         if tweet_token in dec_8_first_cycle_4_key_words:
#             count_dec_8_dec_8_first_cycle[3] = count_dec_8_dec_8_first_cycle[3] + 1
#         if tweet_token in dec_8_first_cycle_5_key_words:
#             count_dec_8_dec_8_first_cycle[4] = count_dec_8_dec_8_first_cycle[4] + 1
#         if tweet_token in dec_8_first_cycle_6_key_words:
#             count_dec_8_dec_8_first_cycle[5] = count_dec_8_dec_8_first_cycle[5] + 1
#         if tweet_token in dec_8_first_cycle_7_key_words:
#             count_dec_8_dec_8_first_cycle[6] = count_dec_8_dec_8_first_cycle[6] + 1
#         if tweet_token in dec_8_first_cycle_8_key_words:
#             count_dec_8_dec_8_first_cycle[7] = count_dec_8_dec_8_first_cycle[7] + 1
#             
# #     max_count_dec_8_dec_8_first_cycle = max(count_dec_8_dec_8_first_cycle)
# #     print max_count_dec_8_dec_8_first_cycle
#     
#     m = max(count_dec_8_dec_8_first_cycle)
#     max_count_dec_8_dec_8_first_cycle = [i for i, j in enumerate(count_dec_8_dec_8_first_cycle) if j == m]
#     
#     
#     all_count_max = []
#     all_count_max.append(count_dec_8_morning_plenary_session)   
#     all_count_max.append(count_dec_8_after_tea_plenary_session)  
#  
#     all_count_max.append(m)
#     
#     
#     m_fin = max(all_count_max)
#     max_count_final = [i for i, j in enumerate(all_count_max) if j == m_fin]
#     final_max_index = max_count_final[0]  
#     
#     session = ""
#     if final_max_index == 0:
#         session = "morning_plenary_session"
#     elif final_max_index == 1:
#         session = "tea_plenary_session"
#     elif final_max_index == 2:
#         if max_count_dec_8_dec_8_first_cycle[0] == 0:
#             session = "The Science of Cities and Urbanisation"
#         elif max_count_dec_8_dec_8_first_cycle[0] == 1:
#             session = "Non traditional STI Partnerships: Women in Stem and Philanthropy"
#         elif max_count_dec_8_dec_8_first_cycle[0] == 2:
#             session = "The Palaeosciences as a Powerful Outreach Tool for Social Cohesion and Environmental Conservation"
#         elif max_count_dec_8_dec_8_first_cycle[0] == 3:
#             session = "Space Science Responding to Society's needs"
#         elif max_count_dec_8_dec_8_first_cycle[0] == 4:
#             session = "Creatively Destroying Africa: Rethinking Inclusion, Integration, and Sustainable Development Through Science, Technology and Innovation"
#         elif max_count_dec_8_dec_8_first_cycle[0] == 5:
#             session = "Systems Analysis for Government Planning"
#         elif max_count_dec_8_dec_8_first_cycle[0] == 6:
#             session = "Science Centres and Outreach Programs: Tandem Development of People and Programs"
#         elif max_count_dec_8_dec_8_first_cycle[0] == 7:
#             session = "Preparing for Careers that Do Not Exist Yet"
#         
#     print session
#     print "key word talk"


def getWordColour(i):

	if i > 34:
		i = 15
	colours = [ "#660066", "#FF0066", "#006699", "#0066CC", "#00FFCC", "#6633CC", "#9966CC",
                "#FF00CC", "#787878 ", "#ff7d69", "#778899", "#CD853F", "#BA55D3", "#000080",
                "#FF6347", "#87CEEB", "#FFA500", "#FF4500", "#FF0000", "#008080", "#00FFFF", 
                "#011d01", "#003300", "#330000", "#333300", "#660000", "#663300", "#993300", 
                "#000033", "#003333", "#330033", "#333333", "#CC0033", "#003366", "#333366"  
                ] 
    
	
	colour = colours[i]

	return colour

def getStopWordsArray():
    stop = stopwords.words('english')
    str_fullstop = '.'
    str_bracket = '(' 
    str_close_bracket = ')'
    str_comma = ','
    str_colon = ':'
    str_semi_colon = ';'
    str_hyphen = '-'
    str_question = '?'
    str_s = '\'s'
    str_percent = '%'
    url_word ='https'
    retweet_word = 'rt'
     
    stop.append(str_fullstop.decode('utf-8'))
    stop.append(str_bracket.decode('utf-8'))
    stop.append(str_close_bracket.decode('utf-8'))
    stop.append(str_comma.decode('utf-8'))
    stop.append(str_colon.decode('utf-8'))
    stop.append(str_hyphen.decode('utf-8'))
    stop.append(str_question.decode('utf-8'))
    stop.append(str_s.decode('utf-8'))
    stop.append(str_percent.decode('utf-8'))
    stop.append(str_semi_colon.decode('utf-8'))
    stop.append(url_word.decode('utf-8'))
    stop.append(retweet_word.decode('utf-8'))
    
    return stop

def CleanWordCloudData(all_paragraphs):
    stop = getStopWordsArray()
    tokenizer = RegexpTokenizer(r'\w+')
    
    all_words = []
    for par in all_paragraphs:
    	tokens = tokenizer.tokenize(par)
    	# tokens = nltk.word_tokenize(par)
         
        #save all words for use in finding the frequencty distibutions
        for str_tok in tokens:
            #make all words lower case to allow for easy comparisons
            str_tok_1 = str_tok.lower()
            if str_tok_1 not in stop:
                if str_tok_1.isdigit() != True: 
                    if len(str_tok_1) > 2:
                        all_words.append(str_tok_1)
                    
    return all_words

def wordCloudData(all_words):

#     d = defaultdict(int)
#     for word in all_words:
#         d[word] += 1
#      
#     freq_count = d.items() 
#     
#     text_and_size = []
#     
#     for item in freq_count:
#     	text_and_size.append(item)
        
    
    text_and_size = []
    fdist2 = nltk.FreqDist(all_words)
    num_of_common = 16
    for un in fdist2.most_common(num_of_common):
        text_and_size.append( (un[0], un[1]) )
     
    #MAKE A LIST OF THE NUMBER OF TIMES THE WORDS OCCUR
    freq_sizes = []
    for friq in text_and_size:
        freq_sizes.append(friq[1])
     
    total = sum(int(x) for x in freq_sizes)

        
    #MAP THE NUMBER OF OCCURENCES OF A WORD TO A VAKUE THAT WILL BE EASY TO PLOT ON THE CURRENT WORD CLOUD VISUALISATION USED    
#     new_freq_sizes = calculateWordSize(freq_sizes)
    
    #REPLACE THE OLD UNMAPPED SIZES WITH SIZES THAT CAN BE VISIBLE ON THE PLOT
    text_and_size_mod = []
    for i in text_and_size:
        new_freq_size = calculateWordSizeOne(i[1],total)
        text_and_size_mod.append((i[0],new_freq_size,i[1]))
      
    #MAKE A LIST OF DICTIONARIES WITH WORD, SIZE AND FREQUENCY AND PARAGRAPHS WHERE WORD APPEARS FOR THE WORD CLOUD                                     
    all_common_lis_word = []
    count = 0
    for i in text_and_size_mod:
        topic_word_dict = {}
        topic_word_dict["text"] = i[0] 
        topic_word_dict["size"] = i[1]
        topic_word_dict["freq"] = i[2]
        topic_word_dict["colour"] = getWordColour(count)
        count+=1 #get the colour depending on the position of the word in unique topics because the getWordColour function is linked to how findWordToHighlight works
        
        all_common_lis_word.append(topic_word_dict)
    
    return all_common_lis_word


def calculateWordSizeOne(freq,total):
      
  
    percenta = freq/float(total)*100
    
    if percenta >= 0 and  percenta < 2:
        size = 10
    elif percenta >= 2 and  percenta < 4:
        size = 20
    elif percenta >= 4 and  percenta < 6:
        size = 28
    elif percenta >= 6 and  percenta < 8:
        size = 34
    elif percenta >= 8 and  percenta < 10:
        size = 45
    elif percenta >= 10 and  percenta < 12:
        size = 55
    elif percenta >= 12 and  percenta < 14:
        size = 60
    elif percenta >= 14 and  percenta < 16:
        size = 62
    elif percenta >= 16 and  percenta < 18:
        size = 65
    elif percenta >= 18 and  percenta < 20:
        size = 65
    elif percenta >= 20 and  percenta < 30:
        size = 70
    elif percenta >= 30 and  percenta < 40:
        size = 70
    elif percenta >= 40 and  percenta < 50:
        size = 80
    elif percenta >= 50 and  percenta < 60:
        size = 80
    elif percenta >= 60 and  percenta < 70:
        size = 80
    elif percenta >= 70 and  percenta < 80:
        size = 90
    elif percenta >= 80 and  percenta < 90:
        size = 90
    elif percenta >= 90 and  percenta < 101:
        size = 90
        
    
    return size


def calculateWordSize(freqs_arr):
    
    sizes = []
    total = sum(freqs_arr)
    
    for feq in freqs_arr:
        percenta = feq/float(total)*100
        
        if percenta >= 0 and  percenta < 2:
            size = 10
        elif percenta >= 2 and  percenta < 4:
            size = 20
        elif percenta >= 4 and  percenta < 6:
            size = 28
        elif percenta >= 6 and  percenta < 8:
            size = 34
        elif percenta >= 8 and  percenta < 10:
            size = 45
        elif percenta >= 10 and  percenta < 12:
            size = 55
        elif percenta >= 12 and  percenta < 14:
            size = 60
        elif percenta >= 14 and  percenta < 16:
            size = 62
        elif percenta >= 16 and  percenta < 18:
            size = 65
        elif percenta >= 18 and  percenta < 20:
            size = 65
        elif percenta >= 20 and  percenta < 30:
            size = 70
        elif percenta >= 30 and  percenta < 40:
            size = 70
        elif percenta >= 40 and  percenta < 50:
            size = 80
        elif percenta >= 50 and  percenta < 60:
            size = 80
        elif percenta >= 60 and  percenta < 70:
            size = 80
        elif percenta >= 70 and  percenta < 80:
            size = 90
        elif percenta >= 80 and  percenta < 90:
            size = 90
        elif percenta >= 90 and  percenta < 101:
            size = 90
        
        sizes.append(size)
    
    return sizes    



def getFirstDayFirstPartTreeMapData(dict_all):
#     categories_first_cycle = [
#                     "Plenary Session",
#                     "Second Plenary Session",
#                     "Responding to Societal Challenges: The Science of Cities and Urbanisation",
#                     "Skills for the Knowledge Economy: Non traditional STI Partnerships: Women in Stem and Philanthropy", 
#                     "Showcasing South African Science: The Palaeosciences as a Powerful Outreach Tool for Social Cohesion and Environmental Conservation",
#                     "African Eyes on the Sky: Space Science Responding to Society's needs",
#                     "Science Agenda for Africa: Creatively Destroying Africa: Rethinking Inclusion, Integration, and Sustainable Development Through Science, Technology and Innovation",
#                     "Science and Society Conversation: Systems Analysis for Government Planning",
#                     "Science Indaba I: Science Centres and Outreach Programs: Tandem Development of People and Programs",
#                     "Science Indaba II: Preparing for Careers that Do Not Exist Yet"
#                     ]
    categories_first_cycle = [
                    "Plenary Session",
                    "Second Plenary Session",
                    "The Science of Cities and Urbanisation",
                    "Non traditional STI Partnerships: Women in Stem and Philanthropy", 
                    "The Palaeosciences as a Powerful Outreach Tool for Social Cohesion and Environmental Conservation",
                    "Space Science Responding to Society's needs",
                    "Creatively Destroying Africa: Rethinking Inclusion, Integration, and Sustainable Development Through Science, Technology and Innovation",
                    "Systems Analysis for Government Planning",
                    "Science Centres and Outreach Programs: Tandem Development of People and Programs",
                    "Preparing for Careers that Do Not Exist Yet"
                    ]
         
    category_first_sizes = [    dict_all["dec_8_morning_plenary_session"],
                                    dict_all["dec_8_after_tea_plenary_session"],
                                    dict_all["dec_8_first_cycle_1_key_words"],
                                    dict_all["dec_8_first_cycle_2_key_words"],
                                    dict_all["dec_8_first_cycle_3_key_words"],
                                    dict_all["dec_8_first_cycle_4_key_words"],
                                    dict_all["dec_8_first_cycle_5_key_words"],
                                    dict_all["dec_8_first_cycle_6_key_words"],
                                    dict_all["dec_8_first_cycle_7_key_words"],
                                    dict_all["dec_8_first_cycle_8_key_words"]
                                ]
         
         
    js_data1 = generateGeneralJsonData.generatingJsonData(categories_first_cycle,category_first_sizes)
    
    return js_data1


def getFirstDaySecondPartTreeMapData(dict_all):
    categories_second_cycle = [
                    "Biophysics Underpins BioDesign and a Vibrant Bioeconomy",
                    "MOOCS: Challenges and Opportunities for Education in Africa", 
                    "Fast 3D Printing of Metal Parts For Aerospace and Medical: A First for Africa",
                    "Exploring the Exciting Potential for BRICS Partnership in Astronomy",
                    "Next Einstein Initiative: Transforming African Science",
                    "International Partnership for Government Science Advice",
                    "Science Centres and Outreach Programs: Climate Change and an Unique Regional Earth System",
                    "Governing Science,Technology and Innovation to Secure Sustainable Development Goals (SDGS) in Africa - From Dialogues to Practical Actions"
                    ]
         
    category_second_sizes = [        dict_all["dec_8_second_cycle_1_key_words"],
                                    dict_all["dec_8_second_cycle_2_key_words"],
                                    dict_all["dec_8_second_cycle_3_key_words"],
                                    dict_all["dec_8_second_cycle_4_key_words"],
                                    dict_all["dec_8_second_cycle_5_key_words"],
                                    dict_all["dec_8_second_cycle_6_key_words"],
                                    dict_all["dec_8_second_cycle_7_key_words"],
                                    dict_all["dec_8_second_cycle_8_key_words"]
                                ]
         
         
    js_data1 = generateGeneralJsonData.generatingJsonData(categories_second_cycle,category_second_sizes)
    
    return js_data1
            
         
# def getTreeMapDataFirstCycle():
#     categories_first_cycle = [
#                     "The Science of Cities and Urbanisation", 
#                     "Non traditional STI Partnerships: Women in Stem and Philanthropy",   
#                     "The Palaeosciences as a Powerful Outreach Tool for Social Cohesion and Environmental Conservation",
#                     "Space Science Responding to Society's needs",
#                     "Creatively Destroying Africa: Rethinking Inclusion, Integration, and Sustainable Development Through Science, Technology and Innovation",
#                     "Systems Analysis for Government Planning",
#                     "Science Centres and Outreach Programs: Tandem Development of People and Programs",
#                     "Preparing for Careers that Do Not Exist Yet"
#                     ]
#     category_first_sizes = [50,50,50,50,50,50,50,50]
#     
# 
#     js_data1 = generateGeneralJsonData.generatingJsonData(categories_first_cycle,category_first_sizes)
# #     json_data=open('TwitterDashboard/static/twitterGeneralDataFirstCycle.json').read()
# #     js_data = json.loads(json_data)
# #     #convert json data from unicode back to strings
# #     js_data1 = convert(js_data)
#     
#     return js_data1
# 
# def getTreeMapDataSecondCycle(): 
#     categories_second_cycle = [ "Biophysics Underpins BioDesign and a Vibrant Bioeconomy",
#                                 "MOOCS: Challenges and Opportunities for Education in Africa",
#                                 "Fast 3D Printing of Metal Parts For Aerospace and Medical: A First for Africa",
#                                 "Exploring the Exciting Potential for BRICS Partnership in Astronomy",
#                                 "Next Einstein Initiative: Transforming African Science",
#                                 "International Partnership for Government Science Advice",
#                                 "Climate Change and an Unique Regional Earth System",
#                                 "Governing Science, Technology and Innovation to Secure Sustainable Development Goals (SDGS) in Africa - From Dialogues to Practical Actions"
#                         ]
#     
#     category_second_sizes = [50,50,50,50,50,50,50,50]
#     
#     js_data1 = generateGeneralJsonData.generatingJsonData(categories_second_cycle,category_second_sizes)
# #     json_data=open('TwitterDashboard/static/twitterGeneralDataSecondCycle.json').read()
# #     js_data = json.loads(json_data)
# #     #convert json data from unicode back to strings
# #     js_data1 = convert(js_data)
#     
#     
#     return js_data1

# getKeyWordsTalk("Skills for the Knowledge Economy: Open Data in a Big Data World @ICSUnews @CODATANews at #SFSA2015 Wed.9 Dec 11am https://t.co/dOl8Zjo1OA")
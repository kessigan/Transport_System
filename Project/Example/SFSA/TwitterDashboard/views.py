from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from pymongo import MongoClient
import data_conversion
import nltk
from collections import Counter


def dashBoard(request):

    context = RequestContext(request)
    tweet_list = []
    table_data = []
    
    tweet_list = data_conversion.generateTwitterText()
    
    first_block_num_tweets = len(tweet_list)
    
    word_list = data_conversion.CleanWordCloudData(tweet_list)
    
    final_list =  data_conversion.wordCloudData(word_list)

    second_block_common_word_most_dict = {}

    if len(final_list)>0:  
        second_block_common_word_most_dict = {}
        second_block_common_word_most_dict["text"] = final_list[0]["text"]
        second_block_common_word_most_dict["freq"] = final_list[0]["freq"]
    else:
        second_block_common_word_most = {}
        second_block_common_word_most_dict["text"] = "No tweets yet"
        second_block_common_word_most_dict["freq"] = 0
    
    table_data = data_conversion.generateTableData()
    
    twitter_users = []
    for row in table_data:
        twitter_users.append(row[0])
        
    fdist2 = nltk.FreqDist(twitter_users)
    num_of_common = 1
    third_block_common_tweeter_dict = {}
    for un in fdist2.most_common(num_of_common):
        third_block_common_tweeter_dict['tweeter'] = un[0]
        third_block_common_tweeter_dict['num'] = un[1]
            
    time_chart_data = data_conversion.generateLineChartData()
    
    # data_conversion.generateMapData()
    
    #get the 
    all_dict_list = []
    for un in table_data:
        one_dict_tot = data_conversion.getKeyWordsTalk(un[1])
        all_dict_list.append(one_dict_tot)
        
      
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
      
    first = Counter(count_all_dict)
    ans = Counter(count_all_dict)
    for single_dict in all_dict_list:
        second = Counter(single_dict)
        ans = ans + second
        
    js_data1 = data_conversion.getFirstDayFirstPartTreeMapData(ans)
    js_data2 = data_conversion.getFirstDaySecondPartTreeMapData(ans)
        
#     js_data2 = []
    return render_to_response("index_new.html", {"data_list" : final_list, "table_data" : table_data, "time_chart_data":time_chart_data, "first_block_num_tweets":[first_block_num_tweets], "second_block_common_word_most_dict":second_block_common_word_most_dict, "third_block_common_tweeter_dict":third_block_common_tweeter_dict, "js_data1": js_data1, "js_data2": js_data2} , context)


#Use the user defined list/search terms  to produce json data for the treemap
import json

def generatingJsonData(category_list,cat_sizes):
    
    print "generating general json data"
 
    #combines all the data into one big json object
    dataJson = {
                    "name": "Science Forum 2015",
                    "children": children(category_list,cat_sizes)
        
                }
    
    #saves the data to a file for later usage
#     with open('TwitterDashboard/static/twitterGeneralData.json', 'w') as outfile:
#     with open(file_name, 'w') as outfile:
#         json.dump(dataJson, outfile)
        
    return dataJson
        
                     
     
def children(category_list,cat_sizes):
#     print "category list: "
#     print category_list
    
    children = []
    counter = 0
    for cat in category_list:
        new_value = {}
        new_value["name"] = cat
        new_value["name_value"] = cat
        new_value["value"] = cat_sizes[counter]
#         new_value["url"] = "chapters"
        new_value["url"] = "../ndpviz/chapters/"
        children.append(new_value)
        counter = counter + 1
        
#     for child in children:
#         print child
        
    return children

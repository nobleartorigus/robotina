def get_key(dictionary, val): 
    for key, value in dictionary.items(): 
         if val == value: 
             return key 
  
    return "key doesn't exist"

def removekey(dictionary, key):
    del dictionary[key]
    return dictionary
def get_key(dictionary, val): 
    for key, value in dictionary.items(): 
         if val == value: 
             return key 
  
    return "key doesn't exist"

def get_value(dictionary, ky): 
    for key, value in dictionary.items(): 
         if ky == key: 
             return value
  
    return "Value doesn't exist"

def removekey(dictionary, key):
    try:
        del dictionary[key]
        return dictionary
    except Exception:
        return 'Cama Fija'
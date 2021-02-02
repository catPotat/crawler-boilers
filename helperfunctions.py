from datetime import datetime

def compress_object(origin_obj, attrs_to_save):
    new_obj = {'Absent keys':[]}

    for key in attrs_to_save:
        if key in origin_obj:
            if type(val:=origin_obj[key]) in [int, str, datetime]:
                new_obj[key] = val
            else:
                new_obj[key] = str(val)
        else:
            new_obj['Absent keys'].append(key)
    
    return new_obj



import json
from bson import json_util

def prettyprint(dict_):
    print(json.dumps(dict_, indent=4, sort_keys=True, default=json_util.default))



from io import StringIO
from html.parser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.text = StringIO()
    def handle_data(self, d):
        self.text.write(d)
    def get_data(self):
        return self.text.getvalue()

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()



def substr_matches(text, substr_ls, exact=False):
    ''' good for discord find by substrings '''
    matches = []
    match_count = 0
    for substr in substr_ls:
        if exact and substr == text.lower():
            return True
        if substr in text.lower():
            match_count += 1
    return match_count == len(substr_ls)

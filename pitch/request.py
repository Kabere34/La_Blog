# from pitch import app
# import urllib.request
# import json
# from .quote import Quotes


# def get_quotes():
#     with urllib.request.urlopen('http://quotes.stormconsultancy.co.uk/random.json') as url:
#         data = url.read()
#         get_json = json.loads(data)

#         if get_json['author'] and get_json['quote']:

#             author = get_json['author']
#             quote = get_json['quote']

#             new_quote = Quotes(author, quote)

#             return new_quote

#         else:
#             return None

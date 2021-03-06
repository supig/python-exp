import random
import json

# quotes = ["Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !", "On doit pouvoir choisir entre s'écouter parler et se faire entendre."]
# characters = ["alvin et les Chipmunks", "Babar", "betty boop", "calimero", "casper", "le chat potté", "Kirikou"]

def read_data_from_json(key):
    key = str(key)
    values = []
    with open('read_json/' + key + 's.json') as f:
        data = json.load(f)
        for entry in data:
            values.append(entry[key])
        return values

def random_characters():
    characters = read_data_from_json('character')
    return get_random_item(characters)

def random_quotes():
    quotes = read_data_from_json('quote')
    return get_random_item(quotes)

def get_random_item(object_list):
    rand_numb = random.randint(0, len(object_list) - 1)
    item = object_list[rand_numb] # get a quote from a list
    return item # return the item

def capitalize_custom(name, mess):
    name = name.title()
    mess = mess.capitalize()
    return (name, mess)

def message(character, quote):
    A = capitalize_custom(character, quote)
    return "{} a dit : {}".format(A[0],A[1].strip()) #method strip in string module

user_answer = input('Tapez entrée pour connaître une autre citation ou B pour quitter le programme.')

while user_answer != "B":
    print(message(random_characters(), random_quotes()))
    user_answer = input('Tapez entrée pour connaître une autre citation ou B pour quitter le programme.')
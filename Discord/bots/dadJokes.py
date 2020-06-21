import requests
import json
import random

# def search():
#     cust_inp = str(input('Let me tell you a joke! Give me a word: '))
#     return cust_inp

def request(*args):
    resp = requests.get(
                'http://icanhazdadjoke.com/search',
                headers={"Accept": "application/json"},
                params={'term': args} ).json()
    return resp['results']

def joke(*args):
    joke_return = request(args)
    return [i['joke'] for i in joke_return]

def choosing_joke(*args):
    jokes = joke(args)
    if len(jokes) > 1:
        return random.choice(jokes)
    elif jokes == []:
        return('Gimme\' another word')
    else:
        return jokes


if __name__ == '__main__':
    print(choosing_joke())
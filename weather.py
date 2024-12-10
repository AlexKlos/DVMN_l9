from urllib.parse import quote

import requests


def main():
    url = 'https://wttr.in'
    params = {
        'n': '',
        'T': '',
        'q': '',
        'm': '',
        'M': '',
        'lang': 'ru'
    }
    places = ['london', 'SVO', 'Череповец']
    
    for place in places:
        try:
            response = requests.get(url + '/' + quote(place), params=params)
            print(response.url)
            response.raise_for_status()
            print(response.text)
        except requests.exceptions.RequestException as e:
            print('An error occurred:', e)
            

if __name__ == '__main__':
    main()
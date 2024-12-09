import requests


def main():
    url_1 = 'https://wttr.in/london?nTqm&lang=en'
    url_2 = 'https://wttr.in/Шереметьево?nTqm&lang=ru'
    url_3 = 'https://wttr.in/Череповец?nTqm&lang=ru'
    urls = [url_1, url_2, url_3]
    
    for url in urls:
        response = requests.get(url)
        print(response.text)
        response.raise_for_status()


if __name__ == '__main__':
    main()
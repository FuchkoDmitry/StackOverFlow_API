import requests
import time
import datetime


def get_questions_list():
    url = 'https://api.stackexchange.com/2.3/questions'
    params = {'tagged': 'Python', 'total': 'True', 'pagesize': 50, 'page': 1,
              'site': 'stackoverflow.com',
              'fromdate': f'{datetime.date.today() - datetime.timedelta(days=2)}',
              'todate': f'{datetime.date.today()}'
              }
    response = requests.get(url, params=params)
    for news in response.json()['items']:
        print(f'"{time.ctime(news["creation_date"])}", {news["link"]}, "{news["title"]}"')
    while response.json()['has_more']:
        params['page'] += 1
        response = requests.get(url, params=params)
        for news in response.json()['items']:
            print(f'"{time.ctime(news["creation_date"])}", {news["link"]}, "{news["title"]}"')
    else:
        print('Download completed.')


if __name__ == '__main__':
    get_questions_list()

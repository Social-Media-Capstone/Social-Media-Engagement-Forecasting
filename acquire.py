import env
from env import api
from tikapi import TikAPI, ValidationException, ResponseException

def get_trend(count):
    '''
    This function takes a number as input and search for that amount of trending videos on tiktok
    '''
    try:
        response = api.public.explore(
        count=count,
        session_id='0',
        country='us')
        print(response.json())
        
    except ValidationException as e:
        print(e, e.field)

    except ResponseException as e:
        print(e, e.response.status_code)
        
def get_hashtag(hashtag):
    '''
    This function takes in a hashtag, and return the video stats count
    for the hashtag in the format of a list.
    '''
    json_to_list = []
    stats = []
    try:
        response = api.public.hashtag(
            name=hashtag
        )

        hashtagId = response.json()['challengeInfo']['challenge']['id']

        response = api.public.hashtag(
            id=hashtagId
        )


        while(response):
            cursor = response.json().get('cursor')
            print("Getting next items ", cursor)
            response = response.next_items()
            json_to_list.append(response.json())
            
    except ValidationException as e:
        print(e, e.field)

    except ResponseException as e:
        print(e, e.response.status_code)

    return json_to_list

def get_data(data):
    '''
    This functino takes in a list of jsons, extract the useful information,
    and return everything into a dataframe.
    '''
    stats = []
    for j in range(0,len(data)):
        for i in range(0,len(data[j]['itemList'])):
            data[j]['itemList'][i]['stats']['time']=data[j]['itemList'][i]['createTime']
            stats.append(data[j]['itemList'][i]['stats'])
    df = pd.DataFrame(stats)
    return df
    
def get_discover(category):
    '''
    This video takes in a string as category and returns the search result of that category's videos from tiktok
    '''
    try:
        response = api.public.discover(
            category=category
        )

        print(response.json())

        while(response):
            offset = response.json().get('offset')
            print("Getting next items ", offset)
            response = response.next_items()

    except ValidationException as e:
        print(e, e.field)

    except ResponseException as e:
        print(e, e.response.status_code)
    
def get_keyword(keyword):
    '''
    This video takes in a string as keyword and returns search result of the keyword videos from tiktok
    '''
    try:
        response = api.public.discoverKeyword(
            keyword=keyword
        )

        print(response.json())

    except ValidationException as e:
        print(e, e.field)

    except ResponseException as e:
        print(e, e.response.status_code)


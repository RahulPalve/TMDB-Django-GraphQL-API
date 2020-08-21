import requests
from .models import Movie

def populate():
    API_KEY='986eb0ba9ed1a2b7084c401742843efa'
    REG='IN'
    LANG='en-US'
    base_url='https://api.themoviedb.org/3/movie/'

    for content in ['popular','upcoming','now_playing']:
        print('Database updating with : '+content)
        for page in range(1,6):
            params='{}?api_key={}&language={}&region={}&page={}'.format(content,API_KEY,LANG,REG,str(page))
            r=requests.get(base_url+params)
            for i in r.json()['results']:
                m=Movie(poster_path=i['poster_path'],
                adult=i['adult'],
                overview=i['overview'],
                release_date=i['release_date'],
                genre_ids=str(i['genre_ids']).strip('[]'),
                tmdb_id=i['id'],
                original_title=i['original_title'],
                original_language=i['original_language'],
                title=i['title'],
                backdrop_path=i['backdrop_path'],
                popularity=i['popularity'],
                vote_count=i['vote_count'],
                video=i['video'], 
                vote_average=i['vote_average']
                )
                m.save()
        



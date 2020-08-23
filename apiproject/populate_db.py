import requests
import os
import django
os.environ["DJANGO_SETTINGS_MODULE"] = 'apiproject.settings'
django.setup()
from apiapp.models import Movie

API_KEY='986eb0ba9ed1a2b7084c401742843efa'
REG='IN'
LANG='en-US'
base_url='https://api.themoviedb.org/3/movie/'
for page in range(1,6):
    params='popular?api_key={}&language={}&region={}&page={}'.format(API_KEY,LANG,REG,str(page))
    r=requests.get(base_url+params)
    print("Database adding movies from page : ",page)
    for i in r.json()['results']:
        tag_url='{}{}/keywords?api_key={}'.format(base_url,str(i['id']),API_KEY)
        r_tags=requests.get(tag_url).json()['keywords']
        tags=[ tag['name'] for tag in r_tags]
        i['genre_ids']=[str(gid) for gid in i['genre_ids'] ]
        tags=','.join(tags+i['genre_ids'])

        m=Movie(
            poster_path=i['poster_path'],
            adult=i['adult'],
            overview=i['overview'],
            release_date=i['release_date'],
            genre_ids=','.join(i['genre_ids']),
            tmdb_id=i['id'],
            original_title=i['original_title'],
            original_language=i['original_language'],
            title=i['title'],
            backdrop_path=i['backdrop_path'],
            popularity=i['popularity'],
            vote_count=i['vote_count'],
            video=i['video'], 
            vote_average=i['vote_average'],
            tags=tags
        )
        m.save()
        print("..",end='')
    
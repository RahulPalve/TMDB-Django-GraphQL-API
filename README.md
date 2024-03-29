# Checkout Live running version!
[https://djgql.herokuapp.com/api](https://djgql.herokuapp.com/api)


# Installation Guide
***Instructions to run project on localhost :**</br>
( Only applicable for "**master**" branch, "**prod**" branch have production ready code ), also the database provided is pre-populated. If you want to Populate database delete  db file follow below instructions and run "**populate_db.py**" script.

To setup this project, create a virtual environment using Python 3.7 or higher. And make sure you install django 3.1([link to Django Installation Guide !](https://docs.djangoproject.com/en/2.2/topics/install/) ). Then run the following command in your terminal (ensure that you are in the project directory):

~~~ 
$ pip install -r requirements.txt 
~~~
It will set your environment up to run the project

Run the following commands in your terminal:
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
This will set your SQL database up and run your local server. Press ```ctrl+c to``` stop the server.

You will find a directory named ```schema.py ``` in the root directory of the project, most GraphQL API code should go there.

Do remember to run ```python manage.py makemigrations``` in your terminal before committing changes.


# Other Notes:

* As Django's ORM is used, any database can be used, without much modification.
* For Recommenadation System [Jaccard Similarity](https://blog.dominodatalab.com/recommender-systems-collaborative-filtering) (content based) is used, recommendations are calculated on query, this can be calculataed beforehand to improve efficiency.




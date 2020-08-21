import graphene
from graphene_django import DjangoObjectType
from apiapp.models import Movie, MovieList

class MovieType(DjangoObjectType):
    class Meta:
        model = Movie

class MovieListType(DjangoObjectType):
    class Meta:
        model = MovieList

class Query(graphene.ObjectType):

    movies=graphene.List(MovieType)
    movie=graphene.Field(MovieType, id=graphene.Int())

    def resolve_movies(self,info):
        return Movie.objects.all()

    def resolve_movie(self,info,id):
        try:
            return Movie.objects.get(pk=id)
        except:
            return None

schema = graphene.Schema(query=Query)

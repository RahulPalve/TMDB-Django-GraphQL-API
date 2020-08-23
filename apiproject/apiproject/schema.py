import graphene
from graphene_django import DjangoObjectType
from apiapp.models import Movie, MovieList
from graphql import GraphQLError

class MovieType(DjangoObjectType):
    class Meta:
        model = Movie

class MovieListType(DjangoObjectType):
    class Meta:
        model = MovieList

class CreateMovieList(graphene.Mutation):
    id = graphene.Int()
    codename=graphene.String()

    class Arguments:
        codename=graphene.String()

    def mutate(self, info, codename):
        m = MovieList(codename=codename)
        m.save()

        return CreateMovieList(
            id=m.pk,
            codename=m.codename,
        )   

class PushToList(graphene.Mutation):
    movie_id = graphene.Int()
    codename=graphene.String()
    id = graphene.Int()

    class Arguments:
        codename=graphene.String()
        movie_id = graphene.Int()

    def mutate(self, info, codename, movie_id):
        ml = MovieList.objects.get(codename=codename)
        m = Movie.objects.get(pk=movie_id)
        ml.movies.add(m)

        if(ml.listtags!=None):
            set_mltags=set(ml.listtags.split(','))
        else:
            set_mltags=set()
        set_mtags=set(m.tags.split(','))

        tag_union=list(set_mltags.union(set_mtags))
        ml.listtags=','.join(tag_union)
        ml.save()
        

        return PushToList(
            codename=ml.codename,
            movie_id=m.tmdb_id,
            id=ml.id
        )



class Query(graphene.ObjectType):

    movies=graphene.List(MovieType)
    movie=graphene.Field(MovieType, id=graphene.Int())
    recommendedMovies=graphene.List(MovieType,codename=graphene.String())
    movieList=graphene.Field(MovieListType,codename=graphene.String())

    def resolve_movies(self,info):
        return Movie.objects.all()

    def resolve_movie(self,info,id=None):
        try:
            return Movie.objects.get(pk=id)
        except:
            return None

    def resolve_movieList(self,info,codename=None):
        try:
            return MovieList.objects.get(codename=codename)
        except:
            return None

    def resolve_recommendedMovies(self,info,codename=None):
        ml=MovieList.objects.get(codename=codename)
        tag_set=set(ml.listtags.split(","))

        recommended=sorted(Movie.objects.all(), key=lambda movie: len(tag_set.intersection(set(movie.tags.split(",")))))
        l=len(recommended)
        return recommended[l-1:l-10:-1]

class Mutation(graphene.ObjectType):
    create_movie_list = CreateMovieList.Field()
    push_to_list = PushToList.Field() 
schema = graphene.Schema(query=Query,mutation=Mutation)

import graphene
from graphene_django import DjangoObjectType
from apiapp.models import Movie, MovieList


class MovieType(DjangoObjectType):
    class Meta:
        model = Movie

class MovieListType(DjangoObjectType):
    class Meta:
        model = MovieList

class CreateMovieList(graphene.Mutation):
    codename=graphene.String()
    success=graphene.Boolean()

    class Arguments:
        codename=graphene.String()

    def mutate(self, info, codename):
        try:
            m = MovieList(codename=codename)
            m.save()
            success=True
        except:
            success=False
        return CreateMovieList(
            codename=m.codename,
            success=success,
        )   

class PushToList(graphene.Mutation):
    movie_id = graphene.Int()
    codename=graphene.String()

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
            movie_id=m.pk,
        )



class Query(graphene.ObjectType):

    movies=graphene.List(MovieType)
    movie=graphene.Field(MovieType, movie_id=graphene.Int())
    lists=graphene.List(MovieListType)
    list=graphene.Field(MovieListType,codename=graphene.String())
    recommendedMovies=graphene.List(MovieType,codename=graphene.String())


    def resolve_movies(self,info):
        return Movie.objects.all()

    def resolve_movie(self,info,movie_id=None):
        try:
            return Movie.objects.get(pk=movie_id)
        except:
            return None

    def resolve_lists(self,info):
        return MovieList.objects.all()

    def resolve_list(self,info,codename=None):
        try:
            return MovieList.objects.get(codename=codename)
        except:
            return None

    def resolve_recommendedMovies(self,info,codename=None):
        ml=MovieList.objects.get(codename=codename)
        tag_set=set(ml.listtags.split(","))

        def Jaccard(movie):
            try:
                intersect=len(tag_set.intersection(set(movie.tags.split(","))))
                union=len(tag_set.union(set(movie.tags.split(","))))
                return float(intersect/union)
            except:
                return 0

        recommended=sorted(Movie.objects.all(), key=Jaccard)
        l=len(recommended)
        return recommended[l-1:l-10:-1]

class Mutation(graphene.ObjectType):
    list = CreateMovieList.Field()
    push = PushToList.Field() 
schema = graphene.Schema(query=Query,mutation=Mutation)

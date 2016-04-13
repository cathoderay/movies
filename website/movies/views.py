from django.shortcuts import render
from django.views import generic

from django.db.models import Q

from movies.models import Movie, Genre, Actor


class IndexView(generic.ListView):
    template_name = 'movies/index.html'
    context_object_name = 'movies'
    queryset = Movie.objects.order_by('-popularity')


class MovieDetailView(generic.DetailView):
    model = Movie
    template_name = 'movies/detail.html'
    context_object_name = 'movie'

    def get_context_data(self, **kwargs):
        context = super(MovieDetailView, self).get_context_data(**kwargs)

        #TODO: refactor this query
        movies = Movie.objects.all()
        cur_pk = self.kwargs['pk']
        cur_movie = Movie.objects.get(pk=cur_pk)
        cur_genres = map(lambda x: x[0], cur_movie.genres.values_list())
        cur_cast = map(lambda x: x[0], cur_movie.cast.values_list())

        related_movies = []
        for genre in cur_genres:
            related_movies += Movie.objects.exclude(pk=cur_pk).filter(genres__in=[genre])
        for cast in cur_cast:
            related_movies += Movie.objects.exclude(pk=cur_pk).filter(cast__in=[cast])

        order = {}
        for movie in related_movies:
            if not movie.pk in order:
                order[movie.pk] = 1
            else:
                order[movie.pk] += 1
        movies_pks_sorted = map(lambda x: x[0], 
                            sorted(order.items(), key=lambda x: x[1], reverse=True))[:10]
        
        related_movies = []
        for movie in movies_pks_sorted:
            related_movies.append(Movie.objects.get(pk=movie))
        context['movies'] = related_movies

        return context


class MoviesByGenreView(generic.ListView):
    model = Movie
    template_name = 'movies/genre.html'
    context_object_name = 'movies'

    def get_queryset(self):
        return Movie.objects.filter(genres__in=[self.kwargs['pk']])

    def get_context_data(self, **kwargs):
        context = super(MoviesByGenreView, self).get_context_data(**kwargs)
        context['genre'] = Genre.objects.get(pk=self.kwargs['pk'])
        return context


class ActorDetailView(generic.DetailView):
    model = Actor
    template_name = 'movies/actor.html'
    context_object_name = 'actor'

    def get_context_data(self, **kwargs):
        context = super(ActorDetailView, self).get_context_data(**kwargs)
        context['movies'] = Movie.objects.filter(cast__in=[self.kwargs['pk']])[:20]
        return context

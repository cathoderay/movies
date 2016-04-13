from django.test import TestCase

from movies.models import Genre, Actor, Movie


class GenreTest(TestCase):
    def test_genre_has_str_repr(self):
        genre = Genre(name='Comedy')
        self.assertEqual(genre.name, str(genre))


class ActorTest(TestCase):
    def test_actor_has_str_repr(self):
        actor = Actor(name="Leonardo DiCaprio")
        self.assertEqual(actor.name, str(actor))


class MovieTest(TestCase):
    def test_movie_has_str_repr(self):
        movie = Movie(title="Pulp Fiction")
        self.assertEqual(movie.title, str(movie))



    

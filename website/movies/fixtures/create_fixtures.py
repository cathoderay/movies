# -*- coding: utf-8 -*-

""" This script is intended to generate a dataset in order
    to test the movies app.
    Side-effect: it creates files: actors.yaml, 
                                   genres.yaml,
                                   movies.yaml"""


from scrap import get_movies_data
import yaml


genres = [u"Ação", u"Animação", u"Aventura", u"Biografia", u"Comédia", 
          u"Documentário", u"Drama", u"Fantasia", u"Ficção-Científica",
          u"Guerra", u"Infantil", u"Musical", u"Policial", u"Romance",
          u"Suspense", u"Terror/Horror", u"Western"]


def genres_fixtures():
    g = open('genres.yaml', 'w+')
    for i, genre in enumerate(genres):
        g.write("- model: movies.genre\n")
        g.write("  pk: %d\n" % i)
        g.write("  fields:\n")
        g.write("    name: %s\n" % genre.encode('utf8'))
    g.close()


def actors_movies_fixtures():
    a = open('actors.yaml', 'w+') 
    m = open('movies.yaml', 'w+')
    
    movies = get_movies_data()
    actors = []
    for movie_pk, movie in enumerate(movies):
        actors_pks = []
        for actor in movie['actors']:
            if actor not in actors:
                actors.append(actor)
                actor_pk = actors.index(actor)
                a_fixture = [{'model': 'movies.actor', 
                              'pk': actor_pk, 
                              'fields': {'name': actor}}]
                actors_pks.append(actor_pk)
            else:    
                actors_pks.append(actors.index(actor))
            a.write(yaml.safe_dump(a_fixture, 
                                   default_flow_style=False, 
                                   allow_unicode=True))

            a.flush()     
        m_fixture = [{'model': 'movies.movie', 
                      'pk': movie_pk, 
                      'fields': {'title': movie['name'],
                      'cast': actors_pks, 
                      'genres': map(lambda x: genres.index(x), movie['genres']),
                      'poster' : movie['img'],
                      'synopsis' : movie['description']}}]
        m.write(yaml.safe_dump(m_fixture, 
                               default_flow_style=False, 
                               allow_unicode=True))
        m.flush()
    m.close()
    a.close()


if __name__ == '__main__':
    genres_fixtures()
    actors_movies_fixtures()

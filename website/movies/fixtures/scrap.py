# -*- coding: utf-8 -*- 

""" This is intended to do web scrapping from globosatplay. 
    Side-effect: It saves movies imgs to 'media' directory, in this same path.
    The script create_fixtures.py uses it.
    After usage, move the 'media' directory to its destiny."""


import urllib2
import urllib
from BeautifulSoup import BeautifulSoup
from selenium import webdriver 
import time
import os

URL = 'http://globosatplay.globo.com/telecine/'
GENRES = ['acao', 'animacao', 'aventura', 'biografia', 
          'comedia', 'documentario', 'drama', 'fantasia',
          'ficcao-cientifica', 'guerra', 'infantil',
          'musical', 'policial', 'romance', 'suspense',
          'terror-horror', 'western']


def get_movie_data(code):
    url = URL + "v/" + code
    movie = {}

    response = urllib2.urlopen(url) 
    soup = BeautifulSoup(response.read())
    movie['name'] = soup.find('span', itemprop='name').text.strip()
    movie['genres'] = map(lambda x: x.text.strip(), soup.findAll('span', itemprop='genre'))
    movie['description'] = soup.find('p', itemprop='description').text.strip()
    movie['img'] = soup.find('div', 'info-poster').find('img').get('src')
    movie['actors'] = map(lambda y: y.find('span', itemprop='name').text, 
                          soup.findAll('span', itemprop='actor'))
    filename = "%f.jpg" % time.time()
    urllib.urlretrieve(movie['img'], os.path.join('media', filename))
    movie['img'] = filename
    return movie


def get_movies_codes(genre):
    url = URL + 'generos/' + genre
    driver = webdriver.PhantomJS()
    driver.get(url)
    posters = driver.find_elements_by_class_name('poster')
    return [poster.get_attribute('data-video-id')
            for poster in posters[:10]] #gets 5 movies per genre
 
 
def get_movies_data():
    codes_seen = set()
    for genre in GENRES:
        current_codes = get_movies_codes(genre)
        for code in current_codes:
            if code not in codes_seen:
                yield get_movie_data(code) 
            codes_seen.add(code)





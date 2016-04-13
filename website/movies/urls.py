from django.conf.urls import patterns, url


from . import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.MovieDetailView.as_view(), name='movie_detail'),
    url(r'^genres/(?P<pk>\d+)/$', views.MoviesByGenreView.as_view(), name='genre'),
    url(r'^actor/(?P<pk>\d+)/$', views.ActorDetailView.as_view(), name='actor_detail')
) 



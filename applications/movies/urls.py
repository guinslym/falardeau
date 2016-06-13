from django.conf.urls import url

from .views import MoviesListView

urlpatterns = [
    url(r'^$', MoviesListView.as_view(), name='websites_list'),
    #url(r'^(?P<slug>[-\w]+)/$', WebsitesDetailView.as_view(), name='websites_detail'),
]

from django.conf.urls import url
import views
from views import ArticleListView
from views import ArticlePublishView, ArticleDetailView

urlpatterns = [

    url(r'^$', views.blog_index, name = 'blog_index'),
    url(r'^article/publish$', ArticlePublishView.as_view(), name='article_publish'),
    url(r'^article/(?P<title>\S+)$', ArticleDetailView.as_view(), name='article_detail'),
    url(r'^article/(?P<title>\w+\.?\w+)/edit$', ArticleEditView.as_view(), name='article_edit'),


]
    

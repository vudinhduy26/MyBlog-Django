from  django.urls import include,path
from . import views
from django.conf import settings

urlpatterns = [
    path('',views.index,name='home'),
    path('<str:categories_slug>/<str:categories_child_slug>/<str:detail_slug>',views.detail_content,name='detail_content'),
    #path('<str:categoriesss>',views.categoriess,name='categorie'),
    path('<str:categories>/<str:categories_child>',views.categoriess_content_child,name='categories-child'),
    path('contact/',views.contact,name='contact'),
    #### url list same categories
    path('<str:slugsame>',views.ContentSamecate,name='ContentSamecate'),
    path('', views.sendMail, name='send_mail'),
    path('search-content/', views.search_content, name="search_content")
]
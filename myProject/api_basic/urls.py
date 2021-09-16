from . import views
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

# Routing the rout
router = DefaultRouter()
router.register('article', views.ArticleViewset, basename='article')

urlpatterns = [

    # path('',views.Article_list, name='article-list' ),
    path('',views.ArticleAPIView.as_view(), name='article-list' ),

    path('detail/<int:pk>/',views.article_detail, name='article-detail' ),
    path('detail/<int:id>/', views.ArticleDetails.as_view(), name='article-detail' ),

    # path('', views.api_root),

    path('article/', views.GenericView.as_view(), name='article-generic-list'),
    path('<int:id>/', views.GenericView.as_view(), name='article-generic'),

    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),

    # path('users/',
    #      views.UserList.as_view(),
    #      name='user-list'),
    #
    # path('users/<int:pk>/',
    #      views.UserDetail.as_view(),
    #      name='user-detail'),
]

from django.urls import path

from . import views

urlpatterns = [
    path('<int:plot_point_id>/', views.plot_point, name='plot_point'),
    path('profile', views.profile, name='profile'),
    # ex: /StoryPage/5/
    #path('<int:question_id>/', views.detail, name='detail'),
    # ex: /StoryPage/5/results/
    #path('<int:question_id>/results/', views.results, name='results'),
    # ex: /StoryPage/5/vote/
    #path('<int:question_id>/vote/', views.vote, name='vote'),
]
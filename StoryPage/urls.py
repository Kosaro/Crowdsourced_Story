from django.urls import path

from . import views

urlpatterns = [
    path('', views.plot_point, name='plot_point'),
    path('get-choices', views.get_choices, name='get_choices'),
    path('add_choice', views.add_choice, name='add_choice'),
    path('upvote', views.upvote, name='upvote'),
    path('choice_upvote', views.choice_upvote, name='choice_upvote'),
    path('downvote', views.downvote, name='downvote'),
    path('choice_downvote', views.choice_downvote, name='choice_downvote'),
    path('bookmark', views.bookmark, name='bookmark'),
    # ex: /StoryPage/5/
    #path('<int:question_id>/', views.detail, name='detail'),
    # ex: /StoryPage/5/results/
    #path('<int:question_id>/results/', views.results, name='results'),
    # ex: /StoryPage/5/vote/
    #path('<int:question_id>/vote/', views.vote, name='vote'),
]
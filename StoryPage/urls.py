from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.storySelection, name="default"),
    path('<int:plot_point_id>/', views.plot_point, name='plot_point'),
    path('profile', views.profile, name='profile'),
    path('add-choice/', views.add_choice, name='add_choice'),
    path('open_plot_point/', views.open_plot_point, name='open_plot_point'),
    path('toggle_bookmark/', views.toggle_bookmark, name='toggle_bookmark'),
    path('toggle_upvote/', views.toggle_upvote, name='toggle_upvote'),
    path('toggle_downvote/', views.toggle_downvote, name='toggle_downvote'),
    #path("logout/", views.logout_request, name="logout"),
    #path("login/", auth_views.login, name="login"),
    path("login/", views.log_in, name="login"),
    path("register/", views.register, name="register"),
    path('accounts/', include('django.contrib.auth.urls')),
    #path(r'accounts/login/', 'django.contrib.auth.views.login', name='login'),
]
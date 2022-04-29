from django.urls import path

from . import views

app_name='polls'
urlpatterns = [


   # ex /polls/
   # path('',views.index,name='index'),
   path('', views.IndexView.as_view(), name='index'),

   # ex /polls/5
   # path('<int:question_id>/',views.detail,name='detail'),
   path('<int:pk>/', views.DetailView.as_view(), name='detail'),

   # ex /polls/5/results/
   # path('<int:question_id>/results/', views.results, name='results'),
   path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),

   # ex /polls/5/vote
   path('<int:question_id>/vote', views.vote, name='vote'),

   # pk : 데이터 내부의 하나의 열 데이터를 구분할 수 있는 값 중복x
]
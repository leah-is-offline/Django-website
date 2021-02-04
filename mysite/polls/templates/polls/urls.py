from django.urls import path
from . import views

urlpatterns = [
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote')

]

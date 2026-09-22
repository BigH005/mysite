from django.urls import path

from . import views

# app_name creates a "namespace" so templates can refer to these URLs as
# polls:index, polls:detail, etc. -- this matters once you have more than
# one app with a "detail" or "index" view.
app_name = "polls"

urlpatterns = [
    # /polls/
    path("", views.IndexView.as_view(), name="index"),
    # /polls/5/
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # /polls/5/results/
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    # /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]

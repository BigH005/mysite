from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    """Lists every question, newest first. Maps to /polls/"""
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.order_by("-pub_date")


class DetailView(generic.DetailView):
    """Shows one question with its choices as a voting form. Maps to /polls/<id>/"""
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    """Shows vote counts and percentages for one question. Maps to /polls/<id>/results/"""
    model = Question
    template_name = "polls/results.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        question = context["question"]
        context["total_votes"] = sum(
            c.votes for c in question.choice_set.all())
        return context


def vote(request, question_id):
    """Handles the POST from the voting form. Maps to /polls/<id>/vote/"""
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    selected_choice.votes += 1
    selected_choice.save()
    # Redirect after a successful POST so refreshing the results page
    # doesn't resubmit the vote.
    return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

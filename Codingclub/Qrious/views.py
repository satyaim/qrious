from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views import generic
from django.views.generic import View, FormView
from django.core.urlresolvers import reverse

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import auth
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Player, Questions
from .forms import AnswerForm


def test(request):
    return render(request, 'Qrious/test.html')


def main(request):
    user = request.user
    try:
        up = Player()
        up.name = user
        up.save()
    except:
        up = Player.objects.get(name=user)

    return render(request, 'Qrious/index.html')


class IndexView(generic.ListView):
    template_name = 'Qrious/index.html'

    def get_queryset(self):
        return Questions.objects.all()


class DetailView(generic.DetailView):
    model = Questions
    template_name = 'Qrious/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_pk = self.kwargs['pk']
        product = Questions.objects.get(pk=product_pk)
        context.update({
            'product': product
        })
        return context


def answer(request, pk):
    question = Questions.objects.get(pk=pk)
    answerof = request.POST['answerof']

    user = request.user
    up = Player.objects.get(name=user)

    if answerof == question.solution:
        list1 = list(up.answers_given)
        list1[question.question_no] = '1'
        up.answers_given = ''.join(list1)
        up.question_no += 1
        up.save()

    c = up.answers_given.count('1')
    up.score = c*10
    up.save()


    return render(request, 'Qrious/test.html')

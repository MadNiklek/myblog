from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Article
from django.contrib.auth.decorators import login_required
from . import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.views.generic.base import View


def article_list(request):
    articles = Article.objects.all().order_by('date');
    articles = articles.reverse()
    userr = request.user
    return render(request, 'article_list.html', { 'articles': articles, 'userr' : str(userr).title()  }   )

def delete(request, slug):
    article = Article.objects.get(slug = slug)
    articles = Article.objects.all().order_by('date');
    articles = articles.reverse()
    user = request.user
    if user.is_authenticated:
        userr = request.user
        article.delete()
        return render(request, 'article_list.html', { 'articles': articles, 'userr' : str(userr).title() })
    else:
        form=AuthenticationForm()
        return render(request, 'login.html', {'form' : form})
    return render(request, 'article_detail.html', { 'article': article })

def article_detail(request, slug):
    article = Article.objects.get(slug = slug)
    return render(request, 'article_detail.html', { 'article': article })

@login_required(login_url="/accounts/login/")
def article_create(request):
    userr = request.user
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            # save article to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'article_create.html', { 'form': form,'userr':str(userr).title()})

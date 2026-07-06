from django.shortcuts import render
from articles.models import Article
from projects.models import Project


def accueil(request):
    derniers_articles = Article.objects.all().order_by('-date')[:3]
    derniers_projects = Project.objects.all().order_by('-date')[:3]
    return render(request, 'core/index.html', {
        'derniers_articles': derniers_articles,
        'derniers_projects': derniers_projects,
    })


def apropos(request):
    return render(request, 'core/apropos.html')


def journal(request):
    articles = Article.objects.all().order_by('-date')
    return render(request, 'articles/liste.html', {'articles': articles, 'query': ''})

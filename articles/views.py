from django.shortcuts import render, get_object_or_404
from .models import Article

def liste_articles(request):
    query = request.GET.get('q', '')
    if query:
        articles = Article.objects.filter(titre__icontains=query).order_by('-date')
    else:
        articles = Article.objects.all().order_by('-date')
    return render(request, 'articles/liste.html', {
        'articles': articles,
        'query': query,
    })

def detail_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'articles/detail.html', {'article': article})

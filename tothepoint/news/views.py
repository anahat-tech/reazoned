from django.shortcuts import render,redirect
import feedparser
from news.models import Headlines
from newspaper import Article
import nltk
from django.views.generic import DetailView


def index(request):
    Headlines.objects.all().delete()
    url = 'https://timesofindia.indiatimes.com/rssfeeds/1221656.cms'
    feed = feedparser.parse(url)
    for entry in feed.entries:
        postlink = entry.link
        article = Article(postlink)
        #article.download()
        #article.parse()
        new_headline = Headlines()
        new_headline.title = entry.title
        new_headline.url = entry.link
        new_headline.image = article.top_image
        new_headline.text = article.text
        new_headline.save()
    headlines = Headlines.objects.all()[::-1]
    context = {
        'object_list': headlines,
    }
    return render(request, "news/news.html", context)


def world(request):
    Headlines.objects.all().delete()
    url = 'https://timesofindia.indiatimes.com/rssfeeds/296589292.cms'
    feed = feedparser.parse(url)
    for entry in feed.entries:
        postlink = entry.link
        article = Article(postlink)
        new_headline = Headlines()
        new_headline.title = entry.title
        new_headline.url = entry.link
        new_headline.image = article.top_image
        new_headline.text = article.text
        new_headline.save()
    headlines = Headlines.objects.all()[::-1]
    context = {
        'object_list': headlines,
    }
    return render(request, "news/world.html", context)


def business(request):
    Headlines.objects.all().delete()
    url = 'https://timesofindia.indiatimes.com/rssfeeds/1898055.cms'
    feed = feedparser.parse(url)
    for entry in feed.entries:
        postlink = entry.link
        article = Article(postlink)
        new_headline = Headlines()
        new_headline.title = entry.title
        new_headline.url = entry.link
        new_headline.image = article.top_image
        new_headline.text = article.text
        new_headline.save()
    headlines = Headlines.objects.all()[::-1]
    context = {
        'object_list': headlines,
    }
    return render(request, "news/business.html", context)


def tech(request):
    Headlines.objects.all().delete()
    url = 'https://timesofindia.indiatimes.com/rssfeeds/66949542.cms'
    feed = feedparser.parse(url)
    for entry in feed.entries:
        postlink = entry.link
        article = Article(postlink)
        new_headline = Headlines()
        new_headline.title = entry.title
        new_headline.url = entry.link
        new_headline.image = article.top_image
        new_headline.text = article.text
        new_headline.save()
    headlines = Headlines.objects.all()[::-1]
    context = {
        'object_list': headlines,
    }
    return render(request, "news/tech.html", context)


def sports(request):
    Headlines.objects.all().delete()
    url = 'https://timesofindia.indiatimes.com/rssfeeds/4719148.cms'
    feed = feedparser.parse(url)
    for entry in feed.entries:
        postlink = entry.link
        article = Article(postlink)
        new_headline = Headlines()
        new_headline.title = entry.title
        new_headline.url = entry.link
        new_headline.image = article.top_image
        new_headline.text = article.text
        new_headline.save()
    headlines = Headlines.objects.all()[::-1]
    context = {
        'object_list': headlines,
    }
    return render(request, "news/sports.html", context)


def entertainment(request):
    Headlines.objects.all().delete()
    url = 'https://timesofindia.indiatimes.com/rssfeeds/1081479906.cms'
    feed = feedparser.parse(url)
    for entry in feed.entries:
        postlink = entry.link
        article = Article(postlink)
        new_headline = Headlines()
        new_headline.title = entry.title
        new_headline.url = entry.link
        new_headline.image = article.top_image
        new_headline.text = article.text
        new_headline.save()
    headlines = Headlines.objects.all()[::-1]
    context = {
        'object_list': headlines,
    }
    return render(request, "news/entertainment.html", context)


def opinion(request):
    Headlines.objects.all().delete()
    url = 'https://timesofindia.indiatimes.com/rssfeeds/784865811.cms'
    feed = feedparser.parse(url)
    for entry in feed.entries:
        postlink = entry.link
        article = Article(postlink)
        #article.download()
        #article.parse()
        new_headline = Headlines()
        new_headline.title = entry.title
        new_headline.url = entry.link
        new_headline.image = article.top_image
        new_headline.text = article.text
        new_headline.save()
    headlines = Headlines.objects.all()[::-1]
    context = {
        'object_list': headlines,
    }
    return render(request, "news/opinion.html", context)


def article_detail(request):
    if request.method == 'POST':
        a = request.POST.get('linked', False)
        article_link = str(a)
        article = Article(article_link)
        article.download()
        article.parse()
        #nltk.download('punkt')
        article.nlp()
    return render(request, "news/article.html", {"article": article, "a": article_link})




from frontend.models import Event, Podcast, Product
from django.shortcuts import render, redirect
from django.contrib import messages
from . import views

# Create your views here.
def landing(request):
    context = {
        'all_events': Event.objects.all(),
        'spring_events': [],
        'summer_events': [],
        'fall_events': [],
        'winter_events': []
    }

    for event in context['all_events']:
        if event.season == 'Spring':
            context['spring_events'].append(event)
            print(event.month)
        if event.season == 'Summer':
            context['summer_events'].append(event)
        if event.season == 'Fall':
            context['fall_events'].append(event)
        if event.season == 'Winter':
            context['winter_events'].append(event)

    springEvt = []
    for event in context['spring_events']:
        springEvent = Event.objects.get(name=event)
        springEvt.append(springEvent)
    context['spring_events'] = springEvt 
    summerEvt = []
    for event in context['spring_events']:
        summerEvent = Event.objects.get(name=event)
        summerEvt.append(summerEvent)
    context['spring_events'] = summerEvt 
    fallEvt = []
    for event in context['fall_events']:
        fallEvent = Event.objects.get(name=event)
        fallEvt.append(fallEvent)
    context['fall_events'] = fallEvt 
    winterEvt = []
    for event in context['winter_events']:
        winterEvent = Event.objects.get(name=event)
        winterEvt.append(winterEvent)
    context['winter_events'] = winterEvt 

    print(context['spring_events'])

    return render(request, 'landing.html', context)

def about(request):
    return render(request, 'about.html')

def news(request):
    return render(request, 'news.html')

def podcast(request):
    context = {
        'all_podcasts': Podcast.objects.all(),
    }

    print(context['all_podcasts'])
    print('-----')

    all_podcasts = context['all_podcasts'].reverse()
    print(all_podcasts)

    context['all_podcasts'] = all_podcasts

    return render(request, 'podcast.html', context)

def store(request):

    context = {
        'all_products': Product.objects.all()
    }

    if len(context['all_products']) <= 0:
        return render(request, 'store-temp.html', context)
    else:

        all_products = context['all_products'].reverse()
        context['all_products'] = all_products

        return render(request, 'store.html', context)


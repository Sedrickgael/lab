from django.shortcuts import render
from django.core.paginator import Paginator
from . import models


# Create your views here.
def index(request):
    projets = models.Projet.objects.filter(status=True)
    page = request.GET.get('page', 1)
    paginator = Paginator(projets, 1)
    try:
        projets = paginator.page(page)
    except PageNotAnInteger:
        projets = paginator.page(1)
    except EmptyPage:
        projets = paginator.page(paginator.num_pages)

    datas = {
        'projets' : projets,
    }
    return render(request, 'index.html', datas)


def topic(request, projet_id):
    projet = models.Projet.objects.get(id=projet_id)
    if request.method == 'POST':
        reply = request.POST.get('reply')
        critique = models.Critique()
        critique.user = request.user
        critique.project = projet
        critique.save()
    datas = {
        'projet':projet,
    }
    return render(request, '02_topic.html', datas)
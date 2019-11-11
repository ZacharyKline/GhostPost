from django.shortcuts import render, HttpResponseRedirect, reverse
from ghostPost.models import BoastnRoast
from ghostPost.forms import BoastorRoast
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt


def index(request):
    html = 'index.html'
    data = BoastnRoast.objects.all().order_by('-post_time')

    return render(
        request, html, {'data': data}
    )


def upvoting(request, id):
    try:
        post = BoastnRoast.objects.get(id=id)
    except BoastnRoast.DoesNotExist():
        return HttpResponseRedirect(reverse('homepage'))
    post.total_votes += 1
    post.save()
    return HttpResponseRedirect(reverse('homepage'))


def best_view(request):
    html = 'loved.html'
    data = BoastnRoast.objects.all().order_by('-total_votes')

    return render(
        request, html, {'data': data}
    )


def worst_view(request):
    html = 'hated.html'
    data = BoastnRoast.objects.all().order_by('total_votes')
    return render(
        request, html, {'data': data}
    )


def downvoting(request, id):
    try:
        post = BoastnRoast.objects.get(id=id)
    except BoastnRoast.DoesNotExist():
        return HttpResponseRedirect(reverse('homepage'))
    post.total_votes -= 1
    post.save()
    return HttpResponseRedirect(reverse('homepage'))


def boast_view(request):
    html = 'boasts.html'
    data = BoastnRoast.objects.filter(boast=True).order_by('-post_time')
    return render(request, html, {'data': data})


def roast_view(request):
    html = 'roasts.html'
    data = BoastnRoast.objects.filter(boast=False).order_by('-post_time')
    return render(request, html, {'data': data})


def postit(request):
    html = 'post.html'
    if request.method == 'POST':
        form = BoastorRoast(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            BoastnRoast.objects.create(
                boast=data['boast'],
                message=data['message']
            )
        return HttpResponseRedirect(reverse('homepage'))
    form = BoastorRoast()
    return render(request, html, {'form': form})


@csrf_exempt
def deletepost(request, secret_code):
    try:
        if request.method == 'DELETE':
            query = BoastnRoast.objects.get(secret_code=secret_code)
            query.delete()
            return HttpResponse('Deleted')
        return HttpResponse('Whoops')
    except BoastnRoast.DoesNotExist:
        return HttpResponseNotFound()

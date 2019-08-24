from django.shortcuts import render, HttpResponse, redirect
from .models import Network, Show
from datetime import datetime
from django.contrib import messages


def add_show(request):
    return render(request, 'main/add_show.html')

def create_show(request):
    # pass the post data to the method we wrote and save the response in a variable called errors
    errors = Show.objects.basic_validator(request.POST)
    # check if the errors in the dictionary has anything in it
    if len(errors) > 0:
        # if the errors in the dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/shows/new')
    else:
        if request.method == 'POST':
            print("checking...")
            post = request.POST
            title = post['title']
            print(title)
            new_network = Network.objects.create(name=request.POST['network'])
            network = new_network
            print(network)
            release_date = post['releaseDate']
            print(release_date)
            description = post['description']
            print(description)
            new_show = Show.objects.create(title=title, network=network, release_date=release_date, description=description)
            print("\n\n\n", new_show)
            return redirect('/shows')

def all_shows(request):
    context = {
        "shows": Show.objects.all()
    }
    return render(request, 'main/all_shows.html', context)

def edit(request, showId):
    show = Show.objects.get(id=showId)
    convertedTime = datetime.strftime(show.release_date, "%m/%d/%Y")
    context = {
        "show": show,
        "releaseDate": convertedTime,
    }
    print(context)
    return render(request, 'main/edit_show.html', context)

def update(request, showId):
    if request.method == "POST":
        show_update = Show.objects.get(id=showId)
        show_update.title = request.POST['title']
        new_network = Network.objects.create(name=request.POST['network'])
        show_update.network = new_network

        if request.POST['releaseDate'] != "":
            show_update.release_date = request.POST['releaseDate']
        if request.POST['description'] != "":
            show_update.description = request.POST['description']
        
        show_update.save()
        return redirect(f'/shows/{showId}')

def show_id(request, showId):
    show = Show.objects.get(id=showId)
    updated = datetime.strftime(show.updated_at, "%B %d, %Y %I:%M %p")
    convertedTime = datetime.strftime(show.release_date, "%m/%d/%Y")
    context = {
        "show": show,
        "updated": updated,
        "releaseDate": convertedTime
    }
    return render(request, 'main/show_by_id.html', context)

def delete(request, showId):
    showToDelete = Show.objects.get(id = showId)
    showToDelete.delete()
    return redirect('/shows')




from django.shortcuts import render,redirect
import random

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    return render(request, "encyclopedia/entry.html", {
        "entry": util.get_entry(title),
        "title": title
    })

def search(request):
       query = request.GET.get('q', '')
       all_entries = util.list_entries()
       if query in all_entries:
           return redirect('entry', title=query)
       else:
           # Filter entries that contain the query as a substring
           search_results = [entry for entry in all_entries if query.lower() in entry.lower()]
           return render(request, 'encyclopedia/search_results.html', {
               'search_results': search_results,
               'query': query
           })
       
def random_page(request):
    all_entries = util.list_entries()
    random_entry = random.choice(all_entries)
    return redirect('entry', title=random_entry)

def new_page(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title in util.list_entries():
            return render(request, 'encyclopedia/new_page.html', {
                'error': 'This entry already exists.'
            })
        else:
            util.save_entry(title, content)
            return redirect('entry', title=title)
    else:
        return render(request, 'encyclopedia/new_page.html')
    
def edit_page(request, title):
    if request.method == "POST":
        content = request.POST["content"]
        util.save_entry(title, content)
        return redirect("entry", title=title)  # Assuming you have a view function named 'entry' to display the saved Markdown page
    else:
        content = util.get_entry(title)
        if content is None:
            return render(request, "encyclopedia/error.html", {"message": "Page not found."})
        else:
            return render(request, "encyclopedia/edit_page.html", {"title": title, "content": content})
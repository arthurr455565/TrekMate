from django.shortcuts import render, get_object_or_404
from .models import Trek

# List all treks with optional search
def trek_list(request):
    treks = Trek.objects.all()
    query = request.GET.get('q')
    if query:
        treks = treks.filter(name__icontains=query)
    return render(request, 'treks/trek_list.html', {'treks': treks})

# Trek details by slug
def trek_detail(request, slug):
    trek = get_object_or_404(Trek, slug=slug)
    return render(request, 'treks/trek_detail.html', {'trek': trek})

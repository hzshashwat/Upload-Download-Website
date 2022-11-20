from django.shortcuts import render, redirect
from .models import Document

# Create your views here.
def model_form_upload(request):
    if request.method == 'POST':
        description = request.POST['description']
        document = request.FILES['document']
        for filename, file in request.FILES.items():
            type = filename
            name = file
        Document.objects.create(description=description, name=name, type=type, document=document)
        return redirect('home')
    else:
        return render(request, 'model_form_upload.html')

def homeview(request):
    return render(request, 'homepage.html')

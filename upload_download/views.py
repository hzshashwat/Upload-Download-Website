from django.shortcuts import render, redirect
from .models import Document
from django.views import View

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

class DownloadView(View):
    def get(self, request, pk):
        fileobj=Document.objects.get(id = pk)
        context = {'files' : fileobj}
        return render(request,'download.html',context=context)

class DownloadAllView(View):
    def get(self, request):
        fileobj=Document.objects.all()
        #Similarlly, we can pass some parameter and filter the results through it.
        context = {'files' : fileobj}
        return render(request,'download_all.html',context=context)
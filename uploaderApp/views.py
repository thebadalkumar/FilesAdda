from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from .models import File
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .forms import UploadForm

class FileUploader(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("login")
        form = UploadForm()
        return render(request, 'fileUploader/index.html', {'form': form})

    def post(self, request):
        if not request.user.is_authenticated:
            return JsonResponse({"data":"Method Not Allowed Here"})
        if request.method=='POST':
            form = UploadForm(request.POST, request.FILES)
            title = request.POST.get("title",None)
            if form.is_valid():
                frm = form.save(commit=False)
                frm.user = request.user
                if title:
                    ext = ""
                    if "." in frm.file.url:
                        ext = "."+frm.file.url.split(".")[-1]
                    frm.file.name = title+ext
                frm.save()
                return JsonResponse({'data':'Data uploaded'})
            else:
                return JsonResponse({'data':'Something went wrong!!'})

def viewFile(request, url):
    file = get_object_or_404(File,url = url, is_delete=False)
    return render(request, "fileUploader/file.html", {"file":file})

@login_required
def FileView(request):
    files = File.objects.filter(user = request.user, is_delete=False)
    context = {
        "files" : files
    }
    return render(request, "fileUploader/myfiles.html", context)

@login_required
def favFileView(request):
    files = File.objects.filter(user = request.user, is_delete=False, is_fav=True)
    context = {
        "files" : files
    }
    return render(request, "fileUploader/myfavfiles.html", context)

@login_required
def remFileView(request):
    files = File.objects.filter(user = request.user, is_delete=True)
    context = {
        "files" : files
    }
    return render(request, "fileUploader/myremovedfiles.html", context)

@login_required
def removeFile(request):
    id = request.POST["id"]
    file = File.objects.get(id = id)
    file.is_delete = True
    file.save()
    return JsonResponse({"data":True})

@login_required
def deleteFile(request):
    id = request.POST["id"]
    file = File.objects.get(id = id)
    file.delete()
    return JsonResponse({"data":True})

@login_required
def restoreFile(request):
    id = request.POST["id"]
    file = File.objects.get(id = id)
    file.is_delete = False
    file.is_fav = False
    file.save()
    return JsonResponse({"data":True})

@login_required
def makeFav(request):
    id = request.POST["id"]
    file = File.objects.get(id = id)
    if file.is_fav:
        file.is_fav = False
    else:
        file.is_fav = True
    file.save()
    return JsonResponse({"data":file.is_fav})
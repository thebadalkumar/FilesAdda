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
            return redirect("/")
        form = UploadForm()
        return render(request, 'fileUploader/index.html', {'form': form})

    def post(self, request):
        if request.method=='POST':
            form = UploadForm(request.POST, request.FILES)
            if form.is_valid():
                frm = form.save(commit=False)
                frm.user = request.user
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
def removeFile(request):
    id = request.POST["id"]
    file = File.objects.get(id = id)
    file.is_delete = True
    file.save()
    return JsonResponse({"data":True})
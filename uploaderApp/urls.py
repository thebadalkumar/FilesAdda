from distutils.filelist import FileList
from django.urls import path
from . import views

urlpatterns = [
    path('', views.FileUploader.as_view(), name='file-uploader'),
    path('files/', views.FileView, name="file-view"),
    path('del-files/', views.removeFile, name="del-file"),
]
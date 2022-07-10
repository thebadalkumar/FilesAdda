from django.views import generic
from django.urls import reverse_lazy
from authApp.forms import SignupForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

class SignUp(generic.CreateView):
    form_class = SignupForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        messages.success(self.request, "Account created successfully. Login to continue...")
        return super().form_valid(form)
@login_required
def profile(request):
    form = ProfileUpdateForm(instance=request.user.profile)
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile) 
        if form.is_valid():
            form.save()
            messages.success(request, f'Profile picture has been updated!')
            return redirect('profile')
    return render(request, "profile.html", {"form":form})

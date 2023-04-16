from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView,TemplateView,View
from .models import PostModel,Profile
from django.urls import reverse_lazy
from .forms import LoginForm, PasswordChangeForm, UserRegisterFrom,UpdateUserForm, UpdateProfileForm
from django.contrib.auth.views import LoginView,PasswordChangeView,PasswordResetView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

class PostModelListView(LoginRequiredMixin, ListView):
    model = PostModel
    template_name = "list.html"
    context_object_name = 'posts'

    
    # def get_context_data(self, **kwargs):
    #     context=  super().get_context_data(**kwargs)
    #     context ["posts"] = context['posts'].filter(created_by=self.request.user)
    #     context ['posts'] = context['posts'].filter(done = False).count()
    

class PostModelDetailView(LoginRequiredMixin, DetailView):
    model = PostModel
    template_name = "detail.html"
    context_object_name= 'post'
    fields = "__all__"
    

class PostCreateView(LoginRequiredMixin, CreateView):
    model = PostModel
    template_name = "new.html"
    fields = "title","body", "done",


    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)



class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = PostModel
    template_name = "update.html"
    fields = ["title", "body",'done']


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = PostModel
    template_name = "delete.html"
    success_url = reverse_lazy("list")
        

class RegisterView(CreateView):
    template_name = "register.html"
    success_url = reverse_lazy('login')
    form_class = UserRegisterFrom
    initial = {'key': 'value'}

    

    
class LogInView(LoginView):
    template_name= 'login.html'
    success_url= reverse_lazy('list')
    form_class = LoginForm

class PasswordChange(PasswordChangeView):
    template_name= 'password_change.html'
    success_url= reverse_lazy('login')
    form_class = PasswordChangeForm
    

# class ProfileView(LoginRequiredMixin,DetailView):
#     model = ProfileModel
#     template_name = "profile.html"
#     context_object_name= 'profile'

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'profile.html', {'user_form': user_form, 'profile_form': profile_form})
# class ProfileEditView(LoginRequiredMixin,UpdateView):
#     model = ProfileModel
#     fields = "__all__"
#     template_name = "edit_profile.html"
    # success_url= reverse_lazy("profile")
    
# class CreateProfileView(LoginRequiredMixin,CreateView):
#     model = ProfileModel
#     form_class = UpdateProfileForm
#     template_name = "create_profile.html"
#     success_url= reverse_lazy("profile")
    
class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'password_reset.html'
    email_template_name = 'password_reset_email.html'
    subject_template_name = 'password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('list')

from django.contrib.auth import login, get_user_model
from django.contrib.auth.views import LogoutView
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, DetailView

from accounts.form import RegisterForm


class RegisterView(CreateView):
    model = get_user_model()
    template_name = 'user_create.html'
    form_class = RegisterForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if not next_url:
            next_url = self.request.POST.get('next')
        if not next_url:
            next_url = reverse('webapp:photo_list')
        return next_url


class ProfileView(DetailView):
    model = get_user_model()
    template_name = "profile.html"
    context_object_name = "user_obj"


class CustomLogoutView(LogoutView):
    # def post(self, request, *args, **kwargs):
    #     user = request.user
    #     user.auth_token.delete()
    #     response = super().post(request, *args, **kwargs)
    #     response.delete_cookie("token")
    #     return response

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.core.handlers.wsgi import WSGIRequest
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator

from .models import User
from .forms import RegisterForm
from .tasks import send_register_email_task, delete_user


def register_view(request: WSGIRequest):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password1'],
                is_active=False,
            )

            # Подтверждение по email.
            domain = str(get_current_site(request))

            # send_register_email_task.delay(domain, user.id)
            send_register_email_task.apply_async(args=[domain, user.id])
            delete_user.apply_async(args=[user.id], countdown=20)

            return HttpResponseRedirect(reverse("login"))

    return render(request, 'registration/register-form.html', {'form': form})


def confirm_register_view(request: WSGIRequest, uidb64: str, token: str):
    username = force_str(urlsafe_base64_decode(uidb64))

    user = get_object_or_404(User, username=username)
    if default_token_generator.check_token(user, token):
        user.is_active = True
        user.save(update_fields=["is_active"])
        return HttpResponseRedirect(reverse("login"))

    return render(request, "registration/invalid_email_confirm.html", {"username": user.username})

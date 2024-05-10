from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django_otp.forms import OTPAuthenticationForm, OTPTokenForm
from django_otp.models import Device

# Mis clases:
from .forms import FormularioLogin
# class someView(LoginRequiredMixin, CreateView):
#     login_url = "/login/"

@login_required(login_url='/login/')
def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))

@require_http_methods(["GET", "POST"])
def login_web(request):
    contexto = {"formulario": FormularioLogin()}

    # Compruebo primero si es una petición GET:
    if request.method == "GET":
        
        return render(request, "login-usuario.html", contexto)
    else:
        formulario = FormularioLogin(request.POST)
        if formulario.is_valid():
            nom, apell, _, passwd = formulario.cleaned_data.values()
            obj_usr = authenticate(username=nom, password=passwd)

            if obj_usr is not None:
                #messages.success(request, "¡Login correcto!")
                login(request, obj_usr)
                return redirect("login")
            else:
                messages.error(request, "¡Login incorrecto!")
        return redirect("login")

@login_required
def otp_login_view(request):
    if request.method == 'POST':
        form = OTPTokenForm(request.POST)
        if form.is_valid():
            # OTP Token validation succeeded
            print("otp valido")
            return redirect('success_url')
        else:
            print("otp invalido")
    else:
        form = OTPTokenForm(request.user)
    return render(request, 'otp_login.html', {'form': form})


@require_http_methods(["GET", "POST"])
def registrar(request):
    pass



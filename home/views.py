from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# class someView(LoginRequiredMixin, CreateView):
#     login_url = "/login/"

@login_required(login_url='/login/')
def index(request):
    template = loader.get_template('home/index.html')
    context = {}
    return HttpResponse(template.render(context, request))



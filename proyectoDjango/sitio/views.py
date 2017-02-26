from django.shortcuts import render_to_response

def index(request):
    return render_to_response("index.html")
def proyecto(request):
     return render_to_response("proyectos.html")
def ayudantias(request):
    return render_to_response("ayudantias.html")
def curso(request):
    return render_to_response("curso.html")
def equipo(request):
    return render_to_response("equipo.html")
def semana(request):
    return render_to_response("semana.html")
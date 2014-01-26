#from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from datetime import datetime
from django.shortcuts import render_to_response

# Create your views here.

def index_view(request):
	cadena = "Hola mejorandola"
	return HttpResponse(cadena)

def post(request,id):
	return HttpResponse("Este es el post %s" %id)

def hora_actual(request):
	hora = datetime.now()
	user = "Renzo"
	rango = range(1,10)
	return render_to_response("template1.html", locals())


	#obtener la hora (forma larga)

	#ahora = datetime.now()
	#t = get_template("template1.html")
	#c = Context({"hora": ahora})
	#html = t.render(c)
	#return HttpResponse(html)
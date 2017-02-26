from django.conf.urls import url
from sitio import views 


urlpatterns = [
    url(r'^$',views.index),
    url(r'^semana/$',views.semana),
    url(r'^curso/$',views.curso),
    url(r'^equipo/$',views.equipo),
    url(r'^proyecto/$',views.proyecto),
    url(r'^ayudantias/$',views.ayudantias),

    

]


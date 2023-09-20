from django.shortcuts import render,redirect,get_object_or_404
from .personasForm import PersonaFormulario
from django.urls import reverse_lazy,reverse
from django.contrib import messages  # Importa el módulo de mensajes
from django.views.generic import DeleteView
from .models import Persona
from .personasEditForm import PersonaEdicionForm 


# Create your views here.
def Inicio(request):
    personas = Persona.objects.all()  # Consulta todos los registros de Persona

    context = {
        'personas': personas
    }

    return render(request, 'inicio.html', context)
def cargar_tabla_personas(request):
    personas = Persona.objects.all()  # Consulta todos los registros de Persona

    context = {
        'personas': personas
    }

    return render(request, 'inicio.html', context)
def Personas(request):
    form=PersonaFormulario(request.POST or None)
    #validamos el fomrulario
    if form.is_valid():
        form_data = form.cleaned_data
        print(form_data)
        #guardamos los datos enviados por el form a variables auxiliares
        aux1=form_data.get('nombre')        
        aux2=form_data.get('apellido')        
        aux3=form_data.get('cedula')        
        aux4=form_data.get('direccion') 
        try:
            #guardamos la nueva persona
            obj = Persona(nombre=aux1,apellido=aux2,cedula=aux3,direccion=aux4)     
            obj.save()
            messages.success(request, 'Los datos se han guardado exitosamente.')
            personasAll = Persona.objects.all()  # Consulta todos los registros de Persona
            return render(request,'inicio.html',{'personas':personasAll})
        except Exception as e:
            #print(error)
            # Si ocurre un error al guardar, agrega un mensaje de error
            messages.error(request, f'Ocurrió un error al guardar los datos: {str(e)}')
            

        #return redirect('Inicio')

    context={
        "titulo":"Formulario",
        "form":form
    }
    return render(request,"personas.html",context)

class EliminarPersonaView(DeleteView):
    model = Persona
    template_name = 'eliminar_persona.html'  # Crea esta plantilla
    success_url = reverse_lazy('Inicio')  # Redirige después de eliminar
    def delete(self, request, *args, **kwargs):
        # Antes de eliminar, obtén la persona que se eliminará
        persona = self.get_object()
        
        # Agrega un mensaje de éxito
        #messages.success(request, f'La persona {persona.nombre} {persona.apellido} se ha eliminado con éxito.')
        messages.success(request, 'Los datos se han eliminado con éxito')
        personasAll = Persona.objects.all()  # Consulta todos los registros de Persona
        return render(request,'inicio.html',{'personas':personasAll})

        # Procede con la eliminación llamando al método 'delete' de la superclase
        #return super().delete(request, *args, **kwargs)

def eliminar_persona(request, id):
    persona = get_object_or_404(Persona, pk=id)

    if request.method == 'POST':
        persona.delete()
        
    
    personasAll = Persona.objects.all()  # Consulta todos los registros de Persona

    context = {
        'personas': personasAll
    }

    return redirect('Inicio')

def editar_persona(request, persona_id):
    persona = get_object_or_404(Persona, pk=persona_id)
    print(persona)

    if request.method == 'POST':
        form = PersonaEdicionForm(request.POST, instance=persona)  # Pasa la instancia al formulario
        if form.is_valid():
            form.save()
            messages.success(request, 'Los datos se han editado exitosamente.')
            personasAll = Persona.objects.all()  # Consulta todos los registros de Persona
            return redirect(reverse('Inicio'))
           # return render(request,'inicio.html',{'personas':personasAll})
            #return redirect('Inicio')
    else:
        form = PersonaEdicionForm(instance=persona)  # Pasa la instancia al formulario

    context = {
        "titulo": "Editar Persona",
        "form": form
    }

    return render(request, "editar_persona.html", context)


from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Itm
from django.template import loader
from .forms import ItmForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

# Create your views here.
def Mukul(request):
    Itm_list = Itm.objects.all()
    template=loader.get_template('food1/Mukul.html')
    context={
        'Itm_list':Itm_list,
    }
    
    return HttpResponse(template.render(context,request))
class MukulClassView(ListView):
    model = Itm;
    template_name = 'food1/Mukul.html'
    context_object_name = 'Itm_list'


def detail(request,Itm_id):
    Its = Itm.objects.get(pk=Itm_id)  

    context = {
        'Itm':Its,
    }
    return render(request,'food1/detail.html',context) 


class FoodDetail(DetailView):
    model = Itm;
    template_name = 'food1/detail.html'
    


def create_Itm(request):
    form = ItmForm(request.POST or None)


    if form.is_valid():
        form.save()
        return redirect('food1:Mukul')
       # return redirect('food1:detail') It should have returned to detail page of that particular item

    return render(request,'food1/Itm-form.html',{'form':form})

class CreateItm(CreateView):
    model = Itm ;
    fields = ['Itm_name','Itm_dec','Itm_price','Itm_image' ]
    template_name = 'food1/Itm-form.html'
    
    def form_valid(self,form):
        form.instance.user_name = self.request.user

        return super().form_valid(form)
'''
def update_Itm(request,id):
    Its = Itm.objects.get(id=id)
    form = ItmForm(request.POST or None,instance=Itm)

    if form.is_valid():
        form.save()
        return redirect('food:Mukul')
    return render(request,'food1/Itm-form.html',{'form' : form,'Itm':Its})

def delete_Itm(request,id):
    Its = Itm.objects.get(id=id)

    if request.method == "POST":
        Its.delete()
        return redirect('food1:Mukul')
    return render(request,'food1/Itm-delete.html',{'Itm':Its})


'''






from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.db.models import Sum,Count


# Create your views here.
def home(request):
    people=People.objects.all()
    customers = people.values("name","email","country").annotate(game_count=Count('email')).annotate(total=Sum('score'))
    paginator = Paginator(customers, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={'users':page_obj,}
    return render(request,'home.html',context)
    
def createRecord(request):
    if request.method == 'POST':
        form = PeopleForm(request.POST)
        if form.is_valid():
            form.save()
            person=form.cleaned_data.get('name')
            
            messages.success(request,'Account was created for '+person)
            return render(request, 'create_record.html', {'form': PeopleForm(request.GET)})
    else:
        form = PeopleForm()
    return render(request,'create_record.html', {'form': form})


def DeleteRecord(request,pk):
    import pdb
    # pdb.set_trace()
    person=People.objects.get(id=pk)
    if request.method=='GET':
        person.delete()
        return redirect('/')
    context={'item':person}
    return render(request,'delete.html',context)

def UpdateRecord(request,pk):
    person=People.objects.get(id=pk)
    form=PeopleForm(instance=person)
    if request.method=='POST':
        form=PeopleForm(request.POST,instance=person)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'create_record.html',context)





def users(request):
	users = People.objects.all() #queryset containing all movies we just created
	paginator = Paginator(movies, 3)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	
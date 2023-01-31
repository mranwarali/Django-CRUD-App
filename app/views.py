from django.shortcuts import render,redirect
from .models import *
# Create your views here.

def InsertPageView(request):
    return render(request,"app/insert.html")


def InsertData(request):
    # Data come from HTML to View
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    contact = request.POST['contact']

    # Creating Object of Model Class
    # Inserting Data into Table
    newuser = Student.objects.create(Firstname=fname,Lastname=lname,    
                                        Email=email,Contact=contact)

    # After Insert render on Showpage view
    return redirect('showpage')

#show page view
def ShowPage(request):
    #select * from tablename
    # to fetching all data of thee table
    all_data = Student.objects.all()
    return render(request,"app/show.html",{'key1':all_data})

# edit page vieww
def EditPage(request,pk):
    get_data = Student.objects.get(id=pk)
    return render(request,"app/edit.html",{'key2':get_data})

# update data view
def UpdateData(request,pk):
    udata = Student.objects.get(id=pk)
    udata.Firstname = request.POST['fname']
    udata.Lastname = request.POST['lname']
    udata.Email = request.POST['email']
    udata.Contact = request.POST['contact']
# query for update
    udata.save()
    # render on Showpage view
    return redirect('showpage')

# DELETE DATA view
def DeleteData(request,pk):
    ddata = Student.objects.get(id=pk)
    #query for delete
    ddata.delete()
    #render on show page
    return redirect('showpage')

    return redirect('showpage')
     
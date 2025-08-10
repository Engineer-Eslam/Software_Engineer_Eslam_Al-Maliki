from django.shortcuts import render

def index(request):
    name={"fname":"Eslam Al-Maliki"}
    return render(request, 'index.html',name)

def home(request):
    return render(request,'home.html')

def list_students(request):
    students = {
        'name': 'Eslam Al-Maliki',
        'marks': [98,95,97],
        'eachsub':{'Softwear Engineering':98,
                    'Image Processing':95,
                    'Client and Server Programming':97
                    }}
    return render(request,'showstudents.html',students)

def edit_students (request):
    students={
        "total":290,
        'marks':{'Softwear Engineering':98,
                    'Image Processing':95,
                    'Client and Server Programming':97
                    }}
    return render(request, 'editstudents.html', students)

def del_students(request):
    return render(request,'deletestudents.html')
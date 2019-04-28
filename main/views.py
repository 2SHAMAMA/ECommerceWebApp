from django.shortcuts import render_to_response,redirect
from django.shortcuts import render
from django.http import HttpResponse
from .models import Category
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView

# Create your views here.

'''def Category(request):

    cat=Category.object.all()
    return HttpResponse(cat) 
   ''' 
    
    #return HttpResponse("Hello")
	#return render(request,'YAB/Categories.html')
def login(request):
	return render(request,'YAB/login.html')

#Class login(TemplateView):
#template_name='YAB/login.html' 
'''    logout(request)
    username = "abc"
    password = 123
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/main/')
'''
    

def homepage(request):
    #return HttpResponse("Hello")
    return render(request,'YAB/index.html')

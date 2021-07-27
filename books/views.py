from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import SignupForm,LoginForm,UpdateForm,ChangePasswordForm
from .models import Register
from django.contrib import messages
from django.contrib.auth import logout as logouts

# Create your views here.
def pages(request):

	return HttpResponse("these are my books")

def index(request):
	name="arya"
	return render(request, 'index.html', {'data':name})

def signup(request):
	if request.method=='POST':
		form=SignupForm(request.POST,request.FILES)
		if form.is_valid():
			name=form.cleaned_data['Name']
			age=form.cleaned_data['Age']
			email=form.cleaned_data['Email']
			

			photo=form.cleaned_data['Photo']
			password=form.cleaned_data['Password']
			confirmpassword=form.cleaned_data['ConfirmPassword']
			user=Register.objects.filter(Email=email).exists()
			

			if user:
				messages.success(request,'email already exist')
				return redirect('/signup')
			elif password!=confirmpassword:
				messages.success(request,'successful')
				return redirect('/signup')
			else:
				tab=Register(Name=name,Age=age,Email=email,Password=password,Photo=photo)
				tab.save()
				messages.success(request,'Successful')
				return redirect('/')
	else:
		form=SignupForm()
	return render(request, 'signup.html', {'form':form})

def login(request):
	if request.method=='POST':
		form=LoginForm(request.POST)
		if form.is_valid():
			email=form.cleaned_data['Email']
			password=form.cleaned_data['Password']
			user=Register.objects.get(Email=email)
			if not user:
				messages.success(request,'Email does not exists')
				return redirect('/login')
			else:
				request.session['email']=email
				messages.success(request,'Login successful')
				return redirect('/home/%s' %user.id)
	else:
		form=LoginForm()
	return render(request,'login.html',{'form':form})

def home(request,id):
	user=Register.objects.get(id=id)
	return render(request,'home.html',{'user':user})

def update(request,id):
	user=Register.objects.get(id=id)
	form=UpdateForm(request.POST or None,request.FILES or None,instance=user)
	if form.is_valid():
		form.save()
		messages.success(request,'update successful')
		return redirect('/home/%s' % user.id)
	return render(request,'update.html',{'user':user, 'form':form})

def changepassword(request,id):
	user=Register.objects.get(id=id)
	if request.method=='POST':
		form=ChangePasswordForm(request.POST)
		if form.is_valid():
			oldpassword=form.cleaned_data['OldPassword']
			newpassword=form.cleaned_data['NewPassword']
			confirmpassword=form.cleaned_data['ConfirmPassword']
			if oldpassword!=user.Password:
				messages.success(request,'incorrect password')
				return redirect('/changepassword/%s' % user.id)
			elif newpassword!=confirmpassword:
				messages.success(request,'mismatch')
				return redirect('/changepassword/%s' % user.id)
			else:
				user.Password=newpassword
				user.save()
				messages.success(request,'password changed successfully')
				return redirect('/home/%s' % user.id)                                                                         
    
	else:
		form=ChangePasswordForm()

	return render(request,'changepassword.html',{'user':user, 'form':form})

def logout(request):
	logouts(request)
	messages.success(request,'logout successfuly')
	return redirect('/')
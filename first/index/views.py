from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import ListView
from django.views.generic import CreateView, DeleteView
from .models import add_news
from django.urls import reverse_lazy

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

from django.views.generic import View


#def display(request):
#	return HttpResponse("test a32")

class Display(ListView):
	template_name = "index_view/list-post.html"
	queryset = add_news.objects.all()

class AddPost(CreateView):
	template_name = "index_view/index.html"
	model = add_news
	fields = ['topic', 'text_message', 'date_created', 'author']
	success_url = reverse_lazy('main')

class RemovePost(DeleteView):
	model = add_news
	success_url = reverse_lazy('main')


class Registration(View):
	template_name="index_view/register.html"
	def get(self, request):
		form = UserCreationForm(None)
		return render(request,self.template_name,{'form':form})
	def post(self, request):
		form = UserCreationForm(request.POST) #,instance=request.user
		if form.is_valid():
			user = form.save(commit=False)
			user.username = form.cleaned_data['username']
			if form.cleaned_data['password1'] == form.cleaned_data['password2']:
				user.set_password(form.cleaned_data['password1'])
			user.save()
			return redirect(reverse_lazy('main'))

class Login(View):
	template_name = "index_view/login.html"
	def get(self,request):
		return render(request,self.template_name,{})

	def post(self,request):
		#authenticate, login
		username = request.POST['login']
		password = request.POST['pass']
		user = authenticate(user=username,password=password)
		if user is not None:
			if user.is_active:
				login(request,user)
				return redirect(reverse_lazy("main"))





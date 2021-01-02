from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

from .forms import LoginForm
from chat.forms import MessageForm
from chat.models import MessageModel


def register_view(request):
	if request.user.is_authenticated:
		return redirect('user_home')

	if request.method == 'POST':
		 register_form = UserCreationForm(request.POST)
		 if register_form.is_valid():
		 	register_form.save()
	else:
		register_form = UserCreationForm()

	context = {'register_form': register_form}
	return render(request, 'register.html', context)


def login_view(request):
	if request.user.is_authenticated:
		return redirect('user_home')

	form = LoginForm()
	context = {'login_form':form,}
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username = username ,password = password)
		if user is not None:
			login(request, user)
			return redirect('user_home')
		else:
			info = 'Nie poprawny login lub chasło!'
			context = {'login_form': form,
						'info': info,
						}
	
	return render(request, 'login_page.html', context)


def logout_view(request):
	logout(request)
	return redirect('login')


def user_home_view(request):
	if not request.user.is_authenticated:
		return redirect('login')

	return render(request, 'accounts/loggedin_user_base.html', {'username':request.user.username,'profile_photo': request.user.profile.image,})

def user_conversations_view(request):
	if not request.user.is_authenticated:
		return redirect('login')

	conversations = request.user.profile.conversations.all()
	context = { 'profile_photo'	: request.user.profile.image,
				'conversations'	: conversations,
				'my_profile'	: request.user.profile,
				}
	return render(request, 'accounts/user_conversations.html',context)


def user_messages_view(request, conv = None):
	if not request.user.is_authenticated:
		return redirect('login')

	if conv is None:
		return redirect('conversations')

	user = request.user
	conversation = user.profile.conversations.filter(name=conv)[0]
	form = MessageForm()
	if request.method == "POST":
		message = request.POST['message']
		new_message = MessageModel(conversation=conversation,message=message)
		new_message.save()
		user.profile.messages.add(new_message)
	
	return render(request,'accounts/user_messages.html', { 'profile_photo'	: request.user.profile.image, 'conversation':conversation,"message_form":form,})

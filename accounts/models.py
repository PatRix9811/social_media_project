from django.db import models
from django.contrib.auth.models import User


from chat.models import ConversationModel, MessageModel


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	image = models.ImageField(default = 'default.png', upload_to = f'profile_pictures/')
	conversations = models.ManyToManyField(ConversationModel, blank = True)
	messages = models.ManyToManyField(MessageModel, blank = True)


	def __str__(self):
		return f'{self.user.username} < {self.user.email} >'
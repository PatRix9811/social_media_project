from django.db import models


class ConversationModel(models.Model):
	name = models.CharField(max_length = 100)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Konwersacja'
		verbose_name_plural = 'Konwersacje'


class MessageModel(models.Model):
	conversation = models.ForeignKey(ConversationModel, on_delete = models.CASCADE, related_name= 'messages')
	message = models.TextField(max_length = 500)
	date =  models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.message

	class Meta:
		verbose_name = 'Wiadomość'
		verbose_name_plural = 'Wiadomości'

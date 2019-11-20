from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .forms import ContactForm

class HelloView(APIView):
	permission_classes=(IsAuthenticated,)
	
	def get(self,request):
		content= {'message':'Hello,world'}
		return Response(content)



def get_contact(request):
	if request.method=='POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject=form.cleaned_data['subject']
			message=form.cleaned_data['message']
			sender=form.cleaned_data['sender']
			cc_myself=form.cleaned_data['cc_myself']
			recipients=['072bex448.tribikram@gmail.com']

			if cc_myself:
				recipients.append(sender)

			send_mail(subject, message, sender, recipients)
			return HttpResponse("Form successfully submitted")

	else:
		form = ContactForm()

	return render(request, 'contact.html', {'form':form})	
			

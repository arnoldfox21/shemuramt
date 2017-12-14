from django.core.urlresolvers import reverse
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import View
from social_auth.backends.exceptions import AuthFailed
from social_auth.views import complete



class AuthComplete(View):
	def get(self, request, *args, **kwargs):
		backend = kwargs.pop('backend')
		try:
			return complete(request, backend, *args, **kwargs)
		except AuthFailed:
			messages.error(request, "Your Google Apps domain isn't authorized for this app")
			return HttpResponseRedirect(reverse('login'))

class LoginError(View):
	def get(self, request, *args, **kwargs):
		return HttpResponse(status=401)
import json
import bcrypt
import jwt

from django.views import View
from django.http import HttpResponse, JsonResponse

from .models import Account
from test01.settings import SECRET_KEY

class SignUpView(View):
	def post(self, request):
		data = json.loads(request.body)
		try:    
			if Account.objects.filter(username=data['username']).exists():
				return JsonResponse({'message':'USERNAME_EXIST'}, status=401)
			Account.objects.create(
				username = data['username'],
				password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
			)
			return HttpResponse(status=200)
		except KeyError:
				return JsonResponse({'message':'INVALID_KEY'}, status=400)

class SignInView(View):
	def post(self, request):
		data = json.loads(request.body)
		try:
			if Account.objects.filter(username = data['username']).exists():
				account = Account.objects.get(username = data['username'])
				if bcrypt.checkpw(data['password'].encode('utf-8'), account.password.encode('utf-8')):
					access_token = jwt.encode({ 'username' : account.username}, SECRET_KEY, algorithm = 'HS256')
					return JsonResponse({'access_token':access_token.decode('utf-8')}, status=200)
				return HttpResponse(status=401)
			return HttpResponse(status=401)
		except KeyError:
			return JsonResponse({'message':'INVALID_KEY'}, status=400)

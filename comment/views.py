import json

from django.views import View
from django.http import HttpResponse, JsonResponse

from .models import Comment
from account.models import Account
from account.utils import login_required
#class CommentView(View):
#	def post(self, request):
#		data = json.loads(request.body)
#		try:
#			if Account.objects.filter(username = data['username']).exists():	
#				Comment.objects.create(
#					username = Account.objects.get(username=data['username']),
#					comment = data['comment']
#				)
#				return HttpResponse(status=200)
#			return JsonResponse({'message':'INVALID_USER'}, status=401)
#		except KeyError:
#			return JsonResponse({'message':'INVALID_KEY'},status=400)
#
#	def get(self, request):
#		data = json.loads(request.body)
#		comment_data = Comment.objects.filter(username = Account.objects.get(username=data['username']))
#		return JsonResponse({'comments':list(comment_data.values())}, status=200)
#

class CommentView(View):
	@login_required
	def post(self, request):
		data = json.loads(request.body)
		try:
			Comment.objects.create(
				username = request.user,
				comment = data['comment']
				)
			return HttpResponse(status=200)
		except KeyError:
			return JsonResponse({'message':'INVALID_KEY'},status=400)

	def get(self, request):
		data = json.loads(request.body)
		comment_data = Comment.objects.filter(username = Account.objects.get(username=data['username']))
		return JsonResponse({'comments':list(comment_data.values())}, status=200)

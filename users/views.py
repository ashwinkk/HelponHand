from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User
import json

# Create your views here.
@csrf_exempt
def userLogin(userrequest):
	response = {'status': False}
	if userrequest.method == 'POST':
		datas = userrequest.body
		print datas
		datas = json.loads(datas)
		results = User.objects.filter(phonenum=datas['number'])
		print results
		if len(results)==0:
			try:
				user = User(username=datas['name'],phonenum=datas['number'],regid=datas['id'])
				user.save()
				response['status'] = True
			except:
				pass
	return JsonResponse(response)
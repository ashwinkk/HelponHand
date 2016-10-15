from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .gcmreqs import getContactsNearby,emergencyContacts
from .models import LocCache
import requests,json

# Create your views here.
@csrf_exempt
def checkIn(request):
	response = {'status': False}
	if request.method == 'POST':
		datas = request.body
		datas = json.loads(datas)
		try:
			location = LocCache(phonenum=datas['num'],lat=float(datas['lat']),lon=float(datas['lon']))
			location.save()
			response['status']=True
		except:
			pass		
	return JsonResponse(response)

@csrf_exempt
def help(request):
	respo = {'status':False}
	if request.method=='POST':
		datas = request.body
		url = "https://gcm-http.googleapis.com/gcm/send"
		datas = json.loads(datas)
		print datas,type(datas)
		headers={'Content-Type':'application/json',"Authorization":"key=AIzaSyDkSBG9Bm5VztfMZ8meDcv9HFqSKBqY_uY"}
		regids = getContactsNearby(datas['name'],datas['lat'],datas['lon'])
		notifdata = {'data':{'name':datas['name'],'lat':datas['lat'],'lon':datas['lon']},'registration_ids':regids}
		notifdata = json.dumps(notifdata)
		response = requests.post(url,data=notifdata,headers=headers)
		print response.text
		contacts = datas['contacts'].values()
		regids = emergencyContacts(contacts,datas['name'],datas['lat'],datas['lon'])
		notifdata = {'data':{'name':datas['name'],'lat':datas['lat'],'lon':datas['lon']},'registration_ids':regids}
		notifdata = json.dumps(notifdata)
		response = requests.post(url,data=notifdata,headers=headers)
		print response.text
		respo['status']=True
	return JsonResponse(respo)
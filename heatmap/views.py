from django.shortcuts import render
from helpreq.models import LocCache
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .matrix import matrixmult
import random,json
from math import asin,cos,pi,sin,pow,floor

# Create your views here.
@csrf_exempt
def getlats(latlonreq):
	datas = latlonreq.body
	print datas
	datas = json.loads(datas)
	lat1 = float(datas['lat'])
	lon1 = float(datas['lon'])
	print lat1,lon1
	lats=lat1
	lons=lon1
	r=0.2/6371
	rad2deg=180/pi
	deg2rad=1/rad2deg
	lat1=float(lat1)
	lon1=float(lon1)
	latmax = lat1+rad2deg*r
	latmin = lat1-rad2deg*r
	latT=asin(sin(deg2rad*lat1)/cos(r))
	dlon=asin(sin(r)/cos(deg2rad*lat1))
	lonmax=lon1+rad2deg*dlon
	lonmin=lon1-rad2deg*dlon
	hh = 1
	mm = 45
	print hh,mm
	predict = [[1,pow(hh,1.173),mm]]
	print predict
	theta = [[0.8861797427738332],[0.5060750165138904],[0.08407162747635893]]
	size = matrixmult(predict,theta)
	size = floor(size[0][0])
	print size
	size = int(size)
	i= size
	locarray = []
	i=size
	while i>0:
		r = random.random()
		r = r*latmax;
		while(r<latmin or r>latmax):
			r = random.random()
			r = r*latmax
		latitude = r
		r = random.random()
		r = r*lonmax;
		while(r<lonmin or r>lonmax):
			r = random.random()
			r = r*lonmax;
		longitude = r
		point = {'lat':latitude,'lng':longitude}
		locarray.append(point)
		i = i-1
	response = {'randlocs':locarray,'size':size}
	print response
	return JsonResponse(response)
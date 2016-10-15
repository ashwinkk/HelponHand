from math import asin,cos,pi,sin
from users.models import User
from .models import LocCache

def getContactsNearby(name,lat1,lon1):
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
	usersNearby = LocCache.objects.filter(lat__gte=latmin,lon__gte=lonmin,lat__lte=latmax,lon__lte=lonmax)
	regid = []
	for user in usersNearby:
		userdat = User.objects.filter(phonenum=user.phonenum)
		if userdat[0].regid not in regid:
			regid.append(userdat[0].regid)
	return regid

def emergencyContacts(econtacts,name,lats,lons):
	users=[]
	for num in econtacts:
		user = User.objects.filter(phonenum=num)
		if user:
			users.append(user[0])
	regid = []
	for user in users:
		if user.regid not in regid:
			regid.append(user.regid)
	print regid
	return regid
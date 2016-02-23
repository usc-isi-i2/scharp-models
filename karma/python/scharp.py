def alpha_numeric(m):
	return re.sub('[^A-Za-z0-9]+', ' ', m)

def uri_from_fields(fields):

	string = '_'.join(alpha_numeric(f.strip().lower()) for f in fields)

	if len(string) == len(fields)-1:
		return ''
	return string

def splitLocation(location):
	return re.search('[NS]',location).start()

def getLatitude(s,l):
	second = float(s[-2:])
	minute = float(s[-4:-2])
	degree = float(s[:-4])
	if l == "N":
		return str(degree+minute/60+second/3600)
	else:
		return str(-degree-minute/60-second/3600)	

def getLongitude(s,l):
	second = float(s[-2:])
	minute = float(s[-4:-2])
	degree = float(s[:-4])
	if l == "E":
		return str(degree+minute/60+second/3600)
	else:
		return str(-degree-minute/60-second/3600)

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


def ISOtime(s):
	MM_dict = {"JAN":"01","FEB":"02","MAR":"03","APR":"04","MAY":"05","JUN":"06","JUL":"07","AUG":"08","SEP":"09","OCT":"10","NOV":"11","DEC":"12"}
	return s[:4]+MM_dict[s[4:7]]+s[7:9]+"T"+s[9:11]+":"+s[11:]
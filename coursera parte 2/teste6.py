def fazAlgo(string):
	pos = len(string)-1
	string = string.upper()
	while pos >= 0:
		print(string[pos],end = "")
		pos = pos - 1

fazAlgo("paralelepipedo")
#ODEPIPELELARAP

def fazAlgo2(string):
	pos = 0
	string1 = ""
	string = string.lower()
	stringMa = string.upper()
	while pos < len(string):
		if pos % 2 == 0:
			string1 = string1 + stringMa[pos]
		else:
			string1 = string1 + string[pos]
		pos = pos + 1
	return string1

print(fazAlgo2("paralelepipedo"))
#PaRaLeLePiPeDo

def fazAlgo3(string):
	pos = 0
	string1 = ""
	while pos < len(string):
		if string[pos] != " ":
			string1 = string1 + string[pos]
		pos = pos + 1
	return string1

print(fazAlgo3("ISTO É UM TESTE"))
#ISTOÉUMTESTE

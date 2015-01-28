import urllib2
import json
def Conv(frm,to,amt):
	yql_base_url = "https://query.yahooapis.com/v1/public/yql"
	yql_query = 'select%20*%20from%20yahoo.finance.xchange%20where%20pair%20in%20("'+frm+to+'")'
	yql_query_url = yql_base_url + "?q=" + yql_query + "&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"
	try:
		yql_response = urllib2.urlopen(yql_query_url)
		try:
			yql_json = json.loads(yql_response.read())
			_output = amt * float(yql_json['query']['results']['rate']['Rate'])
			return _output
		except (ValueError, KeyError, TypeError):
			return "JSON format error"

	except IOError, e:
		if hasattr(e, 'code'):
			return e.code
		elif hasattr(e, 'reason'):
			return e.reason

print "get the codes from http://en.wikipedia.org/wiki/ISO_4217"
s1=raw_input("from code\n")
s2=raw_input("to code\n")
amt = int(raw_input("enter the amount"))
rate = Conv(s1,s2,amt)
print rate

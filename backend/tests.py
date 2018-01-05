
			Task remaining


- login.js
- django auth token

web color default: #9c27b0

{{ value|cut:" " }}

{{ value|center:"15" }}

{{ value|capfirst }}

{{ value|add:"2" }}
#If value is 4, then the output will be 6.

<img src="bar.png" alt="Bar"
     height="10" width="{% widthratio this_value max_value max_width %}" />

#If this_value is 175, max_value is 200, and max_width is 100, the image in the above example will be 88 pixels wide 
#(because 175/200 = .875; .875 * 100 = 87.5 which is rounded up to 88).

#important
{% include "name_snippet.html" with person="Jane" greeting="Hello" %}

{{ greeting }}, {{ person|default:"friend" }}!
#

{{ value|join:" // " }}
#If value is the list ['a', 'b', 'c'], the output will be the string "a // b // c".

{{ value|linebreaks }}
#If value is Joel\nis a slug, the output will be <p>Joel<br />is a slug</p>.

{{ value|linenumbers }}
# if value is:

# one
# two
# three

# the output will be:

# 1. one
# 2. two
# 3. three

{{ value|lower }}

#If value is Totally LOVING this Album!, the output will be totally loving this album!.

{{ value|make_list }}

#If value is the string "Joel", the output would be the list ['J', 'o', 'e', 'l']. If value is 123, the output will be the list ['1', '2', '3'].

{{ value|striptags }}

#If value is "<b>Joel</b> <button>is</button> a <span>slug</span>", the output will be "Joel is a slug".

{{ value|time:"H:i" }}

#If value is equivalent to datetime.datetime.now(), the output will be the string "01:23".

{{ blog_date|timesince:comment_date }}
# Formats a date as the time since that date (e.g., “4 days, 6 hours”).

# Takes an optional argument that is a variable containing the date to use as the comparison point 
# (without the argument, the comparison point is now). For example, if blog_date is a date instance representing midnight on 1 June 2006, 
# and comment_date is a date instance for 08:00 on 1 June 2006, then the following would return “8 hours”:
{{ conference_date|timeuntil:from_date }}

{{ value|title }}

#If value is "my FIRST post", the output will be "My First Post".

{{ value|truncatechars:9 }}

# If value is "Joel is a slug", the output will be "Joel i...".

{{ value|truncatewords:2 }}

# If value is "Joel is a slug", the output will be "Joel is ...".

# Newlines within the string will be removed.

{{ value|truncatechars_html:9 }}

# If value is "<p>Joel is a slug</p>", the output will be "<p>Joel i...</p>".

# Newlines in the HTML content will be preserved.

{{ value|truncatewords_html:2 }}

# If value is "<p>Joel is a slug</p>", the output will be "<p>Joel is ...</p>".

{{ value|urlize }}

# If value is "Check out www.djangoproject.com", the output will be 
# "Check out <a href="http://www.djangoproject.com" rel="nofollow">www.djangoproject.com</a>".

{{ value|urlizetrunc:15 }}

# If value is "Check out www.djangoproject.com", the output would be 
# 'Check out <a href="http://www.djangoproject.com" rel="nofollow">www.djangopr...</a>'.

{{ value|wordcount }}

# If value is "Joel is a slug", the output will be 4.

from re import sub
from decimal import Decimal

money = '$6,150,593.22'
value = Decimal(sub(r'[^\d.]', '', money))

# This has some advantages since it uses Decimal instead of float (which is better for representing currency) and it also avoids any locale issues by not hard-coding a specific currency symbol.

HTTP_100_CONTINUE
HTTP_101_SWITCHING_PROTOCOLS
Successful - 2xx
This class of status code indicates that the client's request was successfully received, understood, and accepted.

HTTP_200_OK
HTTP_201_CREATED
HTTP_202_ACCEPTED
HTTP_203_NON_AUTHORITATIVE_INFORMATION
HTTP_204_NO_CONTENT
HTTP_205_RESET_CONTENT
HTTP_206_PARTIAL_CONTENT
HTTP_207_MULTI_STATUS
Redirection - 3xx
This class of status code indicates that further action needs to be taken by the user agent in order to fulfill the request.

HTTP_300_MULTIPLE_CHOICES
HTTP_301_MOVED_PERMANENTLY
HTTP_302_FOUND
HTTP_303_SEE_OTHER
HTTP_304_NOT_MODIFIED
HTTP_305_USE_PROXY
HTTP_306_RESERVED
HTTP_307_TEMPORARY_REDIRECT

HTTP_400_BAD_REQUEST
HTTP_401_UNAUTHORIZED
HTTP_402_PAYMENT_REQUIRED
HTTP_403_FORBIDDEN
HTTP_404_NOT_FOUND
HTTP_405_METHOD_NOT_ALLOWED
HTTP_406_NOT_ACCEPTABLE
HTTP_407_PROXY_AUTHENTICATION_REQUIRED
HTTP_408_REQUEST_TIMEOUT
HTTP_409_CONFLICT
HTTP_410_GONE
HTTP_411_LENGTH_REQUIRED
HTTP_412_PRECONDITION_FAILED
HTTP_413_REQUEST_ENTITY_TOO_LARGE
HTTP_414_REQUEST_URI_TOO_LONG
HTTP_415_UNSUPPORTED_MEDIA_TYPE
HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE
HTTP_417_EXPECTATION_FAILED
HTTP_422_UNPROCESSABLE_ENTITY
HTTP_423_LOCKED
HTTP_424_FAILED_DEPENDENCY
HTTP_428_PRECONDITION_REQUIRED
HTTP_429_TOO_MANY_REQUESTS
HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE
HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS
Server Error - 5xx
Response status codes beginning with the digit "5" indicate cases in which the server is aware that it has erred or is incapable of performing the request. Except when responding to a HEAD request, the server SHOULD include an entity containing an explanation of the error situation, and whether it is a temporary or permanent condition.

HTTP_500_INTERNAL_SERVER_ERROR
HTTP_501_NOT_IMPLEMENTED
HTTP_502_BAD_GATEWAY
HTTP_503_SERVICE_UNAVAILABLE
HTTP_504_GATEWAY_TIMEOUT
HTTP_505_HTTP_VERSION_NOT_SUPPORTED
HTTP_507_INSUFFICIENT_STORAGE
HTTP_511_NETWORK_AUTHENTICATION_REQUIRED
Helper functions
The following helper functions are available for identifying the category of the response code.

is_informational()  # 1xx
is_success()        # 2xx
is_redirect()       # 3xx
is_client_error()   # 4xx
is_server_error()   # 5xx






import random

def roundone(result):

	dice = result
	if 1 in dice and 6 in dice:
		dice.remove(6)
	elif 6 in dice:
		dice.remove(6)
	elif 1 in dice:
		dice.remove(1)
	return dice

def roundtwo(result):
	dice = result
	return result

def roundthree(result):
	dice = result
	return result

def finish():
	return '1'



def roll(number):
	NO =[1, 2, 3, 4, 5, 6]
	res = []
	for i in range(0, number):
		res.append(random.choice(NO))
	dc1 = (random.choice(NO))
	dc2 = (random.choice(NO))
	dc3 = (random.choice(NO))
	dc4 = (random.choice(NO))
	res = [dc1, dc2, dc3, dc4]
	return res

print 'masukkan jumlh player : '

choice = input()

if choice >= 1:
	rolls1 = roll(choice)
	print rolls1
	print roundone(rolls1) 



	# two = input('Tekan angka 0 untuk play round 2 : ')

	# if two == 0:
	# 	rolls2 = map(str, roll())
	# 	r2 = ", ".join(rolls2)
	# 	print roundtwo(r2)
		
	# 	three = input('tekan angka 0 untuk play round 3 : ')

	# 	if three == 0:
	# 		rolls3 = map(str, roll())
	# 		r3 = ", ".join(rolls3)

	# 		print roundthree(r3)
			
	# 		finished = input('tekan angka 0 untuk melihat hasil : ')

	# 		if finished == 0:
	# 			print finish()

	# 		else:
	# 			print "dice was restart"
	# 	else:
	# 		print "dice was restart"

	# else:
	# 	print "dice was restart"

else:
	print "unknow command"
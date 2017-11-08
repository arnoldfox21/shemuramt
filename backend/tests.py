
			Task
- upload
- supllier
- mailer
- forgot password


						!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!



			note setting

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
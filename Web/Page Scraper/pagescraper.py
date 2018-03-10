#!/home/shalini/anaconda2/bin/python

# import modules, classes, functions
from bs4 import BeautifulSoup
import re
import requests
"""Understand abstraction well"""

# take url as input
url = raw_input('Enter the URL:')
out_folder = raw_input('Enter location where you want to save the images:')

# Two HTTP request methods - GET - request data from server & POST -
# submit data to be processed to server
req = requests.get(url)

# parse url
soup = BeautifulSoup(req.text, 'html.parser')

# get all image tags
img_tags = soup.find_all('img')

# get urls of all images, store in a list
urls = [img['src'] for img in img_tags]

# print urls
# print("\n".join(urls))

# create folder with name input_url

# download images
for image in urls:
    filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', image)
    # searches src with .jpg,png,gif ext
    """Regex -'\' allows special characters without invoking their special meaning
    re allows string matching with regular expression
    re.search - scan through string looking where regex produces match
    re.search(pattern, string,flags=0)
    \w - when locale & unicode flags not specifies, equivalent to set [a-zA-Z0-9_]
    [.](jpg|gif|png)$ - from end of the string matches .ext """
    try:
        with open(filename.group(1), 'wb') as f:
            """.group() returns the string matched by re
            e.g. >>> p = re.compile('(a(b)c)d')
                >>> m = p.match('abcd')
                >>> m.group(0) - o/p - 'abcd'
                >>> m.group(1) - o/p - 'abc'
                >>> m.group(2) - o/p - 'b'"""
            #if 'https' not in image:
             #   image = '{}{}'.format(url, image)
            response = requests.get(image)
            f.write(response.content)
    except(requests.exceptions.MissingSchema, AttributeError):
        pass

# Difference between print in 2.7 vs 3.0
# In 2.7, print is statement - parentheses is voluntary
# In 3.0, it's function - means pass items in std way or get syntax error

"""Advantages of Requests vs urllib"""


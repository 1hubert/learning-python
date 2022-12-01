import requests
from bs4 import BeautifulSoup

result = requests.get("https://www.google.com/")

# making sure that the website is accesible
# 200 OK responses == page is indeed present
# for other responses visit wiki on http status codes
# print(result.status_code)

# checking the HTTP header of the website
# print(result.headers)

# storing the page content of the
# website accesed from request to a variable
src = result.content

# with that much of data we need BS to parse and process
# the source. to do so, we create a BS object based
# on the source variable we created above:
soup = BeautifulSoup(src, features="html.parser")

# now that the page source has been processed via BS
# we can acces specific information directly from it.
# for instance, say we want  to see a list of all
# of the links on the page:
links = soup.find_all("a")

# perhaps we just want to extract the link that 
# has contains the text "About" on the page.
# we can use the built-in "text" function to
# acces the text content between the <a> <a/> tags
for link in links:
    if "Warunki" in link.text:
        print(link)
        print(link.attrs['href'])
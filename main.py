import webapp2
import cgi # i imported CGI to process user input submitted through an HTML"form", a CGI script is invoked by an HTTP server.
import string


form = """

<!DOCTYPE html>

<html>
  <head>
    <title> ROT 13 by Cathrine Johansen</title>
  </head>

  <body>
    <h2> Hello.. Please enter some text to ROT13:</h2>
    <form method="post">
      <textarea name="text"
                style="height: 120px; width: 420px;">%(text)s</textarea>  
      <br>
      <input type="submit"> 
    </form>
  </body>

</html>

    """

def escape_html(s):
    return cgi.escape(s, quote = True) # escape replaces all special characters that can cause trouble on the webpage.

def rot_13(s):
    abc = string.ascii_lowercase # abc is equal to a-z, and each letter in abc_13 
    abc_13 = abc[13:] + abc[:13] # has been replaced by the letter that is 13 places away.

    rot = '' 
    for c in s:
        if c in string.ascii_letters:
            rot += abc_13[abc.index(c.lower())] # if c is in a-z or A-Z, get its index in abc, 
        else:                                     #and replace it with the same in abc_13. Alle the letters are lowercase. 
		                                        
            rot += c

    for i in range(0, len(s)):
        if s[i] in string.ascii_uppercase:      # if letter in s at index i was uppercase, replace the similar letter in rot 
            rot = rot.replace(rot[i], rot[i].upper())  #with its uppercase version.

    return rot

class MainHandler(webapp2.RequestHandler): # the handler handles incoming requests and then start the webapp-
                                           #framework to handle the request and call the handler as needed.
    def write_form(self, text = ""):
        self.response.out.write(form % {"text" : escape_html(text)}) # creates an object to handle a request for every "text".
                                                                     
    def get(self):
        self.write_form()

    def post(self):
        user_input = self.request.get("text")
        coded_text = rot_13(user_input)

        if coded_text:
            self.write_form(coded_text)


app = webapp2.WSGIApplication([
    ('/', MainHandler)], debug=True)


#!/usr/bin/env python3

# Import modules for CGI handling 
import cgi, cgitb 

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
username = form.getvalue('username')
password  = form.getvalue('password')

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello - Second CGI Program</title>")
print("</head>")
print("<body>")
print("<h2>username %s </h2>" % (username))
print("<h2>password %s </h2>" % (username))
print("</body>")
print("</html>")
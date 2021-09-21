#!/usr/bin/env python3
import os, json, cgi
import cgi
import cgitb
import sys
cgitb.enable()
import templates
import secret
print("Content-type:text/html\r\n\r\n")
print('<html>')
print('<head>')
print('<title>Hello World - First CGI Program</title>')
print('</head>')
print('<body>')
print('<h2>Hello World! This is my first CGI program</h2>')

json_obj = json.dumps(dict(os.environ), sort_keys=True, indent=4)
print("ENVIRONMENT VAR ", json_obj)
print()
print("<p> QUERY_STRING: {}</p>".format(os.environ["QUERY_STRING"]))
print()
print("<p> HTTP_USER_AGENT: {}</p>".format(os.environ["HTTP_USER_AGENT"]))

print("""
    <h1> Welcome, enter your username and password </h1>

    <form method="POST" action="hello.py">
        <label> <span>Username:</span> <input autofocus type="text" name="username"></label> <br>
        <label> <span>Password:</span> <input type="password" name="password"></label>

        <button type="submit"> Login! </button>
    </form>
    """)

posted_bytes = os.environ.get("CONTENT_LENGTH", 0)
if posted_bytes:
    posted = sys.stdin.read(int(posted_bytes))
    print(f"<p> POSTED: <pre>")
    for line in posted.splitlines():
        print(line)
        login_info = line.split("&")
        username = login_info[0][login_info[0].find("=")+1:]
        password = login_info[1][login_info[1].find("=")+1:]
    print("</pre></p>")
print('</body>')
print('</html>')

if username == secret.username and password == secret.password:
    print("Set-Cookie:UserID = XYZ;\r\n")
    print("Set-Cookie:Password = XYZ123;\r\n")
    print("""
    <h1> Welcome, {username}! </h1>

    <p> <small> Pst! I know your password is
        <span class="spoilers"> {password}</span>.
        </small>
    </p>
    """.format(username=username,
               password=password))
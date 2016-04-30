#!/usr/bin/python

import cgitb, cgi
cgitb.enable()

print("Content-Type: text/html\n")


# We don't check that the fields weren't blank. That kind of data integrity
# assurance can get thrown out the window in a 24 hour hackathon.
def entryPoint():

    form = cgi.FieldStorage()
    print(form)


entryPoint()

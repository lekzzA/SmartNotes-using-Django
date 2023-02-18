------------------ Smart Notes ------------------

This Web App is created using the Django framework of Python. It utilizes HTML and CSS for content visualization and styling. 

Steps to run : 

1) Open the project in your choice of IDE.( I have used VS-Code)
2) Open the terminal, and run the command "python manage.py runserver". This will run the WebApp on the local server.
3) Follow the link to open the Home Page.
4) I) "/login" or the login button : To log into the system as an existing user.
  II) "/logout" or the logout button : To log out of the system.
 III) "/signup" or the signup button : To signup as a new user.


-- All the static files have been defined in the folder static, in the BASE_DIR. It consists of the "base.html" which is used as a template for all the HTML files in the project.
	-> To extend the template we simply use "{% extends "base.html"%}" at the start of an HTML file.
	-> Static file directory has to be defined in the "settings.py" file so that Django will look for the static files in that directory.
-- There are 3 apps, the Home, Notes and Smartnotes.
-- Django uses the database sqlite3 to store the data.

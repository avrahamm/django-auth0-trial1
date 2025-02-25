There are 2 Django apps in simple portfolio project. </br>
I created an Auth0 account and got a default app with credentials.</br>
Credentials are saved in .env file described in .env.example file.</br>
It is important that Auth0 settings urls are identical to local.</br>
If local server runs on http://127.0.0.1:3000 the same should appear in </br>
Auth0 settings, </b> 127.0.0.1 and not localhost</b>.

Step 1 </br>
I followed Auth0 Django tutorial
https://auth0.com/docs/quickstart/webapp/django/01-login
and it worked for me.</br>
Step 2 </br>
I want to protect "/projects" routes for the logged-in user, </br>
as appears in portfolio/urls.py </br>

portfolio app is responsible for authentication.</br>
urls.py, vies.py, index.html template are inspired by </br>
Auth0 tutorial
https://auth0.com/docs/quickstart/webapp/django/01-login

There is another projects app originally comes from RealPython </br>
https://realpython.com/courses/django-portfolio-project/
basic project codem with addition inspired by <br/>
https://www.w3schools.com/django/index.php tutorial.</br>
There is a simple projects list.

To run: </br>
git clone https://github.com/avrahamm/django-auth0-trial1.git </br>
cd https://github.com/avrahamm/django-auth0-trial1.git </br>
pip install -r requirements.txt
touch .env </br>
#fill with values </br>
python3 manage.py runserver 3000 </br>

Currently, I can't arrive to /projects route </br>
after Auth0 logged in.



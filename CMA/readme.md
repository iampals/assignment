Back End Setup:
   It is based on Python 3.X. 
   Need to install dependency from requirements.txt file
   PostgreSQL is used as DB

In API list, Browser:
http://localhost:8000/api/v1/pages/1/  - response is page content which will be driven

http://localhost:8000/api/v1/loginusertoken/  - responses token for username/password


Front End Setup:
  It is based on angularjs.
  Need node.js/npm for development/run environment setup

  http web server installation:

  In command prompt, run "npm install -g httpster"   - it will help to install the http server. Because front end code has to be deployed in http server

  open the root folder in command prompt, 
   run "httpster -p 3000"   - port no (3000) is important. I used this port no in django settings for CORS issue avoid

  
In Application launch in Browser:
  http://localhost:3000/
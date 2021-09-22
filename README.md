# fitapp-api
This is a simple RestAPI project in flask,it contain User Auth(which can be divided in two parts,clients or admins),CRUD operation on Recipes where an admin can Create Read Update and Delete recipes while clients can only list them.Also on user registration when you give details like wheight,height...it automaticaly calculate different fitness measurements like BMI ....!

#SETUP

1.git clone

2.cd project

3.pipenv install

4.On config file add your database URI and email details (if you want to use email sending)


#ENDPOINTS

User Auth
http://127.0.0.1:5000/user/login  body {"username":"test","password":"test"}

http://127.0.0.1:5000/user/register 
body {"username":"test","password":"password","name":"test","surname":"test","email":"test@hotmail.com","age":1,"isAdmin":true,"body_data":{"height":185,"weight":90}}

http://127.0.0.1:5000/user/logout


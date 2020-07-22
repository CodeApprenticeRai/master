Install python virtual enviornment using 'python3 -m pip install --user virtualenv'.
Create a new venv using 'python3 -m venv env'.
Enter the venv using 'source env/bin/activate'
Once the envriornment is instantiated,install Django using 'python -m pip install Django'.
Cd into master/master and use command 'python3 manage.py runserver'
For ease's sake, a user already exists with username 'test_user' and password 'working_at_the_car_wash'. Creating a user can also be done in the sign up page.
The remaining flow of use is simple. The creation of users, challenges, and questions are all labeled. So too is the taking of challenges. The encapsulation of objects is that challenges contain questions, and questions do not exist on their own outside the context of a challenge.

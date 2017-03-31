from flask import Flask
from flask import request
from ProfileValidator import ProfileValidator
from Database import Database
import pymysql

# 1. get only 1 version of pypthon,I guess the 32 bit version is the one I should use
# 2. create db queries to make sure that the  id username and email are unique
# 3. route get profile/:id needs to return the profile with that id
# 3. if there is no profile with that id return the healpful error saying that
# 4. create a route ('/project') a POST request that takes a project name and user ID. Check to make sure the user ID exists and then 'save' the project name to the user



app = Flask(__name__)



@app.route('/', methods=['GET'])
def hello_world():

    return 'sucess'

@app.route('/new-profile', methods=['POST'])
def new_profile():
    # retrieve  post data from form
    uname = request.form['username']
    email = request.form['email']
    pwd   = request.form['password']
    c_pwd = request.form['confirm password']
    zip   = request.form['zipcode']

    # create a dict of the data then dump it to json
    dict = {'username': uname, 'email': email, 'password': pwd, 'confirm password': c_pwd, 'zip': zip}

    validator = ProfileValidator()
    response = validator.is_valid(dict)



    return response




@app.route('/profile/:<id>', methods=['GET'])
def get_profile(id):
    # init Database
    database = Database()
    profile = database.get_profile(id)
    return profile



def validateProfile():
    return

if __name__ == '__main__':
    app.run()


import pymysql
from pprint import  pprint
from flask import json


class Database:

    def __init__(self):
        self.conn = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='',
            db='challenge')

        self.cur = self.conn.cursor()

    def data_is_unique(self, data):
        # run functions and assign variables

        # directly below can be used to simulate id validation
        # id_is_unique = self.is_id_unique(data)
        username_is_unique = self.is_username_unique(data)
        email_is_unique = self.is_email_unique(data)
        response = []

        # check to make to see if variable is unique if not return error
        # if id_is_unique != True:
        #     response.update({'id error': id_is_unique})

        if username_is_unique is not True:
            response.append(username_is_unique)

        if email_is_unique is not True:
            response.append(email_is_unique)

        if len(response) < 1:
            code = {'code': 200}
            success = {'success': [data, code]}
            response.append(success)
        else:
            # wrap the response in an error
            response = {'errors': response}

        # close Database
        self.close()

        return json.jsonify(response)








    def is_username_unique(self, data):
        # execute sql statement
        self.cur.execute("SELECT * from challenge WHERE username = %s", data['username'])
        row = self.cur.fetchone()
        # check if username exists in database
        if row is not None:
            error = {'status': 409, 'message': 'username must be unique'}
            return error
        # if username is unique return true
        return True

    def is_email_unique(self, data):
        self.cur.execute("SELECT * from challenge WHERE email = %s", data['email'])
        row = self.cur.fetchone()
        if row is not None:
            error = {'status': 409, 'message': 'email must be unique'}
            return error
        return True

    def is_id_unique(self, data):
        self.cur.execute("SELECT * from challenge WHERE id = %s", data['id'])
        row = self.cur.fetchone()
        if row is not None:
            error = {'status': 409, 'message': 'id is not unique'}
            return error
        return True

    # returns profile given an id
    def get_profile(self, id):
        self.cur.execute("SELECT * from challenge WHERE id = %s", id)
        row = self.cur.fetchone()

        if row is not None:

            # create profile
            profile = {'id': row[0], 'username': row[1], 'email': row[2],
                                    'password': row[3], 'zipcode': row[4]}
            # build response
            response = {'profile': profile, 'status': 200}
            type = 'success'
        else:
            response = {'message': 'no profile exists with id: '+id, 'status': 404}
            type = 'error'

        return json.jsonify({type: response})

    def close(self):
        self.cur.close()
        self.conn.close()


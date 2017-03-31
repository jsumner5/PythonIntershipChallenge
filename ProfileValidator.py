from flask import json
from Database import Database
class ProfileValidator():

    def __init__(self):
        return

    def is_valid(self, data):

        if data['confirm password'] != data['password']:
            error = {'message': 'passwords do not match'}
            return json.dumps(error)
        if len(data['password']) < 6:
            error = {'message': 'password must be at least 6 characters'}
            return json.dumps(error)
        if len(data['zip']) != 5:
            error = {'message': 'zipcode is not a valid 5 digit zip'}
            return json.dumps(error)


        return self.is_unique(data)

    def is_unique(self, data):
        d = Database()
        response = d.data_is_unique(data)

        return response



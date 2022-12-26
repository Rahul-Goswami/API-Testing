from flask import Flask
from flask_restful import Resource, Api, reqparse
from Employee_Data import Employees

app = Flask(__name__)
api = Api(app)

class Employee(Resource): #Pass Resource as argument to class to notify that this class is to be used as an entry point for API
    def get(self):
        emp = Employees()
        return emp.get_employee_details()

api.add_resource(Employee, '/employee') #employee is one entry point for the API

if __name__ == '__main__':
    app.run() # This runs the Flask API on this machine/server

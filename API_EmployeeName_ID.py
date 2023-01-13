"""I am using Flask Web App Framework to manage the API processing, Waitress as the WSGI (Web Server
Gateway Interface) server to receive HTTP response and serve to the Python App, and NGINX Web Server
as a Reverse Proxy to receive HTTP Request from external requestor and send it to WSGI server

NOTE: Use the following command in terminal to instantiate the Waitress WSGI server:
waitress-serve --host=127.0.0.1 --port=8080 API_EmployeeName_ID:app"""

from flask import Flask
from flask_restful import Resource, Api, reqparse
from Employee_Data import Employees
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
api = Api(app)
app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)
class Employee(Resource): #Pass Resource as argument to class to notify that this class is to be used as an entry point for API
    def get(self):
        emp = Employees()
        return emp.get_employee_details()

api.add_resource(Employee, '/employee') #employee is one entry point for the API

#if __name__ == '__main__':
    #app.run() # This runs the Flask API on this machine/server
    #serve(app) # This runs Waitress WSGI server and maps to the Flask App



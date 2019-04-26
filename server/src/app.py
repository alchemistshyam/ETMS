from flask import Flask, jsonify, request, json , Response
import wmi, os
import win32com
import pythoncom
import sys
import datetime
sys.path.append(os.path.abspath('..\\'))
from   utilities.ProcessList import ProcessList
import jwt

class Application:

    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'shyam'
    processes = []
    processObject = ProcessList()

    @classmethod
    def addProcessList(cls,requestData):
        
        if ( cls.processObject.validate_ProcessList(json.dumps(requestData.get_json()))) :
            cls.processes.insert(0, requestData.get_json())
            response = Response("", status=200, mimetype= 'application/json')
            response.headers['Location'] = "Process Added Succssfully"
            return response
        else:
            invalidErrorMsg = {
                "errorMsg " : "Invalid process passed"            }
            response = Response(json.dumps(invalidErrorMsg), status=400 , mimetype='application/json')
            return response

    @classmethod
    def listProcess(cls):
        return cls.processes

    def createtoken(self):
        expiration_date = datetime.datetime.utcnow() + datetime.timedelta(seconds= 100)
        token = jwt.encode({}, self.app.config['SECRET_KEY'], algorithm= 'HS256')
        return token

    def decode_token(self,token) :
        try :
            jwt.decode(token, self.app.config['SECRET_KEY'])
            return True
        except:
            return False

    @app.route('/gettoken')
    def get_token():
        token = Application().createtoken();
        return token

    # GET to list all the process
    @app.route('/processes')
    def list_processes():
        response = jsonify(Application().listProcess())
        return response

    @app.route('/scan/<string:scanType>')
    def scanData(scanType):
        token = request.args.get('token')
        print(token)
        if Application().decode_token(token):
            if scanType == 'process':
                return jsonify(ProcessList.get_ProcessList())
        else:
            return jsonify({'error' , 'Need a valid token to view this page'}) , 401
            
    # Post to insert processes - One by one
    @app.route('/processes' , methods= ['POST'])
    def add_processList():
        response = Application().addProcessList(request)
        return response
    

    def start_server(self):
        self.app.run(port=5000 , debug=True)

if __name__ == "__main__":
    serverStart = Application()
    serverStart.start_server()    

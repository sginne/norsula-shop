from app import app
from waitress import serve
from app.configuration import Configuration

#Switch between waitress and development flask
try:
    if Configuration.debugging==True:
        app.run(host='127.0.0.1',port=Configuration.port)
    else:
        serve(app,host='127.0.0.1', port=Configuration.port)
except AttributeError:
    serve(app, host='127.0.0.1', port=5000)
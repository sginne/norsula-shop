from app import app
from waitress import serve

#Switch between waitress and development flask
#app.run()
serve(app,host='127.0.0.1', port=5003)
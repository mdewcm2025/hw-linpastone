from cmsimde import flaskapp
from gevent.pywsgi import WSGIServer

#flaskapp.app.run(host="0.0.0.0", debug=True)
#http_server = WSGIServer(('0.0.0.0', 8080), flaskapp.app)
http_server = WSGIServer(('::', 8080), flaskapp.app, family=socket.AF_INET6)
http_server.serve_forever()
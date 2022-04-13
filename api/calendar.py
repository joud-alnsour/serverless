from http.server import BaseHTTPRequestHandler
from datetime import datetime
from urllib import parse
import platform
import calendar

class handler(BaseHTTPRequestHandler):

  def do_GET(self):    
    
    path= self.path
    url_components = parse.urlparse(path)
    query_string = parse.parse_qsl(url_components.query)
    dic=dict(query_string)
    name= dic.get('name')
    if name:
      message = f'Hello, {name}!\n'
    else:
      message = 'Hello, Stranger!\n' 

    message += f"\n Greetings from Python Version {platform.python_version()} at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    message1 = '\nThis is the datetime Year/Month/Day/Number of Week/Hour/Minute/Second: ' +'\n'
    message2 = '\nThis is the Calendar for year 2022: ' +'\n\n'

    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(message.encode())
    self.wfile.write(message1.encode())
    self.wfile.write(str(datetime.now().strftime('%Y-%m-%d/%W/ %H:%M:%S \n')).encode())
    self.wfile.write(message2.encode())
    self.wfile.write(calendar.calendar(2022, 2, 1, 6).encode())

    return
import http.server  
import socketserver  
import cgi  
  
PORT = 8000  
  
class CustomHandler(http.server.SimpleHTTPRequestHandler):  
   def do_GET(self):  
      self.send_response(200)  
      self.send_header("Content-type", "text/html")  
      self.end_headers()  
      html = """  
        <html>  
        <head>  
           <title>User Information</title>  
        </head>  
        <body>  
           <h1>User Information</h1>  
           <form action="" method="post">  
              <label for="name">Name:</label><br>  
              <input type="text" id="name" name="name"><br>  
              <label for="age">Age:</label><br>  
              <input type="number" id="age" name="age"><br>  
              <label for="dob">Date of Birth:</label><br>  
              <input type="date" id="dob" name="dob"><br>  
              <label for="school">School:</label><br>  
              <input type="text" id="school" name="school"><br>  
              <label for="gender">Gender:</label><br>  
              <input type="radio" id="male" name="gender" value="male"> Male<br>  
              <input type="radio" id="female" name="gender" value="female"> Female<br>  
              <input type="submit" value="Submit">  
           </form>  
           <div id="output"></div>  
        </body>  
        </html>  
      """  
      self.wfile.write(html.encode())  
  
   def do_POST(self):  
      form = cgi.FieldStorage(  
        fp=self.rfile,  
        headers=self.headers,  
        environ={'REQUEST_METHOD': 'POST'}  
      )  
      name = form.getvalue("name")  
      age = form.getvalue("age")  
      dob = form.getvalue("dob")  
      school = form.getvalue("school")  
      gender = form.getvalue("gender")  
      output = f"""  
        <p>Name: {name}</p>  
        <p>Age: {age}</p>  
        <p>Date of Birth: {dob}</p>  
        <p>School: {school}</p>  
        <p>Gender: {gender}</p>  
      """  
      self.send_response(200)  
      self.send_header("Content-type", "text/html")  
      self.end_headers()  
      html = """  
        <html>  
        <head>  
           <title>User Information</title>  
        </head>  
        <body>  
           <h1>User Information</h1>  
           <form action="" method="post">  
              <label for="name">Name:</label><br>  
              <input type="text" id="name" name="name"><br>  
              <label for="age">Age:</label><br>  
              <input type="number" id="age" name="age"><br>  
              <label for="dob">Date of Birth:</label><br>  
              <input type="date" id="dob" name="dob"><br>  
              <label for="school">School:</label><br>  
              <input type="text" id="school" name="school"><br>  
              <label for="gender">Gender:</label><br>  
              <input type="radio" id="male" name="gender" value="male"> Male<br>  
              <input type="radio" id="female" name="gender" value="female"> Female<br>  
              <input type="submit" value="Submit">  
           </form>  
           <div id="output">{output}</div>  
        </body>  
        </html>  
      """  
      self.wfile.write(html.encode())  
  
with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:  
   print("Serving at port", PORT)  
   httpd.serve_forever()

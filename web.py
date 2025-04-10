from http.server import HTTPServer, BaseHTTPRequestHandler
content="""<!doctype html>
<html>
<head>
<title> My Web Server</title>
<style>
    table,tr,td,th
    {
    
    border:1px solid black;
    border-collapse:collapse;
    padding:10px;
    text-align:center;
    }
    </style>
</head>
<body>
<center><h1 style="font-family: cursive;"><u>TCP/IP PROTOCOLS</u></h1><br>
<table>
<tr>
<th>S.NO</th>
<th>LAYER</th>
<th>PROTOCOLS</th>
</tr>
    
<tr>
<td>1.</td>
<td>Application layer protocol</td>
<td>HTTPS,FTP,DNS</td>
</tr>
    
<tr>
<td>2.</td>
<td>Transport layer protocol</td>
<td>TCP</td>
    
</tr>
    
<tr>
<td>3.</td>
<td>Internet layer protocol</td>
<td>IP</td>
</tr>
    
<tr>
<td>4.</td>
<td>Link layer protocol</td>
<td>MAC</td>
</tr>
</table>
</center>
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()
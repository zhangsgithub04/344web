import socket

"""
Student: 
Based on Sample Starter Code drafted by S. Zhang 2018
Partial & Simplified Solution for a Web Server using plain TCP socket
Still needs a lot of work to expand it to a full fledged web server. 
"""

class OneontaWebServer:
    webhostpath='c:\\courses\\csci344\\'  
    
    # Handle a GET request.
    def handle_request(self, connection, request):
        requestfilename='mytest1.html'
        #requestfilename='favicon.ico'
        #!!! You need to parse the request to extract the name of the requested file.
		
        parts= request.split()
        requestfilename=parts[1]   
        #print requestfilename
        #Do it yourself first ... before getting my hints
        # also need to know file system    
        fullfilename=OneontaWebServer.webhostpath+requestfilename
        print "file name of requested: "+fullfilename
        f = open(fullfilename) #opens file and reads the contents
        data =f.read()
        self.server_respond(connection, data)
	
    # Respond a file
    def server_respond(self, connection, content):
        #print content
        connection.send('HTTP/1.1 200 OK\n')
        connection.send('Content-Type: text/html\n')
        connection.send('Content-Length: '+str(len(content))+'\n')
        connection.send('\n')
	
        # header and body should be separated by additional newline
        connection.send(content) # Use triple-quote string.
    
    def start_server(self):
        HOST=''
        PORT = 8080 
        listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listen_socket.bind((HOST, PORT))
        listen_socket.listen(1)

        print 'Serving HTTP on port %s ...' % PORT

        while True:
		
            try:
                client_connection, client_address = listen_socket.accept()
                request = client_connection.recv(1024)
                print "In From Client: "+request
                self.handle_request(client_connection, request)
            except IOError:
                # error message
                client_connection.send('\n404 File Not Found\n') #sends an error message to be printed on the page
				
        client_connection.close()
	
# the entry point	
mywebserver = OneontaWebServer()	
mywebserver.start_server()	

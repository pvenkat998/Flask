import socket


def show_hostname():

   hostname = socket.gethostname()

   print("Name:"+hostname)

if __name__ == "__main__":

     show_hostname()
import socket

def show_computer_ip():
    hostname = socket.gethostname()

    hostname ="user-pc"

    try:

         ip = socket.gethostbyname(hostname)

         print ("IP Address:"+ip)

    except socket.error as err:

         print (hostname+":"+err)

    if __name__ == "__main__":

         show_computer_ip()


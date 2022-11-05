###########################################################################################
#   Les Imports
###########################################################################################
import os
import socket
import time
import pickle
from threading import main_thread

from _thread import *
from kivy.app import App
from kivy.clock import Clock
from kivy.properties import StringProperty, BooleanProperty
from kivymd.app import MDApp
import random
import kivy.core.text.markup
from kivy.core.text.markup import MarkupLabel
from kivy.uix.label import Label

class ChatApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
       
    nick_name = ""
    host_ip = ""
    host_port = ""
    message = StringProperty("")
    label_messages = StringProperty("")
    ClientMultiSocket = socket.socket()
    #test = StringProperty("[color=ff0000]Host Ip [/color]")

    # The following function handles the reception of messages from the server
    # and displays them on the client screen
    def display_response_client_thread(self, connection_socket):
        while True:
            data = connection_socket.recv(2048)                                          # wait until data are received
            if not data:
                break
            self.label_messages += "\n"+ data.decode('utf-8')
        connection_socket.close()
        

    def on_nickname_validate(self, widget):
        self.nick_name = widget.text
        print(self.nick_name)

    def on_hostip_validate(self, widget):
        self.host_ip = widget.text
        print(self.host_ip)

    def on_hostport_validate(self, widget):
        self.host_port = widget.text
        print(self.host_port)

    def disconnect_pressed(self):
        print("Disconnecting..........")
        self.ClientMultiSocket.close()
        self.label_messages += "[color=#00ff00]\n[b]INFO[/b]: You succesfully disconnected[/color]"
    def connect_pressed(self):
        print('Connecting ...')
        try:
            self.ClientMultiSocket.close()
            self.ClientMultiSocket = socket.socket()                                                 # Create client connection socket with the server
            self.ClientMultiSocket.connect((self.host_ip, int(self.host_port)))
        except ValueError:
            self.label_messages += "[color=#ff0000]\n[b]PROBLEM[/b]: Provide Nickname, Server IP and port[/color]"
        except socket.error as e:
            print(str(e))
            self.label_messages += "[color=#ff0000]\n[b]PROBLEM[/b]: Server offline ...[/color]"
        else:
            print("Connected")
            self.ClientMultiSocket = self.ClientMultiSocket
            # Display Welcome message
            res = self.ClientMultiSocket.recv(1024)
            self.label_messages += "\n " + res.decode('utf-8')
            # Create a listening thread that will listen for data from the server
            # for all the other messages coming from the server
            start_new_thread(self.display_response_client_thread, (self.ClientMultiSocket, ))
    
    def send_message(self, text):
        self.message = text
        try:
            dict = {"id": self.nick_name, "msg": self.message}
            self.ClientMultiSocket.sendall(pickle.dumps(dict))
            #self.ClientMultiSocket.sendall(str.encode(self.nick_name + ": " + self.message))
        #except OSError:
        #    self.label_messages += '\n You must connect to the server'
        except socket.error as e:
            if (e.errno == 57) or (e.errno == 9):
                self.label_messages += "[color=#ff0000]\n[b]PROBLEM[/b]: You must connect with the server[/color]"
            if e.errno == 61:
                self.label_messages += "[color=#ff0000]\n[b]PROBLEM[/b]: Server offline[/color]"
            print(str(e))
        self.message = ""
        


ChatApp().run()

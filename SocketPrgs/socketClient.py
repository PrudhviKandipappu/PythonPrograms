#

import socket
import threading
import PySimpleGUI as psg 
ClientSocket = socket.socket()
host = '165.22.14.77'
port = 8000

ClientSocket. connect((host, port))

names = []
ListBox1 = psg.Listbox(names, size = (20, 4), font=('Bold', 14), expand_y = True, enable_events = True, key ='_LIST_')
layout = [[ListBox1],[psg.Input(size=(20, 1), font = ('Bold', 14), expand_y=True, key = '_INPUT_'),
psg.Button('Send')]]

def ReceiveMessage():
    msg = ClientSocket.recv(1024).decode()
    names.append(msg)
    window['_LIST_'].update(names)
    
window = psg.Window('Listbox with names', layout, size=(400, 150))
while True:
   threading._start_new_thread(ReceiveMessage, ())
   event, values = window.read()
   if event in (psg.WIN_CLOSED, 'Exit'):
      break
   if event == 'Send':
        names.append(values['_INPUT_'])
        ClientSocket. sendall(str(values['_INPUT_']).encode())
        window['_LIST_'].update(names)
window.close()

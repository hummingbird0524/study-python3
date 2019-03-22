'''
Created on 2018/02/01

@author: y_nishikawa
'''

# -*- coding:utf-8 -*-

import socket

#--------------------------------------------------
IP   = "127.0.0.1"  # IPアドレス
PORT = 50000        # 待ち受けポート
#--------------------------------------------------

def run():
    print("--------------------------------------------------")
    print("- [Python3] TCP Socket Server")
    print("--------------------------------------------------")
    
    # サーバーSocket生成
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # バインド
    server.bind( (IP, PORT) )
    
    # 接続待ち受け(引数はキューの最大数)
    server.listen(10)
    
    print("### Waiting for connections...")
    
    # 接続待ち受け
    (con, addr) = server.accept()
    
    print("### Connectet by", addr)
    
    while True:
        rcvMsg = con.recv(1024).decode()
        
        if rcvMsg == "":
            break
        
        print("recv: ", rcvMsg)
        
        con.sendall(b"receive success")
    
    con.close()
    
    server.close()
'''
Created on 2018/02/01

@author: y_nishikawa
'''
# -*- coding:utf-8 -*-

import socket

#--------------------------------------------------
IP   = "127.0.0.1"  # 通信先IPアドレス
PORT = 50000        # 通信先ポート
#--------------------------------------------------

def run():
    print("--------------------------------------------------")
    print("- [Python3] TCP Socket Client")
    print("--------------------------------------------------")
    
    # Socket通信用オブジェクト生成
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 接続
    client.connect( (IP, PORT) )
    
    while True:
        # 送信メッセージ入力
        sendMsg = input("### Please input send message: ")
        
        if sendMsg == "QUIT":
            break
        
        # 送信
        client.send(sendMsg.encode(encoding='utf_8', errors='strict'))
        
        # 応答受信
        response = client.recv(1024).decode()
        
        print("recv: ", response)
    
    client.close()
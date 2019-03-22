'''
****************************************************************************************************
Python 3 サンプルプログラム Main
Created on 2018/02/02
@author: y_nishikawa
****************************************************************************************************
'''
# -*- coding:utf-8 -*-
from TcpSocket import TcpServer, TcpClient
import os
import threading

def main():
    while True:
        
        print("--------------------------------------------------")
        print("◆Network Program")
        print("  1. TCP Socket Server")
        print("  2. TCP Socket Client")
        #print("  3. UDP Socket Server")
        #print("  4. UDP Socket Client")
        print("--------------------------------------------------")
        print("q. end")
        print("--------------------------------------------------")
        print("")
        
        programNo = input("### Please input program number: ")
        
        os.system("cls")
        
        if programNo == "1":
            #TcpServer.run()
            th_server = threading.Thread(target=TcpServer.run())
            th_server.start()
            
        elif programNo == "2":
            #TcpClient.run()
            th_client = threading.Thread(target=TcpClient.run())
            th_client.start()
            
        elif programNo == "q":
            print("# Program is over!!")
            print("# Please press any key...")
            break
        
        os.system("cls")
    
    return

if __name__ == '__main__':
    main()
from oscpy.client import OSCClient
import socket
import chess
from tabulaRasalib import *

board=chess.Board()



ip='127.0.0.1'
porta=3000



cols=list('ABCDEFGH') #lista de colunas

osc = OSCClient(ip, porta)

########### so as linhas
#for i in range(8):
#    osc.send_message(str.encode(('/L'+str(i+1))), str.encode(b[i]))

movimento=""

while (movimento != "fim"):
	movimento=input("move: ")
	board.push(chess.Move.from_uci(movimento))
	b=board.fen()
	b=expandefen(b)
	b=b[0:71]
	b=b.split('/')
	b.reverse()
	print (b)
	print (board)
	
	for i in range(8):
			cNUM=0
			for c in cols:
				linha=list(b[i])
				celula=str.encode(linha[cNUM])
				OSCpath=str.encode(('/L'+str(i+1)+'/'+c))
				osc.send_message(OSCpath, celula)
				cNUM=cNUM+1








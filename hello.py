a=("a","b","c","d","e","f","g","h","i","j","k","l",'m','n','o','p','q','r','s','t','u','v','w','x','y','z')
b=[]
final=[1,2,3,4,5,6,7,8,9,0]
for i in a:
	if((i=='h') or (i=='e') or (i=='l') or (i=='o') or (i=='w') or (i=='r') or (i=='d')):b.append(i)
for i in b:
	if(i=='h'):final[0]=i
	elif(i=='e'):final[1]=i
	elif(i=='l'):final[2]=final[3]=final[8]=i
	elif(i=='o'):final[4]=final[6]=i
	elif(i=='w'):final[5]=i
	elif(i=='r'):final[7]=i
	elif(i=='d'):final[9]=i
	else:break
def hello(z):
	out=""
	while(z<10):
		out=out+final[z]
		z -=-1
		if(z==10):
			print(out)
			break
hello(0)

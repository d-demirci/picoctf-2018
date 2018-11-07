>>> gr="You have now entered the Duck Web, and you're in for a honkin' good time"
... res=''
... for i in range(len(gr)):
...     res += chr(((i + 134514776) ^ ord(gr[i]) )%255 )
... print res
... f=open('./sekrutbuffer','r')
... buf=f.readlines()
... vals=[]
... for line in buf:
...     a=line.split('        ')[2].split('db')[1].replace('h','').replace('\n','')
...     vals.append(int('0x'+a.replace(' ',''),16) )
... print vals
... res=''
... for i in range(len(vals)):
...     res += chr( vals[i] ^ ord(gr[i])  )
... print res
����м�ԣ��ؔ������୚��ɛ��鵦���򚄉:�v:�~=�z�A�C|�����GK����P}���
[41, 6, 22, 79, 43, 53, 48, 30, 81, 27, 91, 20, 75, 8, 93, 43, 82, 23, 1, 87, 22, 17, 92, 7, 93, 0]
picoCTF{qu4ckm3_7ed36e4b}D


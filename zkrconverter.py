#!/usr/bin/python
#coding: utf8
def main():
 ff1='./13'
 ff2='./14'
 format1file=file(ff1)
 format2file=file(ff2)
 #ffl1=format1file.readlines()
 #№ffl2=format2file.readlines()
 format1=[]
 for ff in format1file:
  ff=ff.replace('\n','')
  f=ff.split('|')
  format1.append(f)
 format2=[]
 for ff in format2file:
  ff=ff.replace('\n','')
  f=ff.split('|')
  format2.append(f)
 print len(format2[3])
 zkr1f='./130701А1626903.ZR1'
 zkr1file=file(zkr1f,'r')
 zkr1lines=zkr1file.readlines()
 zkr1=[]
 for ff in zkr1lines:
  ff=ff.replace('\n','')
  f=ff.split('|')
  zkr1.append(f)
  zkr1dict={}
 for j in range(len(format1)):
  lines=format1[j]
  for i in range(1,len(lines)):
   zkr1dict[format1[j][i]]=zkr1[j][i]
 #print    zkr1dict[ 'DATE_ZR']
 #print format1[3]#, format1[2][3], format1[2][3]=='ZR(*)'
 #print zkr1[0][1]
 zkr2=[]
 f=[]
 fw=file('./14.zkr1','w')
 zkr1dict['NUM_VER']='TXZR140101'
 for j in range(len(format2)):
  lines=format2[j]
  ff=[]
  #print len(format2[3]),
  #ormat2[3][57]
  ff.append(format2[j][0])
  s=format2[j][0]
  for i in range(1,len(lines)):
   if format2[j][i] in zkr1dict.keys():
    ff.append(zkr1dict[format2[j][i]])
    s=s+'|'+zkr1dict[format2[j][i]]
   else:
    ff.append('')
    s=s+'|'
  f.append(ff)
  fw.write(s+'\n')
  print s
 fw.close()
   
if __name__ == "__main__":
    main()

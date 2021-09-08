a=int(input("USS Arizona outer width: \n"))
b=int(input("USS Arizona inner width: \n"))
c=int(input("USS Arizona tower height: \n"))

d = int(((a+b)/7))

for i in range(d):
    print('       '+a*' '+'              |'+b*'  '+'|')
    
print('       '+a*' '+'           |##$'+b*'  '+'$##|')

for j in range(c):
    print('       '+a*' '+'            ## '+b*'  '+' ##')

print('        '+a*' '+'           #..#'+b*'  '+'#..#')
print('        '+a*' '+'    \----. #..#'+b*'..'+'#..# .----/')
print(''+a*' '+'      \ ***|_|    |#..#'+b*'-#'+'#..#|    |_|*** /')
print('.__'+a*'_'+'____|___           _'+b*'..'+'_       _______|_'+a*'_'+'..')
print('`---. '+a*' '+'                 '+b*'  '+'                 '+a*' '+'--\\.')
print(' <<#\_'+a*'_'+'_________________'+b*'__'+'________________'+a*'_'+'_____\\')







      
### 
### Author:wenjunhuang
### Class: CSc 110
### Description: Describe your program with one
###              or more sentences of text.
###

      

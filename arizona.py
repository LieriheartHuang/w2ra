a=int(input("USS Arizona outer width: \n"))
b=int(input("USS Arizona inner width: \n"))
c=int(input("USS Arizona tower height: \n"))

d = int(round(((a+2*b)/7),0))

print('      '+a*' '+'                    |'+b*'  '+'|')
print('      '+a*' '+'                 |##$'+b*'  '+'$##|')
for i in range(d):
    print('      '+a*' '+'                  ## '+b*'  '+' ##')

print('      '+a*' '+'                 #..#'+b*'  '+'#..#')
print('      '+a*' '+'          \----. #..#'+b*'..'+'#..# .----/')
print('      '+a*' '+'    \ ***|_|    |#..#'+b*'-#'+'#..#|    |_|*** /')
print('._____'+a*'_'+'_____|____          _'+b*'..'+'._          ____|_'+a*'_'+'..')
print('`---. '+a*' '+'                     '+b*'  '+'                     '+a*' '+'--\\.')
print(' <<#\_'+a*'_'+'_____________________'+b*'__'+'____________________'+a*'_'+'_____\\')







      
### 
### Author:wenjunhuang
### Class: CSc 110
### Description: Describe your program with one
###              or more sentences of text.
###

      

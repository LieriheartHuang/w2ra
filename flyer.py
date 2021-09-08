a=int(input("Wright flyer size: \n"))
b=int( a/5 )+1
c=int(a*1.2)
print('   '+c*'     '+'      #')
print('   '+c*'     '+'#---------#')
print('   '+c*'     '+'#---------#')
print('==='+c*'====='+'=========='+c*'====='+'====')
for i in range(b):
    print(' H'+c*'    |'+'  |  %H%  |  '+c*'|    '+'H')
          
print(' H'+c*'    |'+'**|**%H%**|**'+c*'|    '+'H')
      
for j in range(b):
    print(' H'+c*'    |'+'  |  %H%  |  '+c*'|    '+'H')
      
      
print('====='+c*'====='+'==%H%=='+c*'====='+'=====')
print('   '+c*'     '+'|         |')
print('   '+c*'     '+'+#########+')

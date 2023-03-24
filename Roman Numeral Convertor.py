thousand = int(input())
hundred = int(input())
ten = int(input())
one = int(input())

numeral1 = str(input())
numeral2 = str(input())
numeral3 = str(input())
numeral4 = str(input())

print('Numbers to Numerals:')

if thousand == 3 :
  print('MMM')
elif thousand == 2 :
  print('MM')
elif thousand == 1 :
  print('M')
else :
  print(0)

if hundred == 9 :
  print('CM')
elif hundred == 8 :
  print('DCCC')
elif hundred == 7 :
  print('DCC')
elif hundred == 6 :
  print('DC')
elif hundred == 5 :
  print('D')
elif hundred == 4 :
  print('CD')
elif hundred == 3 :
  print('CCC')
elif hundred == 2 :
  print('CC')
elif hundred == 1 :
  print('C')
else :
  print(0)

  
if ten == 9 :
  print('XC')
elif ten == 8 :
  print('LXXX')
elif ten == 7 :
  print('LXX')
elif ten == 6 :
  print('LX')
elif ten == 5 :
  print('L')
elif ten == 4 :
  print('XL')
elif ten == 3 :
  print('XXX')
elif ten == 2 :
  print('XX')
elif ten == 1 :
  print('X')
else :
  print(0)

if one == 9 :
  print('IX')
elif one == 8 :
  print('VIII')
elif one == 7 :
  print('VII')
elif one == 6 :
  print('VI')
elif one == 5 :
  print('V')
elif one == 4 :
  print('IV')
elif one == 3 :
  print('III')
elif one == 2 :
  print('II')
elif one == 1 :
  print('I')
else :
  print(0)
  
print('Numerals to Numbers:')
  
if numeral1 == 'MMM' :
  print(int(3))
elif numeral1 == 'MM' :
  print(int(2))
elif numeral1 == 'M' :
  print(int(1))
else :
  print(0)
  
if numeral2 == 'CM' :
  print(int(9))
elif numeral2 == 'DCCC' :
  print(int(8))
elif numeral2 == 'DCC' :
  print(int(7))
elif numeral2 == 'DC' :
  print(int(6))
elif numeral2 == 'D' :
  print(int(5))
elif numeral2 == 'CD' :
  print(int(4))
elif numeral2 == 'CCC' :
  print(int(3))
elif numeral2 == 'CC' :
  print(int(2))
elif numeral2 == 'C' :
  print(int(1))
else :
  print(0)

if numeral3 == 'XC' :
  print(int(9))
elif numeral3 == 'LXXX' :
  print(int(8))
elif numeral3 == 'LXX' :
  print(int(7))
elif numeral3 == 'LX' :
  print(int(6))
elif numeral3 == 'L' :
  print(int(5))
elif numeral3 == 'XL' :
  print(int(4))
elif numeral3 == 'XXX' :
  print(int(3))
elif numeral3 == 'XX' :
  print(int(2))
elif numeral3 == 'X' :
  print(int(1))
else :
  print(0)

if numeral4 == 'IX' :
  print(int(9))
elif numeral4 == 'VIII' :
  print(int(8))
elif numeral4 == 'VII' :
  print(int(7))
elif numeral4 == 'VI' :
  print(int(6))
elif numeral4 == 'V' :
  print(int(5))
elif numeral4 == 'IV' :
  print(int(4))
elif numeral4 == 'III' :
  print(int(3))
elif numeral4 == 'II' :
  print(int(2))
elif numeral4 == 'I' :
  print(int(1))
else :
  print(0)
# a = input ('Enter your text : ')
# b = len(a)
# for i in range (b):
#    if a[i]== '0' or a[i]=='1' or a[i]=='2' or a[i]=='3' or a[i]=='4' or a[i]=='5' or a[i]=='6' or a[i]=='7' or a[i]=='8' or a[i]=='9':
#        print ('ERROR : <Text have number in it>')
#    else :
#     print ('Text is with out number.')
a = input ('Enter your text : ')
b = len(a)
ver = 0
for i in range (b):
    if a[i]== '0' or a[i]=='1' or a[i]=='2' or a[i]=='3' or a[i]=='4' or a[i]=='5' or a[i]=='6' or a[i]=='7' or a[i]=='8' or a[i]=='9':
        ver = 1
if ver == 1:
    print('ERROR <Your input has number in it>')
else:
    print('OK')

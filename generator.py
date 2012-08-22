file = open('images.txt', 'w')
file_min = open('images_mini.txt','w')
s='http://www.germes-doors.ru/images/doorart/%D1%8D%D0%BB%D0%B8%D1%82%D0%BD%D1%8B%D0%B5/'
name='Ellite'
max_dex= 8
max = 9
for x in range(1,max_dex + 1):
    file_min.write(s + ("%s%s0%d.jpg\n" %('small/',name,x)))
    file.write(s + ("%s0%d.jpg\n" %(name,x)))

for x in range(10,max + 1):
    file_min.write(s + ("%s%s%d.jpg\n" %('small/',name,x)))
    file.write(s + ("%s%d.jpg\n" %(name,x)))
file.close()
file_min.close()



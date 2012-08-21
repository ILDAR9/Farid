file = open('panel.txt', 'w')
for x in range(1,10):
    file.write("http://www.germes-doors.ru/images/palitra/small/0%d.jpg\n" %(x))
for x in range(10,11):
    file.write("http://www.germes-doors.ru/images/palitra/%d.jpg" %(x))
file.close()



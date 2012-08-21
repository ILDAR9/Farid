file = open('panel.txt', 'w')
for x in range(1,10):
    file.write("""<a rel="doors" class="intdoor" href="../media/indoorVariants/panel/Pannels%s%s.jpg"><img
    src="../media/indoorVariants/panel/min/Pannels%s%s.jpg"></a>\n""" %(0,x,0,x))
for x in range(10,86):
    file.write("""<a rel="doors" class="intdoor" href="../media/indoorVariants/panel/Pannels%s.jpg"><img
    src="../media/indoorVariants/panel/min/Pannels%s.jpg"></a>\n""" %(x,x))
file.close()



file = open('html_generated.html', 'w')
#atributes
folder = "hitech"
img_name = ""
max_dex = 3
max = 9

for x in range(1, max_dex + 1):
    cur_img = (("%s%d") % (img_name, x))
    file.write(("""
                <a class="intdoor" href="../media/indoorVariants/doorart/%s/%s.jpg"><img
                    alt="%s" class="pre_view"
                    src="../media/indoorVariants/doorart/%s/min/%s.jpg"></a>\n
                """
                % (folder, cur_img, cur_img, folder, cur_img)))

for x in range(10, max + 1):
    cur_img = (("%s%d") % (img_name, x))
    file.write(("""
                <a class="intdoor" href="../media/indoorVariants/doorart/%s/%s.jpg"><img
                    alt="%s" class="pre_view"
                    src="../media/indoorVariants/doorart/%s/min/%s.jpg"></a>\n
                """
                % (folder, cur_img, cur_img, folder, cur_img)))

file.close()
# should open a XML and a TRG file and create test data

from shutil import copyfile #import from library so we can use "copyfile"

x=10001
for x in range(10001,10011):  #defines the number of times through the loop, and by extension the number of files
	y = x + 1 # y is used to create an incremented number for the end of the file names
	ft = open("DOC_CSCT_VOUCHER_LT_0016276_1611091537%s.TRG"% x, "r+") #open the original/latest TRG and read
	fd = open("DOC_CSCT_VOUCHER_LT_0016276_1611091537%s.XML"% x, "r+") #open the original/latest XML and read
	fd.seek(379) #begin overwriting characters at character number defined in parens
	fd.write("LT_0016276_1611091537%s" % x) #what is written

	fd.seek(497)
	fd.write("LT_0016276_1611091537%s" % x)

	fd.seek(701)
	fd.write("L511716276_%s0915370001" % x)

	copyfile("DOC_CSCT_VOUCHER_LT_0016276_1611091537%s.XML" % x,"DOC_CSCT_VOUCHER_LT_0016276_1611091537%s.XML" % y ) #copy the now updated XML file to a new file name

	ft.write("Trip ID: LT_0016276_1611091537%s" % x) #write to the TRG file

	copyfile("DOC_CSCT_VOUCHER_LT_0016276_1611091537%s.TRG" % x,"DOC_CSCT_VOUCHER_LT_0016276_1611091537%s.TRG" % y )

	fd.close()
	ft.close()
	x += 1
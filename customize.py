HW_WEBSITE = 'http://lms.nthu.edu.tw/course.php?courseID=43630&f=hw_doclist&hw=215376'

ACCOUNT = ''
PASSWORD= ''

CSV_FILENAME = 'lab-summary.csv'


def customize_comment(grade): # return a string
    comment = ''
    for i in range(1, 6):
        comment = comment + 'lab1_' + str(i) + ' ' + str(grade['lab1_' + str(i)]) + '\n'
    
    comment = comment + 'Report ' + grade['Report']
    return comment

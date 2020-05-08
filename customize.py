HW_WEBSITE = 'http://lms.nthu.edu.tw/course.php?courseID=YOUR_SCORE_ID&f=hw_doclist&hw=YOUR_HW_ID'

CLEAR_PREVIOUS=False
# CLEAR_PREVIOUS=True # un-comment it if you want to delete previous socres on ILMS before sending the new scores

ACCOUNT = ''
PASSWORD= ''

CSV_FILENAME = 'lab-summary.csv'


def customize_comment(grade): # return a string
    comment = ''
    if int(grade['score']) < 50:
        comment += 'QAQ. 乾巴爹哭搭賽'
    else:
        comment += 'good job'
    return comment

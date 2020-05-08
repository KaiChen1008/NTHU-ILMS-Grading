FILE_NAME = 'index.html'

class hw_id_parser():
    def __init__(self):
        self.f = open('index.html')
        self.table = {}
    
    def get_table(self):
        return self.table

    def start(self):
        line = self.get_next_line()
        while not self.is_end_file(line):
            if '<tr' in line:
                self.add_student()
            line = self.get_next_line()
        
        
        # print(len(self.table))
        # for key in self.table:
            # print(key, self.table[key]) 
    
    def is_end_file(self,line):
        if '</html>' in line: return True
        return False

    def get_next_line(self):
        return self.f.readline()
    
    def add_student(self):
        # 0 <td class=td width=60 align=center>2324524</td>
        # 1 <td class=td align=left><a href='108062202/content.html'>lab1_108062202</a></td>
        # 2 <td class=td width=70 align=left>108062202</td>
        # 3 <td class=td width=55 align=left>林oo</td>
        # 4 <td class=td width=75 align=center><a href='http://lms.nthu.edu.tw/course.php?courseID=43630&f=doc&cid=2324524'>線上閱讀</a></td>
        tds = []
        for i in range(5):
            tds.append(self.get_next_line())
        
        hw_id = self.parse_id(tds[0])
        student_id = self.parse_id(tds[2])

        # self.table[student_id] = hw_id
        self.table[hw_id] = student_id
    
    def parse_id(self, td):
        # <td class=td width=60 align=center>2324524</td>
        # <td class=td width=70 align=left>108062202</td>
        start = td.find('>')
        end   = td.rfind('<')
        return td[start+1:end]

parser = hw_id_parser()
parser.start()
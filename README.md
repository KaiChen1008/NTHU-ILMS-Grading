# NTHU-ILMS-Grading

## Requirements

1. python3

## Installation

1. Find the brower's version.
   - setting -> about Chrome

<img src="https://i.imgur.com/O5YRSuc.png" style="zoom:25%;" />

2. Download the [Chrome Driver](https://chromedriver.chromium.org/downloads)

3. Unzip the file and put chromedriver under `/usr/local/bin ` (mac / linux)

   ```bash
   mv chromedriver /usr/local/bin
   ```

4. Install `selenium`.

```bash
pip install selenium
```



## Usage

- Download homeworks from ILMS.

<img src="https://i.imgur.com/EVtAxw7.gif" style="zoom:25%;" />

- Unzip the zip file and find `index.html`. Drag `index.html` to your work directory.

<img src="https://i.imgur.com/jQ9DKbR.png" style="zoom:25%;" />

- Specify `HW_WEBSITE` in `customize.py`.

```python
HW_WEBSITE = 'http://lms.nthu.edu.tw/course.php?courseID=???&f=hw_doclist&hw=???'
```

<img src="https://i.imgur.com/D9yFCQo.png" alt="ilms-page" style="zoom:25%;" />



- Setup your ILMS account in `customize.py`

  ```python
  ACCOUNT = ''
  PASSWORD= ''
  ```

  

- Summary grades in a csv file.

  - Your csv file should <font color=#bf2222>at minimum</font> contain a "ID" column" and a "score" column.
  - In csv file, each row represent a student.
  - p.s. You can generate a csv file simply using Excel or Google Sheet.

  <img src="https://i.imgur.com/DsaUNQD.png" alt="截圖 2020-05-06 上午12.19.08" style="zoom:25%;" />

- Customize your comment by modifying `customize_comment` in `custumize.py`.
  - The input `grade` is a map. 
  - The keys of `grade` are the first line of csv file.
  - Take above csv file for example. There are 7 keys in `grade`. `ID`, `Name` , `score` ...

```python
def customize_comment(grade): # return a string
    comment = ''
    comment = grade['lab1'] + ' ' + grade['lab2'] + ' ' + grade['lab3'] + '\n'
    comment = comment + 'report ' + grade['report']
    return comment

```

- Run the script

```bash
python ilms-grading.py
```

---
If this repository is useful, please give us a star :)) :blush: :blush: :blush:

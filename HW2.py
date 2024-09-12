import math
import time
from dataclasses import field
from datetime import datetime, timedelta
from functools import reduce
from logging import fatal


def q1():
    #הגדדרת פונקציה לינארי בלמבדה
    linear_fanc = lambda y: ( y/2 ) + 2

    #יצירת רשימה של מספרחם מ0 עד 10000
    numbers = list(range(10001))

    #מדידת זמן עבור פונקציית העל
    start = time.time()
    new_list = list(map(linear_fanc,numbers))#יצירת רשימה חדשה שמכילה את המספרים החדשים אחרי הפעלת הפונקציה
    sum = reduce(lambda x,y:x+y, new_list, 0)#פונקציית על שסוכמת את הרשימה
    end = time.time()
    print("פונקציית על" ,start-end)

    #מדידת זמן עבור הפונקציה האטרטיבית
    start1 = time.time()
    imp_sum = 0
    for x in new_list:
        imp_sum += x
    end1 = time.time()
    print("אופרטיבי" , end1-start1)

    #מדידת זמן עבור הקריאה לפונקציית הלמבדה וכן עבור הסכימה
    start2 = time.time()
    sum_single = reduce(lambda x ,y: x + linear_fanc(y) ,numbers, 0) # ביצוע הקריאה לפונקציה הלינארית והסכימה ב-reduce אחד
    ent2 = time.time()
    print("פונקציית על אחת" , ent2-start2)


def q2():
    numbers = list(range(1, 1001))

    #חלוקת הרשימה numbers ל2 רשימות (זוגיים ואי זוגיים)
    is_odd = lambda x: x % 2 != 0
    is_even = lambda x: x % 2 == 0

    odd_num = list(filter(is_odd,numbers))
    even_num = list(filter(is_even,numbers))

    #הפעלת הפונקציות המתאימות עבור רשימת המספרים וזוגיים והמספרים האי זוגיים
    mult_even = reduce(lambda x, y: x * y, even_num, 1)
    sum_odd = reduce(lambda x, y: x + (y / 2) + 2, odd_num, 0)

    # הצגת התוצאות
    print("תוצאת כפל הזוגיים:", mult_even)
    print("תוצאת סכום האי זוגיים:", sum_odd)


def q3(date,num_of_date,num_to_skip):
    #המרת המחרוזת לפורמט של תאריך לועזי
    date = datetime.strptime(date,"%Y-%m-%d")
    #יצירת רשימה שמחזירה את מספר הימים הרוצי אחרי הוספת הימים
    dates = list(map(lambda x: (date + timedelta(days=x*num_to_skip).strftime("%Y-%m-%d"), range(num_of_date))))

    return dates


def q4a(exponent):
    return lambda base:base**exponent


def q4b(x):
    return map(q4a,range(x))


def q4c(x,n):
    taylor = lambda taylor_term: q4a(x)(n)/math.factorial(n) #x^n/n!
    return reduce(lambda x,y:x+taylor(y), range(n+1), 0)#מחשב את סכום הtaylor_term על הx המבוקש

#q5
#בתוך הפונקציה manager_task ישנם פונקציות נוספות סמטפלות בפעולות ספצפיות
#על המילון הכללי בעזרת שימוש בclosure
#כאשר אנו שולחים פקוצה לפונקציה הmanager_task לפי שם הפקודה אנו מפעילים את הפונקציה המתאימה
def manager_task():
    tasks_manager = {}

    def add_task(task_name, status="incomplete"):
        tasks_manager[task_name]=status

    def get_task():
        return tasks_manager

    def task_complete(task_name):
        tasks_manager[task_name] = "complete"

    return {
        'add_task': add_task,
        'get_task': get_task,
        'task_complete': task_complete
    }
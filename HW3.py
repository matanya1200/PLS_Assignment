#רקורסיה
import sys
import time
import itertools


#יצירת tuple של המספרים מ1 עד n באמצעות רקורסיה


def q1rec(n):
    #אם n=1 תכניס לtuple את המספר 1 ותחזיר את הtuple
    if n == 1:
        return (1,)
    # אם n לא שווה 1 שתלח לפנקציה זו את n-1 ותכניס לtuple את n
    else:
        return q1rec(n-1)+(n,)

# יצירת tuple של המספרים מ1 עד n באמצעות רקורסיה זנבית
def q1rec_tell(n, acc = ()):
    if n == 0:
        return acc
    else:
        return q1rec_tell(n-1,(n,)+acc)

#סוכם את במספרים שבtuple בעזרת רקורסיה
def q2rec(tpl):
    if len(tpl) == 0:
        return 0
    else:
        tpl[0]+q2rec(tpl[1:])

#סוכם את במספרים שבtuple בעזרת רקורסיה זנבית
def q2rec_tell(tpl, acc = 0):
    if len(tpl) == 0:
        return acc
    else:
        return q2rec_tell(tpl[1:],acc+tpl[0])


#מוצא את המכנה המשותף המקסימלי
def q3rec_GCD(x,y):
    if y == 0:
        return x
    return q3rec_GCD(y, x % y)

#מוצא את המכפיל המשותף המינימלי
def q3rec_LCM(x,y):
    return abs(x*y)//q3rec_GCD(x,y)


#בודק בצורה רקורסיבית אם n פולינדרום
def isPalindrome(n):
    s = str(n)

    if(len(s) <= 1):
        return True

    else:
        if(s[0] != s[-1]):
            return False

    return isPalindrome(s[1:-1])


def sortedzip(lists):
    # מקרה בסיסי: אם יש רק רשימה אחת או שאין כלל רשימות, אין מה למיין או לזווג
    if not lists:
        return []
    if len(lists) == 1:
        return zip(sorted(lists[0]))

    # מיון של כל הרשימות שבפנים
    sorted_lists = [sorted(lst) for lst in lists]

    # שימוש ב-zip כדי לזווג את כל הרשימות הממוינות
    return zip(*sorted_lists)


def sortedzip_tail(lists, acc=None):
    if acc is None:
        acc = []

    if not lists:
        return zip(*acc)

    acc.append(sorted(lists[0]))

    return sortedzip_tail(lists[1:], acc)



#Lazy Evaluation, Generators
#1א
#ללא שימוש ב evaluation lazy
def create_array_eager():
    start_time = time.time()
    arr = list(range(10001))  # רשימה רגילה של המספרים
    end_time = time.time()
    print("זמן ביצוע:", end_time - start_time, "שניות")
    print("גודל בזיכרון:", sys.getsizeof(arr), "bytes")
    return arr

# תוך שימוש ב evaluation lazy
def create_array_lazy():
    start_time = time.time()
    arr = (x for x in range(10001))  # מחולל במקום רשימה
    end_time = time.time()
    print("זמן ביצוע:", end_time - start_time, "שניות")
    print("גודל בזיכרון:", sys.getsizeof(arr), "bytes")
    return arr #חוזר אוביקט מסוג generator


#1ב
#ללא שימוש ב evaluation lazy
def take_first_5000_eager(arr):
    start_time = time.time()
    new_arr = arr[:5000]
    end_time = time.time()
    print("זמן ביצוע:", end_time - start_time, "שניות")
    print("גודל בזיכרון:", sys.getsizeof(new_arr), "bytes")
    return new_arr

#תוך שימוש ב evaluation lazy
def take_first_5000_lazy(arr):
    start_time = time.time()
    new_arr = itertools.islice(arr, 5000) #מחזיר כל פעם את האיבר הבא עד שמעיה לאיבר האחרון בקפיצות של 1
    end_time = time.time()
    print("זמן ביצוע:", end_time - start_time, "שניות")
    print("גודל בזיכרון:", sys.getsizeof(new_arr), "bytes")
    return new_arr

#2
#עבור כל מספר מחזיר אם הוא רישאוני הקריאה next תחזיר את המספר הראשוני הבא אחרי שהפונקציה נעצרה בגלל הפקודה yield
def prime_generator():
    num = 2  # מתחילים עם המספר הראשוני הראשון
    while True:
        # בדיקת ראשוניות של num
        if is_prime(num):
            yield num
        num += 1

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# שימוש בגנרטור
gen = prime_generator()
print(next(gen))  # 2
print(next(gen))  # 3
print(next(gen))  # 5
print(next(gen))  # 7
print(next(gen))  # 11

#3
#מחזיר את 8 התוצאת הרשאונות
def taylor_series_generator(x):
    n = 0  # מתחילים עם n = 0
    term = 1  # האיבר הראשון בטור הוא 1 (x^0 / 0!)
    sum_taylor = term  # מחזיקים את הסכום המצטבר של האיברים
    yield sum_taylor  # מחזירים את הסכום הראשוני (האיבר הראשון)

    while True:
        n += 1
        term *= x / n  # מחשבים את האיבר הבא: (x^n / n!)
        sum_taylor += term  # מוסיפים את האיבר לסכום המצטבר
        yield sum_taylor  # מחזירים את הסכום המעודכן

# שימוש בגנרטור
gen = taylor_series_generator(2)
for _ in range(8):
    print(next(gen))
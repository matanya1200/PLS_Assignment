import math


#מקבל מספר ובודק מהPentaNumer שלו
def getPentaNum(n):
    for x in range(1, n+1):
        return n * (3 * n - 1) / 2


#מקבל 2 מספרים ומחזיר את כל הPentaNumer בין שני המספרים
def pentaNumRange(n1, n2):
        return list(getPentaNum(x) for x in range(n1, n2))


#בודק את סכם הספרות של מספר מסויים
def sumDigit(n):
    return sum(int(digit) for digit in str(n))


#מחזיר את הגימטריה של מילה
def gematria_value(word):
    gematria = {'א': 1, 'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5, 'ו': 6, 'ז': 7, 'ח': 8, 'ט': 9, 'י': 10,
                'כ': 20, 'ל': 30, 'מ': 40, 'נ': 50, 'ס': 60, 'ע': 70, 'פ': 80, 'צ': 90,
                'ק': 100, 'ר': 200, 'ש': 300, 'ת': 400}

    return sum(gematria.get(letter, 0) for letter in word)


#בודק אם המספר שהתקבל ראשוני
def isPrimes(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    if n % 2 == 0:
        return False
    for x in range(3, int(math.sqrt(n)) + 1, 2):
        if n % x == 0:
            return False

    return True


#בודק אם למספר הראשוני שהתקבל יש twin
def twin_prime(n):
    if isPrimes(n-2):
        return n-2
    if isPrimes(n+2):
        return n-2
    return None


#מחזיר מילון עם כל זוגות הtwin numbers מ0 עד n
def primes_twin_dict(n):
    primes_twin = {}
    for x in range(2, n):
        if isPrimes(x):
            twin = twin_prime(x)
            if twin is not None:
                primes_twin[x] = twin

    return primes_twin


#מקבל 3 מילונים ומחבר אותם יחד
def add3dict(d1, d2, d3):
    result = {}
    keys = set(d1.keys()).union(d2.keys()).union(d3.keys())

    for key in keys:
        value = set()
        if key in d1:
            value.add(d1[key])
        if key in d2:
            value.add(d2[key])
        if key in d3:
            value.add(d3[key])
        result[key] = tuple(value)

    return result


#מחזיר את המספר כפול 2
def mult_by_2(x):
    return x * 2


#מחזיר את המספר בחזקת 2
def square(x):
    return x ** 2


#מחזיר את האיפוך של המספר
def reciprocal(x):
    return 1 / x if x != 0 else None


#מקבל רשימה של מספרים ורשימה של פונקציות ומחזיר מילון של המספרים אחרי ביצוע הפונקציות
def apply_functions(numbers, fancs):
    results = {}
    for fanc in fancs:
        name = fanc.__name__
        fanc_result = []

        for x in numbers:
            if fanc(x) is not None:
                fanc_result.append(fanc(x))
        results[name] = tuple(fanc_result)

    return results


#מפעיל את כל הפונקציות האחרות
def main():
    num1 = input("enter a number:")
    while not (num1.isdigit()):
        num1 = input("enter a number:")
    num1 = int(num1)

    num2 = input("enter another number(grater then the first number):")
    while not (num2.isdigit()):
        num2 = input("enter another number:")
    num2 = int(num2)

    num3 = input("enter a number with more then 1 digit")
    while not (num3.isdigit()):
        num3 = input("enter a number with more then 1 digit")
    num3 = int(num3)

    word = input("Enter a Hebrew word")

    print("the PentaNumers between the 2 numbers")
    print(pentaNumRange(num1, num2))

    print("the sum of the digits of the third number")
    print(sumDigit(num3))

    print("the gematria of the word")
    print(gematria_value(word))

    print("A dictionary of each pair of twin primes")
    print(primes_twin_dict(num3))

    d1 = {1: 'a', 2: 'b'}
    d2 = {1: 'c', 2: 'd'}
    d3 = {2: 'b', 3: 'd'}

    print("the united dictionary")
    print(add3dict(d1, d2, d3))

    numbers = range(1, 6)

    functions = [mult_by_2, square, reciprocal]

    print("a dictionary of the number 1-5 after the functions")
    print(apply_functions(numbers, functions))


if __name__ == "__main__":
    main()

#כל הפונקציות הם פונקציות טהורות כיוון שהם אינם משנות משתנים חיצוניים
#חוץ מפונקציית הmain שמקבלת ערכים מהמשתמש



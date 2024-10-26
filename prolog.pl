#1
#given:
parent(X,Y), male(X), female(Y), married(X,Y)

#father
father(X, Y) :- parent(X, Y), male(X)# אבא אם הורה וגם זכר

#mather
mother(X, Y) :- parent(X, Y), female(X)# אמא אם הורה וגם נקבה

#sun
son(X, Y) :- parent(Y, X), male(X)# בן אם יש לו הורה וגם הוא זכר

#daughter
daughter(X, Y) :- parent(Y, X), female(X)# בת אם יש לה הורה גם היא נקבה

#grandfather
grandfather(X, Y) :- parent(X, Z), parent(Z, Y), male(X)# סבא אם הוא הורה והילד שלו הורה והוא זכר

#grandmother
grandmother(X, Y) :- parent(X, Z), parent(Z, Y), female(X)# סבתא אם היא הורה והילד שלה הורה והיא נקבה

#grandson
grandson(X, Y) :- parent(Y, Z), parent(Z, X), male(X)# יש לי הורה ולו יש הורה ואני זכר

#granddaughter
granddaughter(X, Y) :- parent(Y, Z), parent(Z, X), female(X)# יש לי הורה ולו יש הורה ואני נקבה

#sibling
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y# יש לx הורה ויש לy אותו הורה וx וy הם לא אותו יצור

#uncle_in_law
uncle_in_law(X, Y) :- married(X, Z), sibling(Z, P), parent(P, Y), male(X)# אני נשוי ולאשתי יש אח שיש לו ילד ואני זכר

#cousin
cousin(X, Y) :- parent(A, X), parent(B, Y), sibling(A, B)#לx יש הורה ולy יש הורה וההורים של x וy אחים

#brother_in_law
brother_in_law(X, Y) :- married(X, Z), sibling(Z, Y), male(X)#אני נשוי ולאשתי יש אח

#niece
niece(X, Y) :- sibling(Y, Z), daughter(X, Z)# יש לי אח ויש לו בת

#second_cousin
second_cousin(X, Y) :-
    parent(A, X),
    parent(B, Y),
    cousin(A, B)#יש לx והרה ויש לy הורה וההורים של x וy בני דודים

#2
#רקורסיה ורשימות

#1
#מחזירה את ההיפוך של הרשימה L

reverse([], []).  # רשימה ריקה נשארת ריקה
reverse([H|T], Reversed) :-
    reverse(T, ReversedTail),  # הפוך את שאר הרשימה
    append(ReversedTail, [H], Reversed).  # הוסף את האיבר הראשון לסוף ההיפוך

#2
#בודק אם x איבר בL
member(X, [X|_]).  # אם האיבר הראשון ברשימה הוא X, X נמצא ברשימה
member(X, [_|T]) :-
    member(X, T).  # בדוק אם X נמצא בשאר הרשימה

#3
#בודק אם הרשימה הי פולינדרום
palindrome(L) :-
    reverse(L, L).  # הרשימה היא פלינדרום אם היא שווה להיפוך שלה

#4
#מחזיר true אם הרשימה מסודרת בסדר לא יורד
sorted([]).  # רשימה ריקה נחשבת ממוספרת
sorted([_]).  # רשימה עם איבר אחד נחשבת ממוספרת
sorted([X, Y | T]) :-
    X =< Y,  # האיבר הראשון קטן או שווה לשני
    sorted([Y | T]).  # המשך לבדוק את שאר הרשימה

#5
#מחזיר את כל הפרמוטציות האפשריות של הרשימה L
permutation([], []).  # הפרמוטציה של רשימה ריקה היא רשימה ריקה
permutation(L, [H|P]) :-  # אם H הוא האיבר הראשון בפרמוטציה
    select(H, L, R),  # בחר איבר H מתוך L, והשאר את השאר כרשימה R
    permutation(R, P).  # המשך לחפש את הפרמוטציות של R

#3
#אריתמטיקה

#1א
scum(1, 1).  % בסיס: סכום עד 1 הוא 1
scum(N, Res) :-
    N > 1,
    N1 is N - 1,
    scum(N1, PartialSum),
    Res is PartialSum + N.



#1ב
sumDigits(0, 0).  # בסיס: סכום הספרות של 0 הוא 0
sumDigits(Num, Sum) :-
    Num > 0,
    LastDigit is Num mod 10,  # האיבר האחרון
    Rest is Num // 10,         # שאר המספר
    sumDigits(Rest, RestSum),
    Sum is LastDigit + RestSum.

#2א
split(0, []).  # בסיס: כאשר N הוא 0, הרשימה ריקה
split(N, [LastDigit | Res]) :-
    N > 0,
    LastDigit is N mod 10,      # האיבר האחרון
    Rest is N // 10,             # שאר המספר
    split(Rest, Res).

#2ב
create(List, Num) :-
    create_helper(List, 0, Num).

create_helper([], Num, Num).  # בסיס: כאשר הרשימה ריקה, המספר הוא מה שיש
create_helper([H | T], Acc, Num) :-
    NewAcc is Acc * 10 + H,  # הכפל ב-10 והוספת הספרה החדשה
    create_helper(T, NewAcc, Num).

#2ג
reverseNumber(Num, Reversed) :-
    split(Num, Digits),  # פיצול למספר ספרות
    reverse(Digits, ReversedDigits),  # הפוך את הרשימה
    create(ReversedDigits, Reversed).  # צור מספר מהספרות ההפוכות

#3א
intersection([], _, []).  # אם הרשימה הראשונה ריקה, החיתוך ריק
intersection([H | T], L2, [H | Z]) :-
    member(H, L2),        # אם האיבר קיים ברשימה השנייה
    intersection(T, L2, Z).
intersection([H | T], L2, Z) :-
    \+ member(H, L2),     # אם האיבר לא קיים ברשימה השנייה
    intersection(T, L2, Z).

#3ב
minus([], _, []).  # אם הרשימה הראשונה ריקה, החיסור ריק
minus([H | T], L2, [H | Z]) :-
    \+ member(H, L2),     # אם האיבר לא קיים ברשימה השנייה
    minus(T, L2, Z).
minus([H | T], L2, Z) :-
    member(H, L2),        # אם האיבר קיים ברשימה השנייה
    minus(T, L2, Z).














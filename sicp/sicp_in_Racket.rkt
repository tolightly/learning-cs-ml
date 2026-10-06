#lang racket
;;; Constants
(define tolerance 0.000001)


;;; -------- General math procedures --------

;; Average procedure that takes two numbers and returns arithmetic mean of them
(define (average a b)
  (/ (+ a b) 2))
;; Square procedure that take one number and returns it's square
(define (square x)
  (* x x))

;;; -------- Square root (Newton's method) SICP 1.1.7 --------

; Return the square root of x using Newton method.
; Formal parameters:
;    x - radicand - значення, квадратний корінь якого ми шукаємо.
;       Assertion: x >= 0.
(define (sqrt-newton x)
  ; Helper predicate that verifies the accuracy of an guess based on it's magnitude of change
  (define (good-enough? guess previous-guess)
    (< (abs (- guess previous-guess)) tolerance))

  ; Helper procedure that improve guess using Newton's method - averaging guess and (/ x guess)
  (define (improve guess x)
    (average guess (/ x guess)))
  #|
    Helper procedure that recursively improves guess until it becomes sufficiently accurate
        Formal parameters:
            x: radicand - значення, квадратний корінь якого ми шукаємо.
            Assertion: x >= 0.
            guess: значення, щодо якого ми припускаємо, що воно є квадратним коренем x і це твердження слід перевірити.
            previous-guess: значення guess з попередньої ітерації для перевірки умови зупинки.
    Якщо наше припущення достатньо точне, то ми повертаємо це припущення як результат - квадратний корінь x.
    Якщо припущення неточне, то рекурсивно викликаємо всю процедуру знову, але передаємо покращене припущення.
    |#
  (define (sqrt-iter guess previous-guess x)
    (if (good-enough? guess previous-guess)
        guess
        (sqrt-iter (improve guess x) guess x)))
  
  (sqrt-iter 1.0 0.0 x))








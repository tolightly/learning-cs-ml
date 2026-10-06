#lang racket
;;; Constants
(define tolerance 0.01)


;;; -------- General math procedures --------

;; Average procedure that takes two numbers and returns arithmetic mean of them
(define (average a b)
  (/ (+ a b) 2))
;; Square procedure that take one number and returns it's square
(define (square x)
  (* x x))

#|
Procedure for finding square root using Newton method.
Formal parameters:
    x - radicand - значення, квадратний корінь якого ми шукаємо.
        Assertion: x >= 0.
    guess - значення, щодо якого ми припускаємо, що воно є квадратним коренем x і це твердження слід перевірити.
Якщо наше припущення достатньо точне, то ми повертаємо це припущення як результат - квадратний корінь x.
Якщо припущення неточне, то рекурсивно викликаємо всю процедуру знову, але передаємо покращене припущення.
|#
(define (sqrt-iter guess x)
  (if (good-enough? guess x)
      guess
      (sqrt-iter (improve guess x) x)))

(define (improve guess x)
  (average guess (/ x guess)))

(define (good-enough? guess x)
  (< (abs (- x(square guess))) tolerance))

(define (sqrt-newton x)
  (sqrt-iter 1.0 x))
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
    Procedure for finding the square root using Newton's method.
    Formal parameters:
      x - radicand: the number whose square root is sought.
          Assertion: x >= 0.
      guess - current candidate for the square root of x; it has to be checked.
    If the guess is accurate enough, return it as the result: the square root of x.
    Otherwise call the procedure recursively with an improved guess.
  |#
  (define (sqrt-iter guess previous-guess x)
    (if (good-enough? guess previous-guess)
        guess
        (sqrt-iter (improve guess x) guess x)))

  (if (= x 0)
      0
      (sqrt-iter 1.0 0.0 x)))







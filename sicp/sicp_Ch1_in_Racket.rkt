#lang racket
;;; Macros
(define-syntax-rule (assert expr)
  (when (not expr)
    (error 'assert "Assertion failed: ~s" 'expr)))
    

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
    (< (/ (abs (- guess previous-guess)) guess) tolerance)) ;In this case need to check relative error for very small or big values

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

;;; -------- Finding fixed point of functions SICP 1.3.3 --------
;; Procedure for finding the fixed point of given function
(define (fixed-point f first-guess)
  ; The failure class: functions with fixed point = 0 and function with convergence |f(x)| = q*|x| around 0 
  ; Helper predicate that verifies the accuracy of an guess based on it's magnitude of change
  (define (good-enough? next-guess guess)
    ;In this case need to check relative error for very small or big values
    ;If next-guess is negative, then (/ (abs (- next-guess guess)) next-guess) is always less than tolerance. So we need to use (/ (abs (- next-guess guess)) (abs next-guess)) 
    ;Another problem: division by 0 when next-guess is 0.
    (if (= 0 next-guess)
        (< (abs (- next-guess guess)) tolerance) ;From note sicp_1_1_7.md "How the relative error breaks down at x == 0 in sqrt_newton"
        (< (abs (/ (- next-guess guess) next-guess)) tolerance)))
  ; An iterative procedure that is intended to improve a guess regarding a fixed point by applying f to the previous guess.
  ; If the guess values change only slightly (within the tolerance), the procedure terminates and returns the guess as result.
  (define (try guess)
    (let ((next-guess (f guess)))
      (if (good-enough? next-guess guess)
          next-guess
          (try next-guess))))
  (try first-guess))
; Example of defining function to evaluate square root with fixed-point function
(define (sqrt-fixed-point x)
  (if (< x 0)
      (error "Square root can evaluate only from positive numbers")
      (if (= x 0) 0
          (fixed-point (lambda (y) (average y (/ x y))) 1.0))))  
; Example of defining golden ratio as fixed point
(define golden-ratio (fixed-point (lambda (x) (+ 1 (/ 1 x))) 1.0))
; Asserts
(assert (< (abs (/ (- (sqrt-fixed-point 1e-14) 1e-7) 1e-7)) tolerance))
(assert (< (abs (/ (- (sqrt-fixed-point 10000000000000000) 100000000) 100000000)) tolerance))
(assert (< (abs(/ (- golden-ratio 1.6180339887) 1.6180339887)) tolerance))
(assert (< (abs(/ (- (fixed-point cos 1.0) 0.739085) 0.739085)) tolerance))
(assert (< (abs(/ (- (fixed-point (lambda (x) (- (/ x 2) 1)) -10.0) -2.0) -2.0)) tolerance))
(assert (< (abs (- (fixed-point (lambda (x) (/ x 2)) 1.0) 0.0)) tolerance))
(assert (< (abs (- (fixed-point (lambda (x) (* x x)) 0.9) 0.0)) tolerance))

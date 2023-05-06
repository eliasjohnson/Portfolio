;Program: this program is a prime number detector
;Author: Elias Johnson
;Purpose: Final Project CS2810

.ORIG x3000

;Getting User Input
;Display instructions to user 
LEA R0, WELCOME ; declare label
PUTS
LEA R0, STEP_1 ; declare label
PUTS
LEA R0, STEP_2 ; declare label
PUTS
LEA R0, STEP_3 ; declare label
PUTS
LEA R0, STEP_4 ; declare label
PUTS
HALT

;writing out the statements 
WELCOME .STRINGZ "Hello User, this program is the LC-3 Prime number detector.\n\n"
STEP_1 .STRINGZ "Type in any number between 0 and 999 to see if "
STEP_2 .STRINGZ "your number is prime or \nnot.  For single or "
STEP_3 .STRINGZ "double digits numbers, type in a 0 in the first "
STEP_4 .STRINGZ "\nand or second number places: "

;;;Hundreds place 
LEA R0, OUTPUT
PUTS
OUTPUT .STRINGZ "The number you input, "

HUNDRED GETC ; accepts user input between 0 and 9
OUT
HUNDRED_ADD ADD R2, R0, #-16 ; sets the variable for the hundreths place and first input

ADD R2, R2, #-16 ; Converts the hundred
ADD R2, R2, #-16 ; now into ASCII decimal
JSR VALIDATE

ADD R3, R3, #10 ; Setting r3 to 10 for the multiplication subroutine
HUNDRED_SUB JSR MULTIPLICATION ; calls the multiplication subroutine
ADD R2, R6, #0 ; sets r2 to the result of the subroutine
ADD R6, R4, #0 ; Clears r6 for the subroutine
HUNDRED_SUB_2 JSR MULTIPLICATION ; calls the multiplication subroutine
ADD R5, R6, #0 ; Sets R5 to the result of the multiplication subroutine
ADD R6, R4, #0 ; Clears R6 for the multiplication subroutine
ADD R2, R4, #0 ; Clears R2 for the multiplication Sub

;;; Tens place
TEN GETC ; gets user input between 0 and 9
OUT
TEN_ADD ADD R2, R0, #-16 ; Sets the variable ten, now the second user input
ADD R2, R2, #-16 ; Converts ten's decimal
ADD R2, R2, #-16 ; into Ascii decimal
JSR VALIDATE

TEN_SUB JSR MULTIPLICATION ; calls the multiplication subroutine
ADD R3, R4, #0 ; Clears R3 for later code 
ADD R4, R5, #0 ; Sets R4 to hundred's place value
ADD R5, R6, #0 ; Sets R5 to Ten's place value

;;;Steps for one's place
ONE GETC ; Takes user input between 0 and 9
OUT
ONE_ADD ADD R2, R0, #-16 ; Sets variable "One" == third user input
ADD R2, R2, #-16 ; converts ones decimals 
ADD R2, R2, #-16 ; into ASCII decimal
ADD R6, R2, #0 ; Sets R6 == R2
JSR VALIDATE

;;; Creating full input value
ADD R4, R4, R5 ; Sets R1 == hundreds place value + Tens place value
ADD R4, R4, R6 ; sets R1 == (hundreds place + tens place) + ones place value
ADD R1, R3, #0 ; Clears R1 for prime number check part 2
ADD R2, R3, #1 ; sets R2 for prime check part 2
ADD R3, R3, #2 ; sets R3 for prime check part 2
ADD R5, R4, #0 ; creates modulus value for division loop in part 2
ADD R6, R4, #-2 ; creates counter for division loop in part 2

;Part 2: Prime number checking

;First Prime check
ADD R4, R4, #0 ; Creates variable for BRz testing
BRz ELSE_ZERO ; jumps to else zero if R4 == 0
ADD R4, R4, #-1 ; Decrements input for Brz Testing
BRz ElSE_ONE ; Jumps to Else_one if R4 == 1
ADD R4, R4, #-1 ; Decrements input for BRz testing
BRz ELSE_TWO ; Jumps to else_two if R4 == 2
ADD R4, R4, #2 ; Sets R4 back to original input

;Prime Loop
LOOP ADD R6, R6, #-1 ; Decrements loop counter by one at the start of each loop start 
BRnz PRIME ; Jumps to "prime" when counter reaches zero 
JSR DIVISION; calls division subroutine to check if R4 is divisible by R3 
DIV_BREAK ADD R3, R3, #1 ; Increaments R3 by 1 at the then end of each loop
BRp LOOP ; Jumps to beginning of loop 

;Part 2.5 Multiplication/ Division & validation

;number validation check
VALIDATE AND R1, R1, #0 ; Clears R1 for chatacter checking 
ADD R0, R2, #0 ; sets R2 == input character
BRn ERROR_MESSAGE ; Logs error message if R2 is less than 0
ADD R0, R0, #-10 ; R0 = R0 = - 10 (R0 -= 10)
BRzp ERROR_MESSAGE ; Logs error message if R2 is greater than 9
RET ; Ends the subroutine if the character is between 0 and 9
ERROR_MESSAGE LEA R0, ERROR;
PUTS
JSR BROKEN
ERROR .STRINGZ ", is not a valid number, please reset the \nprogram and try again."

;Division Subroutine
DIVISION ADD R5, R5, #0 ; creates start of subroutine
NOT R3, R3 ; Turn's R3 positibe value 
ADD R3, R3, #1 ; into a negative value
DIV_START ADD R5, R5, R3; R5 = R5 - R3 
BRn DIV_END ; Jumps to "DIV_END" if the r5 < 0
BRz COMPOSITE ; jumps to composite if R5 == 0
JSR DIV_START ; Return to beginning of start loop
DIV_END NOT R3, R3 ; Turns R3 negative value 
ADD R3, R3, #1 ; into a positive value
ADD R5, R4, #0 ; Resets R4 for repeat subroutine calls
JSR DIV_BREAK ; End of subroutine  

;Multiplication Subroutine 
MULTIPLICATION ADD R7, R7, #0 ; creates start of subroutine
COUNTER ADD R4, R4, R3 ; Creates couter for multiplication subroutine
RESULT ADD R6, R6, #0 ; creates storage for multiplication subroutine
MULT_START ; creates multiplication loop
ADD R6, R6, R2 ; R6 = R6 + R2
ADD R4, R4, #-1 ; decrease counter register by 1 
BRp MULT_START ; Return to beginning of start loop 
RET ; end of subroutine

; Final results
ELSE_ZERO
ElSE_ONE
LEA R0, NEITHER_RESULT
PUTS
HALT

ELSE_TWO
PRIME LEA R0, PRIME_RESULT
PUTS
HALT

COMPOSITE LEA R0, COMPOSITE_RESULT
PUTS
HALT

NEITHER_RESULT .STRINGZ ", is neither a prime nor composite"
PRIME_RESULT .STRINGZ ", is a prime number."
COMPOSITE_RESULT . STRINGZ ", is a composite number."

BROKEN ADD R0, R0 #0

.END
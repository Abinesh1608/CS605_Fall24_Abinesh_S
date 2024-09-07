### 1. **Introduction**
This document Contains the test cases and observations related to the Simple Calculator application.

### 2. **Test Cases**

| **Test Case ID** | **Description** | **Input Values** | **Expected Output** | **Actual Output** | **Status** |
|------------------|-----------------|------------------|---------------------|-------------------|------------|
| 01 | Addition of two positive integers | Num1: 10, Num2: 5, Operation: 1 (Addition) | `10 + 5 = 15` | 15 | Pass |
| 02 | Subtraction of two negative integers | Num1: -7, Num2: -3, Operation: 2 (Subtraction) | `-7 - (-3) = -4` | -4 | Pass |
| 03 | Multiplication of a positive and a negative number | Num1: 6, Num2: -2, Operation: 3 (Multiplication) | `6 * (-2) = -12` | -12 | Pass |
| 04 | Division of a number by a non-zero number | Num1: 20, Num2: 4, Operation: 4 (Division) | `20 / 4 = 5` | 5 | Pass |
| 05 | Division by zero | Num1: 15, Num2: 0, Operation: 4 (Division) | Error message: "Error! Division by zero is not allowed." | Error message displayed | Pass |
| 06 | Invalid input for operation selection | Num1: 9, Num2: 3, Operation: 5 (Invalid) | Error message: "Input Invalid! Enter a valid number between 1-4!" | Error message displayed | Pass |
| 07 | Non-numeric input for first number | Num1: "abc", Num2: 3, Operation: 1 (Addition) | Error message: "Invalid input. Please enter a valid number." | Error message displayed | Pass |
| 08 | Perform another calculation | Perform another calculation: "yes", Num1: 8, Num2: 2, Operation: 2 (Subtraction) | `8 - 2 = 6` | 6 | Pass |
| 09 | End calculation | Perform another calculation: "no" | Program ends with "Have a nice day!" | Program exits with message | Pass |

### 3. **Observations**
- The application successfully handles both valid and invalid inputs and performs arithmetic operations correctly.
- Division by zero triggers an appropriate error message.
- Invalid operation inputs are handled with a prompt asking for a valid selection.
- Repeated calculations work as expected, and the program exits cleanly when prompted.

### 4. **Conclusion**
All test cases passed successfully, and the Simple Calculator behaves as expected in terms of error handling and functional requirements.

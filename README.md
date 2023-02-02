# Character-equations

Character equation is a type of logic puzzle that can look like this:

A + AB + ACC == BCCC
Each such expression represents a mathematical equation in which some numerals are replaced by characters. (These characters often form words which make the puzzle more entertaining and attractive.) Your task is to replace the characters by digits such that the equation holds. For example, in the above equation we can replace all occurences of A with digit 9, B with 1, and C with 0, and we get

9 + 91 + 900 == 1000
which is a correct mathematical equation. It is also a Python expression which evaluates to True.

Another example of character equation may be the following puzzle and its solution:

(J + O + I + N + T)**3 == JOINT
(1 + 9 + 6 + 8 + 3)**3 == 19683

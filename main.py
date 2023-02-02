import itertools
import doctest


#functions checks if there is a number with a zero in the beginning
def zero(string):
    elements = str(string).split()
    for item in elements:
        if item != '0' and item[0] == '0':
            return False
    return string

#main function that solves the equation
def solve(equation):
    """Find all solutions to the given character equation

    :param equation: string, the specification of the character equation
    :return: list of strings, solutions to the equation,
                 all characters are replaced by numbers and the equation holds;
             empty list, if no solution is found.

    >>> solve('A + AB + ACC == BCCC')
    ['9 + 91 + 900 == 1000']
    >>> solve('(J + O + I + N + T)**3 == JOINT')
    ['(1 + 9 + 6 + 8 + 3)**3 == 19683']
    >>> solve("GO + MOO + GO == LAME")
    ['74 + 944 + 74 == 1092']
    >>> solve("NORTH / SOUTH == EAST / WEST")
    ['51304 / 61904 == 7260 / 8760']
    >>> solve('ABC + ADC == DECA')
    ['834 + 814 == 1648', '879 + 819 == 1698']
    """
    #set for unique equations that have a solution
    equations = set()
    #set for unique letters
    letters = set()
    txt = ''
    equation2 = ''
    #adds all the unique letters to the set letters
    for item in equation:
        if item.isalpha():

            letters.add(item)
    numbers = "0123456789"
    #string off all unique letters
    letter = "".join(letters)
    for item in letters:
        for perm in itertools.permutations(numbers, len(letters)):
            txt = equation.maketrans(letter, ''.join(perm))
            translated = equation.translate(txt)
            equation2 = zero(translated)
            #if the equation has a number with an initial zero then it returns False
            if equation2 == False:
                continue
            #If the evaluation is correct it adds it into the set
            if eval(equation2.translate(txt)):
                equations.add(equation2)



    equationslist = list()
    #Adds all elements from the set to a list
    for elem in equations:
        equationslist.append(elem)
    return equationslist



if __name__ == '__main__':
    doctest.testmod()




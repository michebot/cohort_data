"""Functions to parse a file containing student data."""


def unique_houses(filename):
    """TODO: Return a set of student houses.

    Iterate over the cohort_data.txt file to look for all of the included house names
    and create a set called "houses" that holds those names.

    For example:

    >>> sorted(unique_houses("cohort_data.txt"))
    ["Dumbledore's Army", 'Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']

    """

    houses = set()
    cohort_data = open("cohort_data.txt")
    for line in cohort_data:
        line = line.rstrip()
        line = line.split('|')
        if line[2] != "":
            houses.add(line[2])

    return houses


def sort_by_cohort(filename):
    """TODO: Return a list of all cohort lists, including ghosts but not instructors.

    Sort students by cohort, skipping instructors.

    Iterate over the data to create a list for each cohort. Puts ghosts into a
    separate list called "ghosts".

    For example:

    >>> sort_by_cohort("cohort_data.txt")
    [['Harry Potter', 'Mandy Brocklehurst', 'Ron Weasley', 'Oliver Wood', 'Colin Creevey', 'Cho Chang', 'Michael Corner', 'Draco Malfoy', 'Seamus Finnigan', 'Eddie Carmichael', 'Theodore Nott', 'Terence Higgs', 'Hermione Granger', 'Penelope Clearwater', 'Angelina Johnson', 'Dennis Creevey'], ['Neville Longbottom', 'Cedric Diggory', 'Pansy Parkinson', 'Anthony Goldstein', 'Padma Patil', 'Luna Lovegood', 'Eleanor Branstone', 'Lee Jordan', 'Marietta Edgecombe', 'Andrew Kirke', 'Ginny Weasley', 'Mary Macdonald', 'Blaise Zabini', 'Natalie McDonald', 'Adrian Pucey', 'Hannah Abbott', 'Graham Pritchard', 'Susan Bones', 'Roger Davies', 'Owen Cauldwell'], ['Laura Madley', 'Orla Quirke', 'Parvati Patil', 'Eloise Midgeon', 'Zacharias Smith', 'Cormac McLaggen', 'Lisa Turpin', 'Demelza Robins', 'Ernie Macmillan', 'Millicent Bullstrode', 'Percy Weasley', 'Jimmy Peakes', 'Justin Finch-Fletchley', 'Miles Bletchley', 'Malcolm Baddock'], ['Marcus Belby', 'Euan Abercrombie', 'Vincent Crabbe', 'Ritchie Coote', 'Katie Bell', 'Terry Boot', 'Lavender Brown', 'Gregory Goyle', 'Marcus Flint', 'Dean Thomas', 'Jack Sloper', 'Rose Zeller', 'Stewart Ackerley', 'Fred Weasley', 'George Weasley', 'Romilda Vane', 'Alicia Spinnet', 'Kevin Whitby'], ['Friendly Friar', 'Grey Lady', 'Nearly Headless Nick', 'Bloody Baron']]
    """
    all_students = []
    winter_16 = []
    spring_16 = []
    summer_16 = []
    fall_15 = []
    ghosts = []

    cohort_data = open("cohort_data.txt")
    for line in cohort_data:
        line = line.rstrip()
        line = line.split("|")
        name = " ".join(line[:2])
        if line[4] == "Winter 2016":
            winter_16.append(name)
        elif line[4] == "Spring 2016":
            spring_16.append(name)
        elif line[4] == "Summer 2016":
            summer_16.append(name) 
        elif line[4] == "Fall 2015":
            fall_15.append(name)
        elif line[4] == 'G':
            ghosts.append(name)

    # Code goes here
    all_students = [fall_15, winter_16, spring_16, summer_16, ghosts]
    return all_students


def hogwarts_by_house(filename):
    """TODO: Sort students into lists by house and return all lists in one list.

    Iterate over the data to create an alphabeticaly sorted list for each
    house, and sorts students into their appropriate houses by last name. Sorts
    ghosts into a list called "ghosts" and instructors into a list called
    "instructors". Add them, in that order, to your list of houses.

    For example:
    >>> hogwarts_by_house("cohort_data.txt")
    [['Abbott', 'Chang', 'Creevey', 'Creevey', 'Edgecombe', 'Nott', 'Spinnet'], ['Abercrombie', 'Bell', 'Brown', 'Coote', 'Finnigan', 'Granger', 'Johnson', 'Jordan', 'Kirke', 'Longbottom', 'Macdonald', 'McDonald', 'McLaggen', 'Patil', 'Peakes', 'Potter', 'Robins', 'Sloper', 'Thomas', 'Vane', 'Weasley', 'Weasley', 'Weasley', 'Weasley', 'Weasley', 'Wood'], ['Bones', 'Branstone', 'Cauldwell', 'Diggory', 'Finch-Fletchley', 'Macmillan', 'Madley', 'Midgeon', 'Smith', 'Whitby', 'Zeller'], ['Ackerley', 'Belby', 'Boot', 'Brocklehurst', 'Carmichael', 'Clearwater', 'Corner', 'Davies', 'Goldstein', 'Lovegood', 'Patil', 'Quirke', 'Turpin'], ['Baddock', 'Bletchley', 'Bullstrode', 'Crabbe', 'Flint', 'Goyle', 'Higgs', 'Malfoy', 'Parkinson', 'Pritchard', 'Pucey', 'Zabini'], ['Baron', 'Friar', 'Lady', 'Nick'], ['Flitwick', 'McGonagall', 'Snape', 'Sprout']]

    """

    all_hogwarts = []
    dumbledores_army = []
    gryffindor = []
    hufflepuff = []
    ravenclaw = []
    slytherin = []
    ghosts = []
    instructors = []

    # Code goes here
    # cohort_data = open("cohort_data.txt")
    with open(filename) as cohort_data:
        for line in cohort_data:
            line = line.rstrip()
            line = line.split("|")
            if line[2] == "Gryffindor":
                if line[2] != "":
                    gryffindor.append(line[1])
            elif line[2] == "Hufflepuff":
                if line[2] != "":
                    hufflepuff.append(line[1])
            elif line[2] == "Ravenclaw":
                if line[2] != "":
                    ravenclaw.append(line[1]) 
            elif line[2] == "Slytherin":
                if line[2] != "":
                    slytherin.append(line[1])
            elif line[2] == "Dumbledore's Army":
                if line[2] != "":
                    dumbledores_army.append(line[1])
            elif line[4] == 'G':
                ghosts.append(line[1])
            elif line[4] == "I":
                instructors.append(line[1])

    dumbledores_army = sorted(dumbledores_army)
    gryffindor = sorted(gryffindor)
    hufflepuff = sorted(hufflepuff)
    ravenclaw = sorted(ravenclaw)
    slytherin = sorted(slytherin)
    ghosts = sorted(ghosts)
    instructors = sorted(instructors)

    all_hogwarts = [dumbledores_army, gryffindor, hufflepuff, ravenclaw, slytherin, ghosts, instructors]

    # for list in all_hogwarts:
    #     list = sorted(list)

    return all_hogwarts


def all_students_tuple_list(filename):
    """TODO: Return a list of tuples of student data.

    Iterate over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)

    For example:

    >>> all_students_data = all_students_tuple_list("cohort_data.txt")
    >>> print(all_students_data)
    [('Harry Potter', 'Gryffindor', 'McGonagall', 'Fall 2015'), ('Laura Madley', 'Hufflepuff', 'Sprout', 'Spring 2016'), ('Orla Quirke', 'Ravenclaw', '', 'Spring 2016'), ('Marcus Belby', 'Ravenclaw', 'Flitwick', 'Summer 2016'), ('Euan Abercrombie', 'Gryffindor', 'McGonagall', 'Summer 2016'), ('Neville Longbottom', 'Gryffindor', 'McGonagall', 'Winter 2016'), ('Vincent Crabbe', 'Slytherin', 'Snape', 'Summer 2016'), ('Parvati Patil', 'Gryffindor', 'McGonagall', 'Spring 2016'), ('Mandy Brocklehurst', 'Ravenclaw', 'Flitwick', 'Fall 2015'), ('Ritchie Coote', 'Gryffindor', 'McGonagall', 'Summer 2016'), ('Eloise Midgeon', 'Hufflepuff', 'Sprout', 'Spring 2016'), ('Zacharias Smith', 'Hufflepuff', 'Sprout', 'Spring 2016'), ('Katie Bell', 'Gryffindor', 'McGonagall', 'Summer 2016'), ('Cedric Diggory', 'Hufflepuff', 'Sprout', 'Winter 2016'), ('Ron Weasley', 'Gryffindor', 'McGonagall', 'Fall 2015'), ('Cormac McLaggen', 'Gryffindor', 'McGonagall', 'Spring 2016'), ('Lisa Turpin', 'Ravenclaw', 'Flitwick', 'Spring 2016'), ('Oliver Wood', 'Gryffindor', 'McGonagall', 'Fall 2015'), ('Pansy Parkinson', 'Slytherin', 'Snape', 'Winter 2016'), ('Demelza Robins', 'Gryffindor', 'McGonagall', 'Spring 2016'), ('Terry Boot', 'Ravenclaw', 'Flitwick', 'Summer 2016'), ('Lavender Brown', 'Gryffindor', 'McGonagall', 'Summer 2016'), ('Anthony Goldstein', 'Ravenclaw', 'Flitwick', 'Winter 2016'), ('Ernie Macmillan', 'Hufflepuff', 'Sprout', 'Spring 2016'), ('Colin Creevey', "Dumbledore's Army", 'McGonagall', 'Fall 2015'), ('Padma Patil', 'Ravenclaw', 'Flitwick', 'Winter 2016'), ('Cho Chang', "Dumbledore's Army", 'Flitwick', 'Fall 2015'), ('Gregory Goyle', 'Slytherin', 'Snape', 'Summer 2016'), ('Michael Corner', 'Ravenclaw', 'Flitwick', 'Fall 2015'), ('Luna Lovegood', 'Ravenclaw', 'Flitwick', 'Winter 2016'), ('Eleanor Branstone', 'Hufflepuff', 'Sprout', 'Winter 2016'), ('Draco Malfoy', 'Slytherin', 'Snape', 'Fall 2015'), ('Marcus Flint', 'Slytherin', 'Snape', 'Summer 2016'), ('Lee Jordan', 'Gryffindor', 'McGonagall', 'Winter 2016'), ('Marietta Edgecombe', "Dumbledore's Army", 'Flitwick', 'Winter 2016'), ('Andrew Kirke', 'Gryffindor', 'McGonagall', 'Winter 2016'), ('Ginny Weasley', 'Gryffindor', 'McGonagall', 'Winter 2016'), ('Mary Macdonald', 'Gryffindor', 'McGonagall', 'Winter 2016'), ('Blaise Zabini', 'Slytherin', 'Snape', 'Winter 2016'), ('Millicent Bullstrode', 'Slytherin', 'Snape', 'Spring 2016'), ('Seamus Finnigan', 'Gryffindor', 'McGonagall', 'Fall 2015'), ('Eddie Carmichael', 'Ravenclaw', 'Flitwick', 'Fall 2015'), ('Dean Thomas', 'Gryffindor', 'McGonagall', 'Summer 2016'), ('Percy Weasley', 'Gryffindor', 'McGonagall', 'Spring 2016'), ('Jack Sloper', 'Gryffindor', 'McGonagall', 'Summer 2016'), ('Theodore Nott', "Dumbledore's Army", 'Snape', 'Fall 2015'), ('Terence Higgs', 'Slytherin', 'Snape', 'Fall 2015'), ('Jimmy Peakes', 'Gryffindor', 'McGonagall', 'Spring 2016'), ('Natalie McDonald', 'Gryffindor', 'McGonagall', 'Winter 2016'), ('Justin Finch-Fletchley', 'Hufflepuff', 'Sprout', 'Spring 2016'), ('Rose Zeller', 'Hufflepuff', 'Sprout', 'Summer 2016'), ('Miles Bletchley', 'Slytherin', 'Snape', 'Spring 2016'), ('Stewart Ackerley', 'Ravenclaw', 'Flitwick', 'Summer 2016'), ('Adrian Pucey', 'Slytherin', 'Snape', 'Winter 2016'), ('Fred Weasley', 'Gryffindor', 'McGonagall', 'Summer 2016'), ('Hannah Abbott', "Dumbledore's Army", 'Sprout', 'Winter 2016'), ('Graham Pritchard', 'Slytherin', 'Snape', 'Winter 2016'), ('George Weasley', 'Gryffindor', 'McGonagall', 'Summer 2016'), ('Hermione Granger', 'Gryffindor', 'McGonagall', 'Fall 2015'), ('Penelope Clearwater', 'Ravenclaw', 'Flitwick', 'Fall 2015'), ('Malcolm Baddock', 'Slytherin', 'Snape', 'Spring 2016'), ('Angelina Johnson', 'Gryffindor', 'McGonagall', 'Fall 2015'), ('Susan Bones', 'Hufflepuff', 'Sprout', 'Winter 2016'), ('Dennis Creevey', "Dumbledore's Army", 'McGonagall', 'Fall 2015'), ('Roger Davies', 'Ravenclaw', 'Flitwick', 'Winter 2016'), ('Romilda Vane', 'Gryffindor', 'McGonagall', 'Summer 2016'), ('Alicia Spinnet', "Dumbledore's Army", 'McGonagall', 'Summer 2016'), ('Kevin Whitby', 'Hufflepuff', 'Sprout', 'Summer 2016'), ('Owen Cauldwell', 'Hufflepuff', 'Sprout', 'Winter 2016')]
    """

    student_list = []

    with open(filename) as cohort_data:
        for line in cohort_data:
            line = line.rstrip()
            line = line.split('|')
            name = " ".join(line[:2])
            # line = tuple((name) + tuple(line[2:]))
            if line[4] != 'G' or line[4] != 'I':
                line = tuple([name, line[2], line[3], line[4]])
            # print(line)
            student_list.append(line)
    return student_list


def find_cohort_by_student_name(student_list):
    """TODO: Given full name, return student's cohort.

    Use list of tuples generated by all_students_tuple_list() to make a small
    function that, given a first and last name from the command line, return
    that student's cohort, or returns "Student not found." when appropriate.

    NOTE: This function isn't included in doctests. Test it by uncommenting the
    function call at the bottom of the file.

    For example:

    Who are you looking for? Harry Potter
    'Harry Potter was in the Fall 2015 cohort.'

    Who are you looking for? Tom Riddle
    'Student not found.'

    """

    # Code goes here

    return "Student not found."


##########################################################################################
# Further Study Questions


def find_name_duplicates(filename):
    """TODO: Return a set of student last names that have duplicates.

    Iterate over the data to find any last names that exist across all cohorts.
    Use set operations (set math) to create and return a set of these names.

    For example:
    >>> find_name_duplicates("cohort_data.txt")
    set(['Weasley'])

    """

    duplicate_names = set()

    # Code goes here

    return duplicate_names


def find_house_members_by_student_name(student_list):
    """TODO: Prompt user for a student. Display everyone in their house and cohort.

     Prompt the user for the name via the command line and when given a name,
     print a statement of everyone in their house in their cohort.

     Use the list of tuples generated by all_students_tuple_list() to make a
     small function that, when given a student's first and last name, prints
     students that are in both that student's cohort and that student's house.

     NOTE: This function isn't included in doctests. Test it by uncommenting the
     function call at the bottom of the file.

     For example:

     Choose a student: Hermione Granger
     Hermione Granger was in house Gryffindor in the Fall 2015 cohort.
     The following students are also in their house:
     Seamus Finnigan
     Angelina Johnson
     Harry Potter
     Ron Weasley
     Oliver Wood

     """

    # Code goes here

    return


#############################################################################
# Here is some useful code to run these functions without doctests!

# find_cohort_by_student_name(all_students_data)
# find_house_members_by_student_name(all_students_data)


##############################################################################
# END OF MAIN EXERCISE.  Yay!  You did it! You Rock!
#



if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if result.failed == 0:
        print("ALL TESTS PASSED")

def school_age_calculator(age, name):
    if age < 5:
        print("Enjoy the time", name, "is only", age)
    elif age ==5:
        print("Enjoy kindergarten,", name)
    else:
        print("they grow up so fast")

school_age_calculator(3, "David")
#prints out : Enjoy the time David is only 3
school_age_calculator(5, "Thomas")
#prints out : Enjoy kindergarten, Thomas   
school_age_calculator(10, "Ryan")
#prints out : 
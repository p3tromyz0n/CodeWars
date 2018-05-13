def task():
    '''
    I have a cat and a dog.

    I got them at the same time as kitten/puppy. That was humanYears years ago.

    Return their respective ages now as [humanYears,catYears,dogYears]

    NOTES:

    humanYears >= 1

    Cat Years
    15 cat years for first year
    +9 cat years for second year
    +4 cat years for each year after that

    Dog Years
    15 dog years for first year
    +9 dog years for second year
    +5 dog years for each year after that

    '''


def human_years_cat_years_dog_years(human_years):


    while human_years > 0:
        my_list = []
        if human_years == 1:
            cat = 15
            dog = 15
        else:
            cat = 15 + 9 + (human_years - 2) * 4
            dog = 15 + 9 + (human_years - 2) * 5
        my_list.insert(0, human_years)
        my_list.insert(1, cat)
        my_list.insert(2, dog)

        return my_list


def human_years_cat_years_dog_years_short(human_years):
    return [human_years, 24 + (human_years - 2) * 4 if human_years > 1 else 15, 24 + (human_years - 2) * 5 if human_years > 1 else 15]
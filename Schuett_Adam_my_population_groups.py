#file my_population_groups.py
#program conducts unit test using the populationgroup class

totalCount = 0

class PopulationGroup:

    def __init__(self, category, male, female, total):
        self.category=category
        self.male_count=male
        self.female_count=female
        self.total_count=male + female
    #calculate percentage with total
    def calculate_category_percent(self,grand_total):
        return (self.total_count/grand_total)*100


def main():
    print('Unit testing output follows...')

    #test the constructor
    print('\nTesting the constructor:')
    category = '40-44'
    male_count = 28176
    female_count = 29271
    total_count = 57447
    test_case = PopulationGroup(category, male_count, female_count, total_count)
    print(test_case.category)
    print(test_case.male_count)
    print(test_case.female_count)
    print(test_case.total_count)

    #test the method
    print('\nTesting the calculate_category_percentage method:')
    grand_total=951982 #assume grand total is 951982
    print(test_case.calculate_category_percent(grand_total))

#start main method
if __name__ == '__main__':
    main()

from Schuett_Adam_my_population_groups import PopulationGroup


def main():
# do build_population_group_list
    population = build_population_group_list()
# do calculate_column_totals
    male_total, female_total, overall_total = calculate_column_totals(population)
    #pop_group = PopulationGroup()

# sort population groups by category
    population.sort(key=by_category)
# do create_count_based_report
    create_count_based_report(population, overall_total, 'Age Group')
# do create_percentage_based_report
    create_percentage_based_report(population, overall_total, 'Age Group')

# sort population groups by total_count descending
    population.sort(key=by_totals, reverse=True)
# do create_count_based_report
    create_count_based_report(population, overall_total, 'Descending Total Count')
# do create_percentage_based_report
    create_percentage_based_report(population, overall_total, 'Descending Total Count')

# sort population groups by female_count descending
    population.sort(key=by_females, reverse=True)
# do create_count_based_report
    create_count_based_report(population, overall_total, 'Descending Female Count')
# do create_percentage_based_report
    create_percentage_based_report(population, overall_total, 'Descending Female Count')

# sort population groups by male_count descending
    population.sort(key=by_males, reverse=True)
# do create_count_based_report
    create_count_based_report(population, overall_total, 'Descending Male Count')
# do create_percentage_based_report
    create_percentage_based_report(population, overall_total, 'Descending Male Count')


def build_population_group_list():
# prompt for infile
    input_filename = input('Please enter the input filename: ')
# open infile with encoding utf8
    infile = open(input_filename, 'r', encoding='utf8')
# initialize population_groups_list
    population_groups_list = []

    for line in infile:
# split line into strings
        category, male_count, female_count, total = line.split()
# convert male_count and female_count to ints
        male_count = int(male_count)
        female_count = int(female_count)
# construct a new Population Group instance
        p1 = PopulationGroup(category, male_count, female_count, total)
# append instance to population_groups list
        if category != "Total":
            population_groups_list.append(PopulationGroup(category, male_count, female_count, total))
# close infile
    infile.close()
# return population_groups_list
    return population_groups_list


def calculate_column_totals(population_groups_list):
# Receive population_groups_list as parameter
# initialize male_total, female_total, overall_total
    male_total = 0
    female_total = 0
# for group in population_groups_list:
    for group in population_groups_list:
# accumulate male_total, female_total, overall_total
        male_total = group.male_count + male_total
        female_total = group.female_count + female_total

    overall_total = male_total + female_total
# return male_total, female_total, overall_total
    return male_total, female_total, overall_total


def create_count_based_report(population_groups_list, population_group_totals, title):
# receive population_groups_list, male_total, female_total, overall_total, title as parameters
# print blank lines
    print()
# print title
    print('{0:^40}'.format('Counts by ' + title))
# print column headings
    print('\n{0:<10}{1:>10}{2:>10}{3:>10}'.format(
'Age Group', 'Males', 'Females', 'Total'))

    for group in population_groups_list:
        print(str(group))
        print(str(population_group_totals))


def create_percentage_based_report(population_groups_list, population_group_totals, title):
# print blank lines
    print()
# print title
    print('\n{0:^40}'.format('Percentages by ' + title))
# print column headings
    print('\n{0:<10}{1:>10}{2:>10}{3:>10}'.format(
'Age Group', 'Males', 'Females', 'Total'))

    for group in population_groups_list:
# male percentage variable
        male_percentage = (group.male_count / population_group_totals.male_count)
# female percentage variable
        female_percentage = (group.female_count / population_group_totals.female_count)
# total percentage variable
        total_percentage = (group.calculate_total_count() / population_group_totals.calculate_total_count())
        print('{0:<10}{1:>10.2%}{2:>10.2%}{3:>10.2%}'.format(group.category, male_percentage, female_percentage, total_percentage))
        print('{0:<10}{1:>10.2%}{2:>10.2%}{3:>10.2%}'.format('Total', 1, 1, 1))


def by_category(pg):
    return pg.category


def by_males(pg):
    return pg.male_count


def by_females(pg):
    return pg.female_count


def by_totals(pg):
    return pg.calculate_total_count()


main()
from Schuett_Adam_my_population_groups import PopulationGroup


def main():
# do build_population_group_list
    population = build_population_group_list()
# do calculate_column_totals
    male_total, female_total, overall_total = calculate_column_totals(population)
    #pop_group = PopulationGroup()

# sort population groups by category
    population.sort(key=lambda x: x.category)
# do create_count_based_report\
# do create_percentage_based_report
    create_percentage_based_report(population, 'Age Group', male_total, female_total, overall_total)

# sort population groups by total_count descending
    population.sort(key=lambda x: x.total_count, reverse=True)
# do create_count_based_report
# do create_percentage_based_report
    create_percentage_based_report(population, 'Descending Age Group', male_total, female_total, overall_total)

# sort population groups by female_count descending
    #population.sort(key=by_females, reverse=True)
# do create_count_based_report
# do create_percentage_based_report
    population.sort(key=lambda x: x.female_count, reverse=True)
    create_percentage_based_report(population, 'Descending Female Count', male_total, female_total, overall_total)

# sort population groups by male_count descending
    #population.sort(key=by_males, reverse=True)
# do create_count_based_report
# do create_percentage_based_report
    population.sort(key=lambda x: x.male_count, reverse=True)
    create_percentage_based_report(population, 'Descending Male Count', male_total, female_total, overall_total)


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


def create_count_based_report(population_groups_list, title, male_total, female_total, overall_total):
# receive population_groups_list, male_total, female_total, overall_total, title as parameters
# print blank lines
    print()
# print title
    print('{0:^40}'.format('Counts by ' + title))
# print column headings
    print('\n{0:<10}{1:>10}{2:>10}{3:>10}'.format(
'Age Group', 'Males', 'Females', 'Total'))

    for group in population_groups_list:
        print(group.category, group.male_count, group.female_count, group.total_count)
        #print(str(population_group_totals))
    print("Total", male_total, female_total, overall_total)


def create_percentage_based_report(population_groups_list, title, male_total, female_total, overall_total):
# print blank lines
    print()
# print title
    print('\n{0:^40}'.format('Counts by ' + title))
# print column headings
    print('\n{0:<10}{1:>10}{2:>10}{3:>10}'.format(
'Age Group', 'Males', 'Females', 'Total'))

    for group in population_groups_list:
# male percentage variable
# total percentage variable
        total_percentage = 0
        if title == "Age Group" or title == "Descending Age Group":
            total_percentage = (int(group.total_count) / overall_total)
        elif title == "Descending Male Count":
            total_percentage = (int(group.male_count) / overall_total)
        elif title == "Descending Female Count":
            total_percentage = (int(group.female_count) / overall_total)
        print(group.category, group.male_count, group.female_count, "{0:.2%}".format(total_percentage))
    print("Total", male_total, female_total, "100%")


def by_category(pg):
    return pg.category


def by_males(pg):
    return pg.male_count


def by_females(pg):
    return pg.female_count


def by_totals(pg):
    return pg.calculate_total_count()


main()
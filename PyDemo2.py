countries = ["Canada", "United States", ["Germany", "Italy", "France"], ["China", "Japan", "Korea"], ["India", "Pakistan"]]
countries2 = ["Kenya", "Uganda", "Tanzania", ["South Africa", "Zambia", "Zimbabwe"], ["Mexico", "Cuba", "Jamaica", "Brazil"]]
countries[2].insert(2, "England")
print(countries)
countries2[4].insert(1, "Argentina")
print(countries2)
countries2[4].pop(1)
print(countries2)
print(len(countries))
print(len(countries2[3]))
countries2[4].sort()
print(countries2[4])
print(countries2)
print(countries[2][1])
print(countries2[4][1], countries2[4][3], countries2[4][2])
countries.extend(countries2[4])
print(countries)
countries2.insert(4, countries[3])
print(countries2)
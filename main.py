import csv
from countries_worked import main as workedCountryList

def main():
  # Opening the excel file
  file = open('countries_confirmed.csv')

  # Reading the excel file
  csv_reader = csv.reader(file)
  countries_confirmed = []

  # Iterating through rows and 
  # appending them in countries_confirmed list
  for row in csv_reader:
    if row:
      countries_confirmed.append(row[0])

  # Reading values from another module
  countries_worked = workedCountryList()

  # Finding out countries which are in countries_worked, but not in countries_confirmed
  unique_countries = set(countries_worked) - set(countries_confirmed)

  # Sorting and printing the data
  print(sorted(unique_countries))

main()
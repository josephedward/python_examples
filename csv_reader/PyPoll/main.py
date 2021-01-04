import os
import csv
import numpy as np

# read each row
csvpath = os.path.join('.', '', 'PyPoll.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    candidates_unreduced = []
    counties_unreduced = []
    row_count = 0
    print(f"CSV Header: {csv_header}")
    new_list = []
    for row in csvreader:
        new_list.append(row)
        row_count += 1
        counties_unreduced.append(row[1])
        candidates_unreduced.append(row[2])
counties = np.unique(counties_unreduced)
candidates = np.unique(candidates_unreduced)

# count totals
county_totals = [0] * len(counties)
candidate_totals = [0] * len(candidates)
for row in new_list:
    county_index = np.array(counties).tolist().index(row[1])
    county_totals[county_index] += 1
    candidate_index = np.array(candidates).tolist().index(row[2])
    candidate_totals[candidate_index] += 1
candidate_percentages = ["{0:.3f}".format(
    float((x/row_count)*100)) for x in candidate_totals]
# print("Counties: "+ str(counties))
# print("County Totals: "+str(county_totals))
# print("Candidates: "+ str(candidates))
# print("Candidate Totals: "+str(candidate_totals))
# print("Candidate Percentages: "+str(candidate_percentages)+"%")

#  convert to tuple
county_tuple = list(zip(counties, county_totals))
candidate_tuple = list(
    zip(candidate_totals, candidates, candidate_percentages))
# print("County Tuple: "+str(list(county_tuple)))
# print("Candidate Tuple: "+str(list(candidate_tuple)))


def print_election_results(row_count, county_tup, candidate_tup):
    print("***Election Results***")
    print()
    print("-------------------------")
    print()
    print("Total Votes: " + str(row_count-1))
    print()
    print("-------------------------")
    print()
    print("County Totals: ")
    print()
    for x in county_tup:
        print(f'{str(x[0])}: ({str(x[1])})')
    print()
    print("-------------------------")
    print()
    print("Candidate Totals: ")
    print()
    for x in candidate_tup:
        print(f'{str(x[1])}: {str(x[2])}% ({str(x[0])})')
    print()
    print("-------------------------")
    print()
    winner = max(candidate_tup)
    print(f'Winner: {winner[1]}')
    print()
    print("-------------------------")
    output_file = os.path.join("candidate_tuple_output.csv")
    # open the output file, create a header row, and then write the zipped object to the csv
    with open(output_file, "w", newline="") as datafile:
        writer = csv.writer(datafile)
        writer.writerow([
            "candidate_totals",
            "candidates",
            "candidate_percentages",
        ])
        writer.writerows(candidate_tuple)


print_election_results(row_count, county_tuple, candidate_tuple)

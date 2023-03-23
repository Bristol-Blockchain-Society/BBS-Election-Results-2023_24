import pyrankvote
from pyrankvote import Candidate, Ballot

# Define a function to remove duplicate candidates from a ballot
def remove_duplicate_candidates(ballots):
    for ballot in ballots:
        unique_candidates = []
        for candidate in ballot.ranked_candidates:
            if candidate not in unique_candidates:
                unique_candidates.append(candidate)
        ballot.ranked_candidates = unique_candidates
    return ballots

# Create a list of Candidate objects representing the candidates in the election
president_candidates = [Candidate("Rooj Rinchokechai"), Candidate("Yogadhveep Arora"), Candidate("Ta Chanseewong"), Candidate("Theodoros Constantinides"), Candidate("Tiberiu Toca")]

# Create a list of Ballot objects representing the votes cast in the election
raw_president_ballots = [Ballot(ranked_candidates=[president_candidates[0], president_candidates[1], president_candidates[2], president_candidates[3], president_candidates[4]]),
    Ballot(ranked_candidates=[president_candidates[0], president_candidates[1], president_candidates[3], president_candidates[4], president_candidates[2]]),
    Ballot(ranked_candidates=[president_candidates[0], president_candidates[0], president_candidates[0], president_candidates[2], president_candidates[2]]),
    Ballot(ranked_candidates=[president_candidates[3], president_candidates[0], president_candidates[2], president_candidates[4], president_candidates[1]]),
    Ballot(ranked_candidates=[president_candidates[0], president_candidates[0], president_candidates[0], president_candidates[0], president_candidates[0]]),
    Ballot(ranked_candidates=[president_candidates[0], president_candidates[4], president_candidates[2], president_candidates[3], president_candidates[1]]),
    Ballot(ranked_candidates=[president_candidates[0], president_candidates[2], president_candidates[4], president_candidates[3], president_candidates[1]]),
    Ballot(ranked_candidates=[president_candidates[0], president_candidates[3], president_candidates[2], president_candidates[1], president_candidates[4]]),
    Ballot(ranked_candidates=[president_candidates[0], president_candidates[0], president_candidates[3], president_candidates[3], president_candidates[3]]),
    Ballot(ranked_candidates=[president_candidates[4], president_candidates[0], president_candidates[2], president_candidates[3], president_candidates[1]]),
    Ballot(ranked_candidates=[president_candidates[0], president_candidates[0], president_candidates[0], president_candidates[4], president_candidates[4]]),
    Ballot(ranked_candidates=[president_candidates[2], president_candidates[0], president_candidates[4], president_candidates[3], president_candidates[1]]),
    Ballot(ranked_candidates=[president_candidates[0], president_candidates[2], president_candidates[4], president_candidates[3], president_candidates[1]]),
    Ballot(ranked_candidates=[president_candidates[2], president_candidates[0], president_candidates[3], president_candidates[4], president_candidates[1]])
]


# Remove duplicate candidates from the raw ballots
president_ballots_without_duplicates = remove_duplicate_candidates(raw_president_ballots)

# Run the STV election
election_result = pyrankvote.single_transferable_vote(president_candidates, raw_president_ballots, number_of_seats=1)

president = election_result.get_winners()[0]

# Print the election result
print("President")
print(election_result)
print(f"The winner is: {president.name}")
print("############################################")
##########################

# Create a list of Candidate objects representing the candidates for the advisor position
advisor_candidates = [Candidate("Theodoros Constantinides"), Candidate("Yogadhveep Arora"), Candidate("Nanda Girish"), Candidate("Ta Chanseewong"), Candidate("Tiberiu Toca")]

# Create a list of Ballot objects representing the votes cast for the advisor position
raw_advisor_ballots = [Ballot(ranked_candidates=[advisor_candidates[0], advisor_candidates[1], advisor_candidates[2], advisor_candidates[3], advisor_candidates[4]]),
    Ballot(ranked_candidates=[advisor_candidates[1], advisor_candidates[0], advisor_candidates[4], advisor_candidates[3], advisor_candidates[2]]),
    Ballot(ranked_candidates=[advisor_candidates[0], advisor_candidates[4], advisor_candidates[1], advisor_candidates[2], advisor_candidates[3]]),
    Ballot(ranked_candidates=[advisor_candidates[0], advisor_candidates[2], advisor_candidates[3], advisor_candidates[4], advisor_candidates[1]]),
    Ballot(ranked_candidates=[advisor_candidates[0], advisor_candidates[0], advisor_candidates[0], advisor_candidates[1], advisor_candidates[1]]),
    Ballot(ranked_candidates=[advisor_candidates[0], advisor_candidates[1], advisor_candidates[4], advisor_candidates[2], advisor_candidates[3]]),
    Ballot(ranked_candidates=[advisor_candidates[0], advisor_candidates[3], advisor_candidates[4], advisor_candidates[1], advisor_candidates[2]]),
    Ballot(ranked_candidates=[advisor_candidates[0], advisor_candidates[1], advisor_candidates[3], advisor_candidates[4], advisor_candidates[2]]),
    Ballot(ranked_candidates=[advisor_candidates[0], advisor_candidates[0], advisor_candidates[0], advisor_candidates[0], advisor_candidates[0]]),
    Ballot(ranked_candidates=[advisor_candidates[4], advisor_candidates[0], advisor_candidates[1], advisor_candidates[2], advisor_candidates[3]]),
    Ballot(ranked_candidates=[advisor_candidates[0], advisor_candidates[0], advisor_candidates[0], advisor_candidates[0], advisor_candidates[0]]),
    Ballot(ranked_candidates=[advisor_candidates[2], advisor_candidates[1], advisor_candidates[0], advisor_candidates[4], advisor_candidates[3]]),
    Ballot(ranked_candidates=[advisor_candidates[0], advisor_candidates[1], advisor_candidates[2], advisor_candidates[4], advisor_candidates[3]]),
    Ballot(ranked_candidates=[advisor_candidates[1], advisor_candidates[0], advisor_candidates[3], advisor_candidates[2], advisor_candidates[4]])
]

# Remove duplicate candidates from the raw ballots
advisor_ballots_without_duplicates = remove_duplicate_candidates(raw_advisor_ballots)

# Run the STV election
election_result = pyrankvote.single_transferable_vote(advisor_candidates, advisor_ballots_without_duplicates, number_of_seats=1)

advisor = election_result.get_winners()[0]

# Print the election result
print("Advisor")
print(election_result)
print(f"The winner is: {advisor.name}")
print("############################################")

###################################################

# Create a list of Candidate objects representing the candidates for the secretary position
secretary_candidates = [Candidate("Supak Kunopasvorakul"), Candidate("Theodoros Constantinides"), Candidate("Nanda Girish"), Candidate("Chris El Akoury"), Candidate("Tiberiu Toca")]

# Create a list of Ballot objects representing the votes cast for the secretary position
raw_secretary_ballots = [    Ballot(ranked_candidates=[secretary_candidates[0], secretary_candidates[1], secretary_candidates[2], secretary_candidates[3]]),
    Ballot(ranked_candidates=[secretary_candidates[3], secretary_candidates[0], secretary_candidates[2], secretary_candidates[1]]),
    Ballot(ranked_candidates=[secretary_candidates[3], secretary_candidates[4], secretary_candidates[0], secretary_candidates[1]]),
    Ballot(ranked_candidates=[secretary_candidates[1], secretary_candidates[0], secretary_candidates[3], secretary_candidates[4]]),
    Ballot(ranked_candidates=[secretary_candidates[0], secretary_candidates[0], secretary_candidates[0], secretary_candidates[0]]),
    Ballot(ranked_candidates=[secretary_candidates[2], secretary_candidates[4], secretary_candidates[0], secretary_candidates[3]]),
    Ballot(ranked_candidates=[secretary_candidates[0], secretary_candidates[2], secretary_candidates[3], secretary_candidates[4]]),
    Ballot(ranked_candidates=[secretary_candidates[0], secretary_candidates[1], secretary_candidates[2], secretary_candidates[4]]),
    Ballot(ranked_candidates=[secretary_candidates[4], secretary_candidates[4], secretary_candidates[4], secretary_candidates[4]]),
    Ballot(ranked_candidates=[secretary_candidates[4], secretary_candidates[2], secretary_candidates[3], secretary_candidates[0]]),
    Ballot(ranked_candidates=[secretary_candidates[3], secretary_candidates[3], secretary_candidates[3], secretary_candidates[3]]),
    Ballot(ranked_candidates=[secretary_candidates[0], secretary_candidates[3], secretary_candidates[4], secretary_candidates[1]]),
    Ballot(ranked_candidates=[secretary_candidates[2], secretary_candidates[4], secretary_candidates[3], secretary_candidates[0]]),
    Ballot(ranked_candidates=[secretary_candidates[0], secretary_candidates[4], secretary_candidates[2], secretary_candidates[1]])
]


# Remove duplicate candidates from the raw ballots
secretary_ballots_without_duplicates = remove_duplicate_candidates(raw_secretary_ballots)

# Run the STV election
election_result = pyrankvote.single_transferable_vote(secretary_candidates, secretary_ballots_without_duplicates, number_of_seats=1)

secretary = election_result.get_winners()[0]

# Print the election result
print("Secretary")
print(election_result)
print(f"The winner is: {secretary.name}")
print("############################################")
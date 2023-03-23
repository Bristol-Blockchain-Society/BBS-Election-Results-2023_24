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
president_candidates = [Candidate("Rooj Rinchokechai (First Choice)"), Candidate("Yogadhveep Arora"), Candidate("Ta Chanseewong (First Choice)"), Candidate("Theodoros Constantinides"), Candidate("Tiberiu Toca (First Choice)")]

# Create a list of Ballot objects representing the votes cast in the election
president_ballots = [Ballot(ranked_candidates=[president_candidates[0], president_candidates[1], president_candidates[2], president_candidates[3], president_candidates[4]]),
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


# Get the winner
president_ballots_without_duplicates = remove_duplicate_candidates(president_ballots)

# Run the STV election
election_result = pyrankvote.single_transferable_vote(president_candidates, president_ballots_without_duplicates, number_of_seats=1)

president = election_result.get_winners()[0]

# Print the election result
print(election_result)
print(f"The winner is: {president.name}")


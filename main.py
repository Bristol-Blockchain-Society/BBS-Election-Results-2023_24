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

###################################################

# Create a list of Candidate objects representing the candidates for the treasurer position
treasurer_candidates = [
    Candidate("Yogadhveep Arora"),
    Candidate("Supak Kunopasvorakul"),
    Candidate("Chris El Akoury"),
    Candidate("Theodoros Constantinides"),
    Candidate("Nanda Girish"),
    Candidate("Arnav Peehal"),
    Candidate("Ta Chanseewong"),
    Candidate("Tiberiu Toca")
]
#
raw_treasurer_ballots = [    Ballot(ranked_candidates=[treasurer_candidates[0], treasurer_candidates[1], treasurer_candidates[2], treasurer_candidates[3], treasurer_candidates[4], treasurer_candidates[5], treasurer_candidates[6], treasurer_candidates[7]]),
    Ballot(ranked_candidates=[treasurer_candidates[0], treasurer_candidates[2], treasurer_candidates[5], treasurer_candidates[7], treasurer_candidates[4], treasurer_candidates[6], treasurer_candidates[1], treasurer_candidates[3]]),
    Ballot(ranked_candidates=[treasurer_candidates[5], treasurer_candidates[2], treasurer_candidates[1], treasurer_candidates[6], treasurer_candidates[7], treasurer_candidates[0], treasurer_candidates[3], treasurer_candidates[4]]),
    Ballot(ranked_candidates=[treasurer_candidates[3], treasurer_candidates[2], treasurer_candidates[7], treasurer_candidates[6], treasurer_candidates[1], treasurer_candidates[0], treasurer_candidates[5], treasurer_candidates[4]]),
    Ballot(ranked_candidates=[treasurer_candidates[1], treasurer_candidates[1], treasurer_candidates[1], treasurer_candidates[1], treasurer_candidates[1], treasurer_candidates[1], treasurer_candidates[1], treasurer_candidates[1]]),
    Ballot(ranked_candidates=[treasurer_candidates[2], treasurer_candidates[3], treasurer_candidates[4], treasurer_candidates[5], treasurer_candidates[6], treasurer_candidates[7], treasurer_candidates[0], treasurer_candidates[1]]),
    Ballot(ranked_candidates=[treasurer_candidates[3], treasurer_candidates[5], treasurer_candidates[0], treasurer_candidates[2], treasurer_candidates[6], treasurer_candidates[1], treasurer_candidates[4], treasurer_candidates[7]]),
    Ballot(ranked_candidates=[treasurer_candidates[6], treasurer_candidates[1], treasurer_candidates[7], treasurer_candidates[0], treasurer_candidates[2], treasurer_candidates[5], treasurer_candidates[3], treasurer_candidates[4]]),
    Ballot(ranked_candidates=[treasurer_candidates[2], treasurer_candidates[2], treasurer_candidates[2], treasurer_candidates[2], treasurer_candidates[2], treasurer_candidates[2], treasurer_candidates[2], treasurer_candidates[2]]),
    Ballot(ranked_candidates=[treasurer_candidates[3], treasurer_candidates[2], treasurer_candidates[4], treasurer_candidates[5], treasurer_candidates[6], treasurer_candidates[7], treasurer_candidates[1], treasurer_candidates[0]]),
    Ballot(ranked_candidates=[treasurer_candidates[2], treasurer_candidates[2], treasurer_candidates[2], treasurer_candidates[2], treasurer_candidates[2], treasurer_candidates[2], treasurer_candidates[2], treasurer_candidates[2]]),
    Ballot(ranked_candidates=[treasurer_candidates[3], treasurer_candidates[3], treasurer_candidates[3], treasurer_candidates[3], treasurer_candidates[3], treasurer_candidates[3], treasurer_candidates[3], treasurer_candidates[3]]),
    Ballot(ranked_candidates=[treasurer_candidates[6], treasurer_candidates[2], treasurer_candidates[0], treasurer_candidates[1], treasurer_candidates[7], treasurer_candidates[3], treasurer_candidates[4], treasurer_candidates[5]]),
    Ballot(ranked_candidates=[treasurer_candidates[0], treasurer_candidates[4], treasurer_candidates[5], treasurer_candidates[6], treasurer_candidates[1],treasurer_candidates[3], treasurer_candidates[3], treasurer_candidates[3]])]

# Remove duplicate candidates from the raw ballots
treasurer_ballots_without_duplicates = remove_duplicate_candidates(raw_treasurer_ballots)

# Run the STV election
election_result = pyrankvote.single_transferable_vote(treasurer_candidates, treasurer_ballots_without_duplicates, number_of_seats=1)

treasurer = election_result.get_winners()[0]

# Print the election result
print("Treasurer")
print(election_result)
print(f"The winner is: {treasurer.name}")
print("############################################")

##############################################

# Create a list of Candidate objects representing the candidates for the outreach officer position
outreach_candidates = [Candidate("Yogadhveep Arora"), Candidate("Oliver Bonallack"), Candidate("Arnav Peehal"), Candidate("Theodoros Constantinides"), Candidate("Nanda Girish"), Candidate("Chris El Akoury"), Candidate("Ta Chanseewong"), Candidate("Tiberiu Toca")]

outreach_ballots = [
Ballot(ranked_candidates=[outreach_candidates[0], outreach_candidates[1], outreach_candidates[2], outreach_candidates[3], outreach_candidates[4], outreach_candidates[5], outreach_candidates[6], outreach_candidates[7]]),
Ballot(ranked_candidates=[outreach_candidates[2], outreach_candidates[0], outreach_candidates[1], outreach_candidates[6], outreach_candidates[7], outreach_candidates[3], outreach_candidates[5], outreach_candidates[4]]),
Ballot(ranked_candidates=[outreach_candidates[1], outreach_candidates[1], outreach_candidates[1], outreach_candidates[1], outreach_candidates[1], outreach_candidates[1], outreach_candidates[1], outreach_candidates[1]]),
Ballot(ranked_candidates=[outreach_candidates[3], outreach_candidates[1], outreach_candidates[5], outreach_candidates[6], outreach_candidates[7], outreach_candidates[0], outreach_candidates[4], outreach_candidates[2]]),
Ballot(ranked_candidates=[outreach_candidates[2], outreach_candidates[2], outreach_candidates[1], outreach_candidates[1], outreach_candidates[2], outreach_candidates[2], outreach_candidates[1], outreach_candidates[1]]),
Ballot(ranked_candidates=[outreach_candidates[2], outreach_candidates[1], outreach_candidates[6], outreach_candidates[3], outreach_candidates[7], outreach_candidates[0], outreach_candidates[4], outreach_candidates[5]]),
Ballot(ranked_candidates=[outreach_candidates[2], outreach_candidates[1], outreach_candidates[6], outreach_candidates[5], outreach_candidates[0], outreach_candidates[3], outreach_candidates[7], outreach_candidates[4]]),
Ballot(ranked_candidates=[outreach_candidates[1], outreach_candidates[7], outreach_candidates[2], outreach_candidates[6], outreach_candidates[3], outreach_candidates[0], outreach_candidates[4], outreach_candidates[5]]),
Ballot(ranked_candidates=[outreach_candidates[1], outreach_candidates[1], outreach_candidates[1], outreach_candidates[1], outreach_candidates[1], outreach_candidates[1], outreach_candidates[1], outreach_candidates[1]]),
Ballot(ranked_candidates=[outreach_candidates[7], outreach_candidates[1], outreach_candidates[2], outreach_candidates[6], outreach_candidates[3], outreach_candidates[5], outreach_candidates[4], outreach_candidates[0]]),
Ballot(ranked_candidates=[outreach_candidates[2], outreach_candidates[2], outreach_candidates[2], outreach_candidates[2], outreach_candidates[2], outreach_candidates[2], outreach_candidates[2], outreach_candidates[2]]),
Ballot(ranked_candidates=[outreach_candidates[5], outreach_candidates[1], outreach_candidates[2], outreach_candidates[7], outreach_candidates[3], outreach_candidates[0], outreach_candidates[4], outreach_candidates[6]]),
Ballot(ranked_candidates=[outreach_candidates[1], outreach_candidates[2], outreach_candidates[6], outreach_candidates[3], outreach_candidates[7], outreach_candidates[0], outreach_candidates[5], outreach_candidates[4]]),
Ballot(ranked_candidates=[outreach_candidates[1], outreach_candidates[2], outreach_candidates[6], outreach_candidates[3], outreach_candidates[7], outreach_candidates[0], outreach_candidates[4], outreach_candidates[5]]),
]


outreach_ballots_without_duplicates = remove_duplicate_candidates(outreach_ballots)
election_result = pyrankvote.single_transferable_vote(outreach_candidates, outreach_ballots_without_duplicates, number_of_seats=1)

outreach_officer = election_result.get_winners()[0]

print("Outreach Officer")
print(election_result)
print(f"The winner is: {outreach_officer.name}")
print("############################################")

#######################################################


# Create a list of Candidate objects representing the candidates for the media officer position
media_candidates = [Candidate("Luke Edwards"), Candidate("Yogadhveep Arora"), Candidate("Nanda Girish"), Candidate("Chris El Akoury"), Candidate("Ta Chanseewong"), Candidate("Arnav Peehal")]

media_ballots = [Ballot(ranked_candidates=[media_candidates[0], media_candidates[1], media_candidates[2], media_candidates[3], media_candidates[4], media_candidates[5]]),
Ballot(ranked_candidates=[media_candidates[0], media_candidates[0], media_candidates[0], media_candidates[0], media_candidates[0], media_candidates[0]]),
Ballot(ranked_candidates=[media_candidates[0], media_candidates[0], media_candidates[0], media_candidates[0], media_candidates[0], media_candidates[0]]),
Ballot(ranked_candidates=[media_candidates[0], media_candidates[5], media_candidates[3], media_candidates[2], media_candidates[1], media_candidates[4]]),
Ballot(ranked_candidates=[media_candidates[0], media_candidates[0], media_candidates[0], media_candidates[0], media_candidates[0], media_candidates[0]]),
Ballot(ranked_candidates=[media_candidates[0], media_candidates[3], media_candidates[2], media_candidates[1], media_candidates[4], media_candidates[5]]),
Ballot(ranked_candidates=[media_candidates[0], media_candidates[2], media_candidates[5], media_candidates[3], media_candidates[1], media_candidates[4]]),
Ballot(ranked_candidates=[media_candidates[0], media_candidates[1], media_candidates[2], media_candidates[3], media_candidates[4], media_candidates[5]]),
Ballot(ranked_candidates=[media_candidates[0], media_candidates[0], media_candidates[0], media_candidates[0], media_candidates[0], media_candidates[0]]),
Ballot(ranked_candidates=[media_candidates[0], media_candidates[3], media_candidates[2], media_candidates[1], media_candidates[4], media_candidates[5]]),
Ballot(ranked_candidates=[media_candidates[0], media_candidates[0], media_candidates[0], media_candidates[0], media_candidates[0], media_candidates[0]]),
Ballot(ranked_candidates=[media_candidates[3], media_candidates[3], media_candidates[3], media_candidates[3], media_candidates[3], media_candidates[3]]),
Ballot(ranked_candidates=[media_candidates[0], media_candidates[4], media_candidates[5], media_candidates[2], media_candidates[1], media_candidates[3]]),
Ballot(ranked_candidates=[media_candidates[0], media_candidates[5], media_candidates[4], media_candidates[2], media_candidates[1], media_candidates[3]])
]

media_ballots_without_duplicates = remove_duplicate_candidates(media_ballots)
election_result = pyrankvote.single_transferable_vote(media_candidates, media_ballots_without_duplicates, number_of_seats=1)

media_officer = election_result.get_winners()[0]

print("Media Officer")
print(election_result)
print(f"The winner is: {media_officer.name}")
print("############################################")
######################################################################

equality_candidates = [Candidate("Luke Edwards"), Candidate("Supak Kunopasvorakul"), Candidate("Theodoros Constantinides"), Candidate("Arnav Peehal")]

equality_ballots = [
    Ballot(ranked_candidates=[equality_candidates[0], equality_candidates[1], equality_candidates[2], equality_candidates[3]]),
    Ballot(ranked_candidates=[equality_candidates[0], equality_candidates[0], equality_candidates[0], equality_candidates[0]]),
    Ballot(ranked_candidates=[equality_candidates[3], equality_candidates[3], equality_candidates[3], equality_candidates[3]]),
    Ballot(ranked_candidates=[equality_candidates[2], equality_candidates[1], equality_candidates[3], equality_candidates[0]]),
    Ballot(ranked_candidates=[equality_candidates[2], equality_candidates[1], equality_candidates[3], equality_candidates[0]]),
    Ballot(ranked_candidates=[equality_candidates[1], equality_candidates[3], equality_candidates[2], equality_candidates[0]]),
    Ballot(ranked_candidates=[equality_candidates[0], equality_candidates[2], equality_candidates[1], equality_candidates[3]]),
    Ballot(ranked_candidates=[equality_candidates[3], equality_candidates[0], equality_candidates[1], equality_candidates[2]]),
    Ballot(ranked_candidates=[equality_candidates[3], equality_candidates[3], equality_candidates[3], equality_candidates[3]]),
    Ballot(ranked_candidates=[equality_candidates[2], equality_candidates[3], equality_candidates[1], equality_candidates[0]]),
    Ballot(ranked_candidates=[equality_candidates[1], equality_candidates[1], equality_candidates[1], equality_candidates[1]]),
    Ballot(ranked_candidates=[equality_candidates[3], equality_candidates[3], equality_candidates[2], equality_candidates[2]]),
    Ballot(ranked_candidates=[equality_candidates[1], equality_candidates[3], equality_candidates[0], equality_candidates[2]]),
    Ballot(ranked_candidates=[equality_candidates[3], equality_candidates[0], equality_candidates[1], equality_candidates[2]]),
]

equality_ballots_without_duplicates = remove_duplicate_candidates(equality_ballots)
election_result = pyrankvote.single_transferable_vote(equality_candidates, equality_ballots_without_duplicates, number_of_seats=1)

equality_officer = election_result.get_winners()[0]

print("Equality Officer")
print(election_result)
print(f"The winner is: {equality_officer.name}")
print("############################################")
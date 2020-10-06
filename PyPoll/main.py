import os
import csv

election_data = os.path.join("Resources", "election_data.csv")

voter_id=[]
county=[]
candidate=[]

with open (election_data) as pypoll_file:
    poll_file = csv.reader(pypoll_file, delimiter=",")

    next(poll_file)

    for line in poll_file:
        voter_id.append(line[0])
        county.append(line[1])
        candidate.append(line[2])

#Total Votes cast
total_votes=len(voter_id)

#List of Candidates

unique_list_of_candidates=[]

for i in range(total_votes):
    if candidate[i] not in unique_list_of_candidates:
        unique_list_of_candidates.append(candidate[i])

total_number_candidates=(len(unique_list_of_candidates))

# Total number of votes each candidate won

votes_for_each_candidate=[]
votes_for_candidate=0

for b in range(total_number_candidates):
    for a in range(total_votes):
        if unique_list_of_candidates[b]==candidate[a]:
            votes_for_candidate+=1
        else:
            a+=1            
    votes_for_each_candidate.append(votes_for_candidate)
    votes_for_candidate=0

# Percentage of votes each candidate won

percentage_of_votes=[]

for f in range(total_number_candidates):
    votes_for_each_candidate[f]=int(votes_for_each_candidate[f])

for d in range(len(votes_for_each_candidate)):
        e=(votes_for_each_candidate[d])/total_votes
        e=e*100
        e=format(e,'.3f')
        percentage_of_votes.append(e)



# Winner of the election

winner=votes_for_each_candidate[0]
winner_candidate=unique_list_of_candidates[0]

for g in range(total_number_candidates):
    if votes_for_each_candidate[g]>winner:
        winner=votes_for_each_candidate[g]
        winner_candidate=unique_list_of_candidates[g]

# Presentation of the results

final=[]

for c in range(total_number_candidates):
    almost_final=f'{unique_list_of_candidates[c]}: {percentage_of_votes[c]}% ({votes_for_each_candidate[c]})'
    final.append(almost_final)

result=(f"""
```
  Election Results
  -------------------------
  Total Votes: {total_votes}
  -------------------------
    {final}
  -------------------------
  Winner: {winner_candidate}
  -------------------------
  ```
""")

print(result)

# Export a text file with the results

writer =open('poll_results.txt', "w")
writer.write(result)
writer.close()

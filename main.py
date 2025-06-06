#Function: This program determines if a student will be admitted or rejected.
#Input:  Interactive
#Output: Accept or Reject

# Get input and convert to correct data type for testScore and classRank
testScoreString = input("Enter test score: ") #Get input for test score
classRankString = input("Enter class rank: ") #Get input for class rank

# Convert input strings to integers
testScore = int(testScoreString) 
classRank = int(classRankString)

# Test using admission requirements and print Accept or Reject
if testScore >= 90:
  if classRank >= 25:
    print("Accept")
  else:
    print("Reject")
else:
  if testScore >= 80:
    if classRank >= 50:
      print("Accept")
    else:
      print("Reject")
  else:
    if testScore >= 70:
      if classRank >= 75:
        print("Accept")
      else:
        print("Reject")
    else:
      print("Reject")

###############################################################################
# Overall Tasks
# 1 - Create a training set
# 2 - Train a 'dumb' rule-based classifier
# 3 - Create a test set
# 4 - Apply rule-based classifier to test set
# 5 - Report accuracy of classifier
###############################################################################

###############################################################################
# CONSTANTS
# For use as dictionary keys in training/testing sets and computation of averages
# DONE - Do not modify.
###############################################################################
attributeList = []
attributeList.append("ID")
attributeList.append("radius")
attributeList.append("texture")
attributeList.append("perimeter")
attributeList.append("area")
attributeList.append("smoothness")
attributeList.append("compactness")
attributeList.append("concavity")
attributeList.append("concave")
attributeList.append("symmetry")
attributeList.append("fractal")
attributeList.append("class")

###############################################################################
# 1. Create a training set
# - Read in file
# - Create a dictionary for each line
# - Add this dictionary to a list
#
# makeTrainingSet
# parameters: 
#     - filename: name of the data file containing the training data records
#
# returns: trainingSet: a list of training records (each record is a dict,
#                       that contains attribute values for that record.)
###############################################################################
def makeTrainingSet(filename):
    # DONE - Do not modify.
    thisTrainingSet = []
    # Read in file
    for line in open(filename,'r'):
        if '#' in line:
            continue
        line = line.strip('\n')
        linelist = line.split(',')
        # Create a dictionary for the line
        #   assigns each attribute of the record (each item in the linelist)
        #   to an element of the dictionary, using the constant keys given
        #   in attributeList
        record = {}
        for i in range(len(attributeList)):
              if(i==11): #class label is a character, not a float
                  record[attributeList[i]] = linelist[31].strip() 
              else:
                  record[attributeList[i]] = float(linelist[i])
        # Add the dictionary to a list
        thisTrainingSet.append(record)        

    return thisTrainingSet

###############################################################################
# 2. Train 'Dumb' Classifier
# trainClassifier
# parameters:
#     - trainingSet: a list of training records (each record is a dict,
#                     that contains attribute values for that record.)
#
# returns: a dictionary of midpoints between the averages of each attribute's
#           values for benign and malignant tumors
###############################################################################
def trainClassifier(thisSet):
    mean_list = {}

    for i in range(1, 11):
        sum_list = []
        for obs in thisSet:
            sum_list.append(obs[attributeList[i]])
        mean_list[i] = sum(sum_list) / len(thisSet)

    thisClassifier = {'perimeter': mean_list[1], 'symmetry': mean_list[2], 'area': mean_list[3],
                     'concave': mean_list[4], 'texture': mean_list[5], 'concavity': mean_list[6],
                     'radius': mean_list[7], 'compactness': mean_list[8], 'fractal': mean_list[9],
                     'smoothness': mean_list[10]}

    return thisClassifier

###############################################################################
# 3. Create a test set
# - Read in file
# - Create a dictionary for each line
# - Initialize each record's predicted class to '0'
# - Add this dictionary to a list
#
# makeTestSet
# parameters: 
#     - filename: name of the data file containing the test data records
#
# returns: testSet: a list of test records (each record is a dictionary
#                       that contains attribute values for that record
#                       and where the predicted class is set to 0. 
###############################################################################
def makeTestSet(filename):

    # DONE - Do not modify.
    testset = makeTrainingSet(filename)

    for record in testset:
        record["predicted"] = 0

    return testset


###############################################################################
# 4. Classify test set
#
# classifyTestRecords
# parameters:
#      - testSet: a list of records in the test set, where each record
#                 is a dictionary containing values for each attribute
#      - classifier: a dictionary of midpoint values for each attribute
#
# returns: testSet with the predicted class set to either benign or malignant
#
# for each record, if the majority of attributes are greater than midpoint (which is
# stored in the classifier) then predict the record as malignant
###############################################################################
def classifyTestRecords(thisSet, thisClassifier):

    classifier_values = list(thisClassifier.values())
    for obs in thisSet:
        values = list(obs.values())
        count = 0
        for index in range(1, 11):
            if values[index] > classifier_values[index - 1]:
                count += 1

        if count > 5:
            obs['predicted'] = 'M'
        else:
            obs['predicted'] = 'B'

    return thisSet


###############################################################################
# 5. Report Accuracy
# reportAccuracy
# parameters:
#      - testSet: a list of records in the test set, where each record
#                 is a dictionary containing values for each attribute
#                 and both the predicted and actual class values are set
#
# returns: None
###############################################################################
def reportAccuracy(thisSet):
    score = 0
    for obs in thisSet:
        if obs['class'] == obs['predicted']:
            score += 1
    accuracy = int(score/len(thisSet) * 100)
    cases = len(thisSet)
    print("There are " + str(score) + " correct predictions out of " + str(cases)
          + " cases. The accuracy rate is " + str(accuracy) + "%.")

###############################################################################
# main - starts the program
###############################################################################
def main():

    print ("Reading in training data...")           # This is task 1
    trainingFile = "cancerTrainingData.txt"
    trainingSet = makeTrainingSet(trainingFile)
    print ("Done reading training data.\n")

    print ("Training classifier...")                # This is task 2
    # add call to appropriate function
    classifier = trainClassifier(trainingSet)
    print ("Done training classifier.\n")

    print ("Reading in test data...")               # This is task 3
    testFile = "cancerTestingData.txt"
    testSet = makeTestSet(testFile)
    print ("Done reading test data.\n")

    print ("Classifying records...")                 # This is Task 4
    # add call to appropriate function
    thisSet = classifyTestRecords(testSet, classifier)

    print ("Done classifying. Check accuracy.\n" )  # this is Task 5
    # add call to appropriate function
    reportAccuracy(thisSet)

    print ("Program finished.")
    
main()
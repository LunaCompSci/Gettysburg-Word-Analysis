#Christina Nguyen, 3/15, gives unique words out of a text, and other data

def main():
    uniqueWordSet = readFile("GettysburgAddress.txt")  #calls functions
    alphaSortedList = generateSortedList(uniqueWordSet)
    longestWord, lenOfLongestWord = findLongest(uniqueWordSet)
    listofWordFreqs = generateLenFreqs(uniqueWordSet, lenOfLongestWord)
    writeWordFile(alphaSortedList)
    
    print("Number of distinct words:", len(alphaSortedList)) #prints output
    print("Length of longest word:", lenOfLongestWord)
    print("Longest word:", longestWord, "\n")
    for idx in range(len(listofWordFreqs)):
        
        print("Length =   ", format(idx + 1, "2,.0f"), " , Count =   ", format(listofWordFreqs[idx], '2,.0f'))
     
def readFile(txtFile): #reads file
    uniqueWordSet = set()
    file = open(txtFile, "r")
    words = file.readlines()

    for oneLine in words:
        wordList = oneLine.strip().split(" ")

        for oneWord in wordList:
            uniqueWordSet.add(oneWord)

    file.close()
    return uniqueWordSet

def generateSortedList(uniqueWordSet):
    uniqueWordListAsList = list(uniqueWordSet)
        
    for passIdx in range(len(uniqueWordListAsList) - 1): #sorts list into alphabetical order
         smallestIdx = passIdx
         for checkIdx in range(passIdx + 1, len(uniqueWordListAsList)):
             if uniqueWordListAsList[checkIdx] < uniqueWordListAsList[smallestIdx]:
                 smallestIdx = checkIdx
         temp = uniqueWordListAsList[passIdx]
         uniqueWordListAsList[passIdx] = uniqueWordListAsList[smallestIdx]
         uniqueWordListAsList[smallestIdx] = temp

    return uniqueWordListAsList

def findLongest(alphaSortedList): #finds the longest word and len of longest word
     numOfUniqueWords = len(alphaSortedList)
    
     longestWord = ''

     for oneWord in alphaSortedList: 
        if len(oneWord) > len(longestWord):
            longestWord = oneWord

     lenOfLongestWord = len(longestWord)
     return longestWord, lenOfLongestWord
    
def writeWordFile(alphaSortedList): #writes to file
    file = open("GettysburgWord.txt", 'w')
    for word in alphaSortedList:
        file.write(word + "\n")
    file.close()

def generateLenFreqs(alphaSortedList, lenOfLongestWord): #finds the frequency of words
    wordLenFreq = [0] * lenOfLongestWord 

    for oneWord in alphaSortedList:
        wordLenFreq[len(oneWord) - 1] += 1 
       
    return wordLenFreq

if __name__ == '__main__':
    main()

#I started off writing very detailed psuedocode then programing one function at a time. 
#Places where I got stuck:
#I split before stripping which gave me an error.
#When I was first trying my psuedocode I thought I had to have a nested loop for generateLenFreqs.
#I was trying to use the ord() on the selection sort. 

#How I got unstuck:
#I realized I can't strip on a list.
#I initialized a list of al 0s with the length of the word instead.
#I realized I was working with the indexs, not the values and therefore I didn't need the ASCII. 

#Test cases:
#When the file is empty I get a traceback error.
#When the file was all spaces (I chose to do use 5 spaces) this was my output. 
##Number of distinct words: 0
##Length of longest word: 0
##Longest word:

#From this assignment I learned how to use lists and sets and convert between the two.
#On the next assignment I'll start earlier so I can get to the extra credit. 

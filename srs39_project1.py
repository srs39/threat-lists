#Samantha Shoecraft Tcss 143 A
#user input to open files for reading
attendees = input("Please enter the name of the file of the attendees: ")
threat_list = input("Please enter the name of the file with the suspect names: ")

#open files for reading and writing
attendee = open( attendees, "r")
threat = open( threat_list, "r")
matches = open("matches.csv", "w")

#create empty lists and variables
attendee_names = []
attendee_first = []
attendee_last = []
threat_names = []
threat_first = []
threat_last = []
match_70 = [] 
match_90 = []
match_80 = []
perfect_match = []

#attendee_names = []*len(threat_names)
#attendee_first = []*len(threat_names)
#attendee_last = []*len(threat_names)
#threat_names = []*len(threat_names)
#threat_first = []*len(threat_names)
#threat_last = []*len(theat_names)
#match_70 = [] *len(threat_names)
#match_90 = [] *len(threat_names)
#match_80 = [] *len(threat_names)
#perfect_match = [] *len(threat_names)

vowels = "AEIOUaeiou"
#seperate names into lists using .readlines and .append
for row in attendee.readlines():
    row = row.strip()
    line = row.split()
    attendee_names.append(row)
    attendee_first.append(line[0])
    attendee_last.append(line[1])

for row in threat.readlines():
    row = row.strip()
    line = row.split()
    threat_names.append(row)
    threat_first.append(line[0])
    threat_last.append(line[1])
#test lists
#test_first = attendee_first[:13]
#test_last = attendee_last[:13]
#print(test_first)
#print(test_last)
#testattendees_list = attendee_names[:13]
#creat lists for matches
match_first = []
match_last = []
total_match = []
#get matches for first and last names and append to lists making sure that
#i went by the shorter index so as not to get out of range error
def getMatchNum (tname, aname, mplace):
    index = 0
    for item in range(len(tname)):
        threatn = tname[item]
        mplace.append([])
        dexz = 0
        for dex in range(len(aname)):
            attendn = aname[dexz]
            
            if len(threatn) == len(attendn) or len(threatn)<len(attendn):
                numright = addToMatch(threatn,attendn,threatn)
            else:
                numright = addToMatch(attendn,attendn,threatn)

            mplace[item].insert(dexz, numright)
            index += 1
            dexz+=1
def addToMatch(whichlist,attendee,threat):
    numright = 0
    for i in range(len(whichlist)):
        if attendee[i]== threat[i]:
            numright += 1
        elif attendee[i] in vowels and threat[i]=="@":
            numright += .75
        elif attendee[i] not in vowels and threat[i] == "$":
            numright += .5
    return numright
#getMatchNum(threat_first,test_first,match_first)
#print(match_first)
#getMatchNum(threat_first,test_last,match_last)
#print(match_last)
getMatchNum(threat_first,attendee_first,match_first)
#print (match_first)    
#compare letters in last names
getMatchNum(threat_last,attendee_last,match_last)

#print(match_last)
#add number right in first and last name and append to new list, total_match
index = 0
for item in match_first:
    total_match.append([])
    for i in range(len(item)):
        tright = item[i] + match_last[index][i]
        total_match[index].insert(i, tright)
    index += 1            
#print (total_match)
result= []    
#devide number right by the length of threat_names
indexx = 0
matchCount = 0
#sort names by percentages and append to appropriate list if 70% or above
# and print out the perfect and over 80% matches
def insertResult (operator, category, idex):
        if operator:
            category[indexx].insert(idex,aname)
for item in range(len(threat_names)):
    tname = threat_names[item]
    tleng = len(threat_names[item])
    perfect_match.append([])
    match_90.append([])
    match_80.append([])
    match_70.append([])
    for dex in range(len(attendee_names)):
        aname = attendee_names[dex]
        aleng = len(attendee_names[dex])
        if aleng >= tleng:
            result = total_match[item][dex]/(aleng-1)
            #print (result)
        #elif tlen > aleng:
        elif aleng < tleng:
            result = total_match[item][dex]/(tleng-1)
        
        #print matches that are perfect match or greater than or equal to 90%
        if result == 1:
            print("###################################################")
            print("Perfect Match")
            print("Threat:{}".format(tname))
            print("Attendee: {}".format(aname))
            print("###################################################")
            matchCount += 1
        elif result >= .9:
            print("###################################################")
            print("> 90% match:")
            print("Threat:{}".format(tname))
            print("Attendee: {}".format(aname))
            print("###################################################")
            matchCount += 1 
        insertResult(result ==1, perfect_match,dex)
        insertResult(result >= .9 and result < 1, match_90, dex)
        insertResult(result >= .8 and result < .9, match_80, dex)
        insertResult(result >= .7 and result < .8, match_70, dex)
        #print(result)
    indexx +=1
        
    
print("[90,100] matches: {}".format(matchCount))
idexs = 0
#write names to file according to threat list suspect and match level
matches.write("Suspect Name ")
matches.write("Matches")
matches.write("\n")
def writeToFile(match_list,match_level,space,match_string):
    matches.write("\n")
    matches.write("{}{} % matches: ".format(match_level,space))
    matches.write("{},".format(len(match_list[idexs])))
    for nm in match_list[idexs]:
        match_string += (nm+ ',')
        #matches.write(match_string.lstrip(',')
    matches.write(match_string.strip(','))

for item in threat_names:
    m100 = ''
    m90 = ''
    m70 = ''
    m80 = ''
    matches.write(item)
    writeToFile(perfect_match,100,'', m100)
    writeToFile(match_90, 90,' ', m90)
    writeToFile(match_80, 80,' ', m80)
    writeToFile(match_70, 70,' ', m70)
    matches.write("\n")
    idexs+=1

#print(non_match)
#print(perfect_match)
#print(match_90)
#print(match_80)
#print(match_70)

#close files
attendee.close()
threat.close()
matches.close()

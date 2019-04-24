"""
A time is palindrome in format HH:MM is defined as 
        
        | AB:AB if A==B and AB in [00,11,22]
        | AB:BA if AB not in [6,7,8,9,16,17,18,19]
HH:MM = | 10:01 if AB in [6,7,8,9]
        | 20:02 if AB in [16,17,18,19]

"""

def getInFormat(ab):
    if ab >= 0 and ab <= 9:
        return '0' + str(ab)
    else:
        return str(ab)

def getReverse(hh):
    hhList = list(hh)
    hhList.reverse()
    strhh = ''.join(hhList)
    return strhh

def findNextPalinTime(hh, mm):
    if hh in ['06','07','08','09']:
        return '10:01'
    if hh in ['16','17','18','19']:
        return '20:02'

    ab = hh
    ba = getReverse(hh)
    if ba > mm:
        return ab + ':' + ba
    else:
        ab1 = int(ab) + 1
        ab = getInFormat(ab1)
        ba = getReverse(ab)
        return ab + ':' + ba

if __name__ == '__main__':

    try:
        hhmm = raw_input("Enter time in HH:MM format ")
        if ':' not in hhmm:
            raise Exception("Time must have : to separate HH and MM")

        hhmmList = hhmm.split(':')
        if len(hhmmList) < 2 or len(hhmmList) > 2:
            raise Exception("Time entered must be in formate HH:MM")

        hh = hhmmList[0]
        mm = hhmmList[1]
        if hh < '0' or hh > '23':
            raise Exception("Entered hours is invalid")
        if mm < '0' or mm > '59':
            raise Exception("Entered minutes is invalid")

        res = findNextPalinTime(hh, mm)
        print "Next palindrome time is %s" % res

    except Exception as error:
        print repr(error)
        print "Enter the time in correct format!"

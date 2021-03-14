import datetime

dateFormat = '%Y-%m-%d'


def dict_factory(cursor, rows):
    print('row: ', rows)
    print('cursor: ', cursor.description)
    dl = []

    for row in rows:
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        dl.append(d)

    print('output: ', dl)
    return dl


def represents_int(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def valid_date(dateString):
    try:
        datetime.datetime.strptime(dateString, dateFormat)
        return True
    except ValueError:
        return False

def past_date(dateString):
    srcDate = datetime.datetime.strptime(dateString, dateFormat)
    
    currentDateString = datetime.date.today().strftime(dateFormat)
    todayDate = datetime.datetime.strptime(currentDateString, dateFormat)

    if srcDate == todayDate:
        return False
    else:
        return True

def validate_name(names, host_or_participant):
    # if each participant name is not greater than 100 characters
    # total number of participants are not greater than 10
    MAX_PARTICIPANT_COUNT = 10
    MAX_NAME_CHARS = 100
    delimiter = ','
    errorMsg = {}
    participantCount = len (names.split(delimiter))
    if  participantCount > MAX_PARTICIPANT_COUNT:
        errorMsg = {'participantCountError':'Number of participants is {} which is greater than {}'.format(participantCount, MAX_PARTICIPANT_COUNT)}
        return errorMsg
    
    errorNames = []
    for pName in names.split(delimiter):
        if len(pName) > MAX_NAME_CHARS:
            errorNames.append(pName)

    if errorNames:
        if host_or_participant == 'host_name':
            errorMsg = {'hostNameLenError':'Host name {} has more than {} characters'.format(delimiter.join(errorNames), MAX_NAME_CHARS)}
        elif host_or_participant == 'participant':
            errorMsg = {'participantNameLenError':'Participant(s) with name(s) {} have more than {} characters'.format(delimiter.join(errorNames), MAX_NAME_CHARS)}
        return errorMsg

    return errorMsg

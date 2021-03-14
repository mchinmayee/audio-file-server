from utils import *
from audiobook_repository import *

def add_audiobook_file_data(post_data):

    retValue = validate_audiobook_data(post_data)
    if not retValue:
        retValue = addAudiobook(post_data)

    print('retValue: ', retValue)
    return retValue

def validate_audiobook_data(audiobook_meta_data):
    errorMsg = []
    MAX_NAME_CHARS = 100

    # validate name
    title = audiobook_meta_data['title']
    author = audiobook_meta_data['author']
    narrator = audiobook_meta_data['narrator']
    duration = audiobook_meta_data['duration']
    insert_date = audiobook_meta_data['upload_date']

    if not title or title == '':
        errorMsg.append({'titleError' : 'Empty title'.format(title)})
    elif len(title) > MAX_NAME_CHARS:
        errorMsg.append({'titleError':'Title {} has more than {} characters'.format(title, MAX_NAME_CHARS)})


    if not author or author == '':
        errorMsg.append({'authorError' : 'Empty author name'.format(author)})
    elif len(author) > MAX_NAME_CHARS:
        errorMsg.append({'authorError':'Author name {} has more than {} characters'.format(author, MAX_NAME_CHARS)})

    if not narrator or narrator == '':
        errorMsg.append({'narratorError' : 'Empty narrator name'.format(narrator)})
    elif len(narrator) > MAX_NAME_CHARS:
        errorMsg.append({'narratorError':'Narrator name {} has more than {} characters'.format(narrator, MAX_NAME_CHARS)})

    # validate duration
    if not represents_int(duration):
        errorMsg.append({'durationError': '{} : not an integer'.format(duration)})
    elif int(duration) <= 0:
        errorMsg.append({'durationError': '{} : not a positive number'.format(duration)})

    # validate date

    if not valid_date(insert_date):
        errorMsg.append({'dateError': "Incorrect date format, should be YYYY-MM-DD"})
    elif past_date(insert_date):
        errorMsg.append({'dateError' : "{} : not today's date".format(insert_date)})

    # return json.dumps(errorMsg)
    return errorMsg

#Update
def update_audiobook(id, put_data):
    errorMsg = []
    errorMsg = validate_audiobook_data(put_data)
    if not errorMsg:
        errorMsg = updateAudiobook(id, put_data)
    
    return errorMsg

#Delete
def delete_audiobook_data(id):
    return deleteAudiobook(id)

def audioBook_id(id):
    return getAudiobookById(id)


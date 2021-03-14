import json
from song_repository import *
from utils import *


def add_song_file_data(post_data):

    retValue = validate_song_data(post_data)
    if not retValue:
        retValue = addSong(post_data)

    print('retValue: ', retValue)
    return retValue

def validate_song_data(song_meta_data):
    errorMsg = []
    # validate name
    name = song_meta_data['name']
    duration = song_meta_data['duration']
    insert_date = song_meta_data['uploadDate']

    if not name or name == '':
        errorMsg.append({'nameError' : 'Empty name'.format(name)})
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

def song_id(id):

    return getSongById(id)

def update_song(id, put_data):
    errorMsg = []
    errorMsg = validate_song_data(put_data)
    if not errorMsg:
        errorMsg = updateSong(id, put_data)
    
    return errorMsg

def delete_audio_file_data(id):
    return deleteSong(id)

def getAudiobookById(id):

    return getSongById(id)       

    '''
    audioFileType = del_data['audioFileType']

    if audioFileType == "song":
        deleteSong(name, del_data['metaData'])
    return "value deleted"
    '''
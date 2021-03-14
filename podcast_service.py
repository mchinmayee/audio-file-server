import json
from utils import *
from podcast_repository import *

def add_podcast_data(post_data):
    retValue = validate_podcast_data(post_data)
    if not retValue:
        retValue = addPodcast(post_data)

    print('retValue: ', retValue)
    return retValue

def update_podcast(id, put_data):
    errorMsg = []
    errorMsg = validate_podcast_data(put_data)
    if not errorMsg:
        errorMsg = updatePodcast(id, put_data)
    
    return errorMsg

def delete_podcast_file_data(id):
    return deletePodcast(id)

def validate_podcast_data(pod_meta_data):
    errorMsg = []
    name = pod_meta_data['name']
    duration = pod_meta_data['duration']
    host_name = pod_meta_data['host_name']
    participant_list = pod_meta_data['participant_list']
    insert_date = pod_meta_data['upload_date']

    if not name or name == '':
        errorMsg.append({'nameError':'Empty name'.format(name)})
    
    #check validation for duration
    if not represents_int(duration): #check for integer or not
        errorMsg.append({'durationError':'{}:not an integer'.format(duration)})
    elif int(duration) <= 0: #check for <= 0
        errorMsg.append({'durationError':'{} Enter a valid number'.format(duration)})

    #Validate date
    if not valid_date(insert_date):
        errorMsg.append({'dateError': "Incorrect date format, should be YYYY-MM-DD"})
    elif past_date(insert_date):
        errorMsg.append({'dateError' : "{} : not today's date".format(insert_date)})

    returnMsg = validate_name(participant_list, 'participant')
    if bool(returnMsg):
        errorMsg.append(returnMsg)

    returnMsg = validate_name(host_name, 'host_name')
    if bool(returnMsg):
        errorMsg.append(returnMsg)
        
    return errorMsg

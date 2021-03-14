from flask import Flask, request
import json
from song_service import *
from podcast_service import *
from audiobook_service import *


app = Flask(__name__)

@app.route('/songs')

def getAllsongs():
    # return json.dumps(getSongs())
    return {'results':getSongs()}, 200

@app.route('/audiobook')
def getAllaudioBooks():
    return {'results':getaudioBooks()},200

@app.route('/podcast')
def getAllPodcast():
    return json.dumps(getPodcasts())

@app.route('/song/<songId>')

def getSongId(songId):
    # return json.dumps(song_id(songId))
    return {'results':song_id(songId)}, 200

@app.route('/book/<audiobookId>')

def getaudiobookId(audiobookId):
    # return json.dumps(song_id(songId))
    return {'results':audioBook_id(audiobookId)}, 200


@app.route('/audio',methods=['POST'])
def addAudioFileData():
    post_data = request.json

    audioFileType = post_data['audioFileType']

    retValue = {}

    if audioFileType == 'song':
        retValue = add_song_file_data(post_data['metaData'])
    
    elif audioFileType == 'audiobook':
        retValue = add_audiobook_file_data(post_data['metaData'])
    
    elif audioFileType == 'podcast':
        retValue = add_podcast_data(post_data['metaData'])

    else:
        retValue = {'audioFileFormatError':'invalid audio type - {}'.format(audioFileType)}
 
    if 'id' in retValue[0].keys():
        return json.dumps(retValue), 201
    else:
        return json.dumps(retValue), 400

@app.route('/song/<id>',methods=['PUT', 'DELETE'])
def updateSongData(id):
    if request.method == 'PUT':
        put_data = request.json
        retValue = update_song(id, put_data)
        print ('retValue: ', retValue)
        if 'id' in retValue[0].keys():
            return json.dumps(retValue), 201
        else:
            return json.dumps(retValue), 400
    elif request.method == 'DELETE':
        deleteValue = json.dumps(delete_audio_file_data(id))   
        print('deletValue are:{}'.format(id))
        return 'OK', 200

@app.route('/podcast/<id>',methods=['PUT', 'DELETE'])
def updatePodcastData(id):
    if request.method == 'PUT':
        put_data = request.json
        retValue = update_podcast(id, put_data)
        print ('retValue: ', retValue)
        if 'id' in retValue[0].keys():
            return json.dumps(retValue), 201
        else:
            return json.dumps(retValue), 400
    elif request.method == 'DELETE':
        retValue = delete_podcast_file_data(id) 
        print('deletValue is:{}'.format(id))
        if retValue == 'OK':
            return 'Record deleted successfully', 200
        else:
            return 'Could not delete record with ID = {}'.format(id), 400


#Update

@app.route('/audiobook/<id>',methods=['PUT', 'DELETE'])
def updateAudiobook_data(id):
    if request.method == 'PUT':
        put_data = request.json
        retValue = update_audiobook(id, put_data)
        print ('retValue: ', retValue)
        if 'id' in retValue[0].keys():
            return json.dumps(retValue), 201
        else:
            return json.dumps(retValue), 400
    elif request.method == 'DELETE':
        deleteValue = json.dumps(delete_audiobook_data(id))   
        print('deletValue are:{}'.format(id))
        return 'OK', 200

#Update podcast
#@app.route('/podcast/<id>',methods=['PUT', 'DELETE'])

if __name__ == "__main__":
    app.run( debug=True)


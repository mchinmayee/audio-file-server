import sqlite3
from utils import dict_factory

dbfile = '../data/audio.db'

def addAudiobook(metadata):

    audiobook = []
    try:
        con = sqlite3.connect(dbfile, check_same_thread=False)
        sqlString = "insert into audiobook (title, author, narrator, duration, upload_date) values (?,?,?,?,?)"
        latestRecSql = "select * from audiobook where id=?;"

        cur = con.cursor()

        title = metadata['title']
        author = metadata['author']
        narrator = metadata['narrator']
        duration = metadata['duration']
        insert_date = metadata['upload_date']

        insertExec = cur.execute(sqlString,(title, author, narrator, duration, insert_date))
        print ('last row id :', insertExec.lastrowid)
        con.commit()

        latestEntry = cur.execute(latestRecSql, (insertExec.lastrowid, ))
        audiobook = dict_factory(latestEntry, latestEntry.fetchall())
        cur.close

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)

    finally:
        if con:
            con.close()
    
    return audiobook

    #update
def updateAudiobook(id, metadata):
    con = sqlite3.connect(dbfile, check_same_thread=False)
    sqlString = "update audiobook set title=?, duration=?,author=?, narrator=?, upload_date=? where id=?"
    getByIdSqlString = "select * from audiobook where id=?"
    cur = con.cursor()

    title = metadata['title']
    author = metadata['author']
    narrator = metadata['narrator']
    duration = metadata['duration']
    insert_date = metadata['upload_date']

    sqlCursor = cur.execute(sqlString,(title, author, narrator, duration, insert_date, id))
    con.commit()

    updatedEntry = cur.execute(getByIdSqlString, (id, ))
    audiobook = dict_factory(updatedEntry, updatedEntry.fetchall())
    con.close()
    
    return audiobook

#get all AudioBooks

def getaudioBooks():
    con = sqlite3.connect(dbfile, check_same_thread=False)
    cur = con.cursor()
    sqlString = "select * from audiobook;"
    sqlCursor = cur.execute(sqlString)
    print('sqlCursor:{}'.format(sqlCursor))
    audiobookList = sqlCursor.fetchall()
    audiobooks = dict_factory(sqlCursor, audiobookList)
    con.close()

    return audiobooks

# get AudioBooks by Id

def getAudiobookById(audioBookId):
    con = sqlite3.connect(dbfile,check_same_thread=False)
    sqlString = "select * from audiobook where id=?;"
    cur = con.cursor()
    sqlCursor = cur.execute(sqlString,(audioBookId,))
    audiobooklist = sqlCursor.fetchall()
    audiobook = dict_factory(sqlCursor, audiobooklist)
    con.close()
    return audiobook

    #delete
def deleteAudiobook(id):
    returnMsg = 'record successfully deleted'
    try:
        con = sqlite3.connect(dbfile,check_same_thread=False)
        sqlString = "delete from audiobook where id = ?"
        cur = con.cursor()
        cur.execute(sqlString, (id,))
        con.commit()
    
    except:
        returnMsg = {'deleteError':'Could not delete song with id = {}'.format(id)}
    
    finally:
        con.close()
    
    return returnMsg


import sqlite3
from utils import dict_factory

dbfile = '../data/audio.db'

def addSong(metadata):

    song = []
    try:
        con = sqlite3.connect(dbfile, check_same_thread=False)
        sqlString = "insert into song (name, duration, upload_date) values (?,?,?)"
        latestRecSql = "select * from song where id=?;"

        cur = con.cursor()
        name = metadata['name']
        duration = metadata['duration'] 
        uploadDate = metadata['uploadDate']
        songExec = cur.execute(sqlString,(name,duration,uploadDate))
        print ('last row id :', songExec.lastrowid)
        # print ('songExec: {}, {}'.format(songExec, type(songExec)))
        con.commit()

        latestEntry = cur.execute(latestRecSql, (songExec.lastrowid, ))
        song = dict_factory(latestEntry, latestEntry.fetchall())
        cur.close

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)

    finally:
        if con:
            con.close()
    
    return song

def getSongs():
    con = sqlite3.connect(dbfile, check_same_thread=False)
    cur = con.cursor()
    sqlString = "select * from song;"
    sqlCursor = cur.execute(sqlString)
    print('sqlCursor:{}'.format(sqlCursor))
    songlist = sqlCursor.fetchall()
    songs = dict_factory(sqlCursor, songlist)
    con.close()

    return songs

def getSongById(songId):
    con = sqlite3.connect(dbfile,check_same_thread=False)
    sqlString = "select * from song where id=?;"
    cur = con.cursor()
    sqlCursor = cur.execute(sqlString,(songId,))
    songlist = sqlCursor.fetchall()
    song = dict_factory(sqlCursor, songlist)
    con.close()
    return song

def updateSong(id, metadata):
    con = sqlite3.connect(dbfile, check_same_thread=False)
    sqlString = "update song set name=?, duration=?, upload_date=? where id=?"
    getByIdSqlString = "select * from song where id=?;"
    cur = con.cursor()
    name = metadata['name']
    duration = metadata['duration'] 
    uploadDate = metadata['uploadDate']
    sqlCursor = cur.execute(sqlString,(name,duration,uploadDate, id))
    con.commit()

    updatedEntry = cur.execute(getByIdSqlString, (id, ))
    song = dict_factory(updatedEntry, updatedEntry.fetchall())
    con.close()
    
    # print(song)
    return song

def deleteSong(id):
    returnMsg = 'OK'
    try:
        con = sqlite3.connect(dbfile,check_same_thread=False)
        sqlString = "delete from song where id = ?"
        cur = con.cursor()
        cur.execute(sqlString, (id,))
        con.commit()
    
    except:
        returnMsg = {'deleteError':'Could not delete song with id = {}'.format(id)}
    
    finally:
        con.close()
    
    return returnMsg
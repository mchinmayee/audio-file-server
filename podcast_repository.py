import sqlite3
from utils import dict_factory

dbfile = '../data/audio.db'

def addPodcast(metadata):

    podcast = []
    try:
        con = sqlite3.connect(dbfile, check_same_thread=False)
        sqlString = "insert into podcast (name, duration, host_name, participant_list, upload_date) values (?,?,?,?,?)"
        latestRecSql = "select * from podcast where id=?;"

        cur = con.cursor()

        name = metadata['name']
        duration = metadata['duration']
        host_name = metadata['host_name']
        participant_list = metadata['participant_list']
        insert_date = metadata['upload_date']

        podcastExec = cur.execute(sqlString,(name,duration,host_name, participant_list, insert_date))
        print ('last row id :', podcastExec.lastrowid)
        # print ('songExec: {}, {}'.format(songExec, type(songExec)))
        con.commit()

        latestEntry = cur.execute(latestRecSql, (podcastExec.lastrowid, ))
        podcast = dict_factory(latestEntry, latestEntry.fetchall())
        cur.close

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)

    finally:
        if con:
            con.close()
    
    return podcast

def updatePodcast(id, metadata):
    con = sqlite3.connect(dbfile, check_same_thread=False)
    sqlString = "update podcast set name=?, duration=?, host_name=?, participant_list=?, upload_date=? where id=?"

    getByIdSqlString = "select * from podcast where id=?;"
    cur = con.cursor()
    
    name = metadata['name']
    duration = metadata['duration']
    host_name = metadata['host_name']
    participant_list = metadata['participant_list']
    insert_date = metadata['upload_date']

    sqlCursor = cur.execute(sqlString,(name,duration, host_name, participant_list, insert_date, id))
    con.commit()

    updatedEntry = cur.execute(getByIdSqlString, (id, ))
    podcast = dict_factory(updatedEntry, updatedEntry.fetchall())
    con.close()
    
    return podcast

def deletePodcast(id):
    returnMsg = 'OK'
    try:
        con = sqlite3.connect(dbfile,check_same_thread=False)
        sqlString = "delete from podcast where id = ?"
        cur = con.cursor()
        cur.execute(sqlString, (id,))
        con.commit()
        cur.close()
    
    except:
        returnMsg = {'deleteError':'Could not delete podcast with id = {}'.format(id)}
    
    finally:
        con.close()
    
    return returnMsg
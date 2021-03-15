Flask / FastAPI Web API that simulates the behavior of an audio file server while using a SQLite database

API Documentation

1. Create Song json example

POST /audio

```json
{
  "audioFileType": "song",
  "metaData": {
    "name": "Jjhankar",
    "duration": 210,
    "upload_date": "2021-03-14"
  }
}
```

2. update json example where the record id is passed as a path variable:

PUT /song/{id}

```json
{
  "name": "war songs one more",
  "duration": 450,
  "uploadDate": "2021-03-14"
}
```

4. Delete Song example

DELETE /song/{id}

5. Create Podcast json example

POST /audio

```json
{
  "audioFileType": "podcast",
  "metaData": {
    "name": "Jjhankar",
    "duration": 210,
    "host_name": "Bhavan Somya",
    "participant_list": "Rajendra kumar, Ghanshaym Das Gujarl, Radha Seth",
    "upload_date": "2021-03-14"
  }
}
```

6. Update podcast example:

PUT /podcast/{id}

```json
{
  "name": "Jjhankar beats",
  "duration": 210,
  "host_name": "Bhavan Somya",
  "participant_list": "Rajendra kumar, Ghanshaym Das Gujarl, Radha Seth",
  "upload_date": "2021-03-14"
}
```

7. Delete podcast example:

DELETE /podcast/{id}

8. Create Audio book json example

POST /audio

```json
{
  "audioFileType": "audiobook",
  "metaData": {
    "title": "The Reverence",
    "duration": 3000,
    "author": "Mablahaguru Sambant",
    "narrator": "Derek O' Gul",
    "upload_date": "2021-03-14"
  }
}
```

9. update Audio book example:

PUT /audiobook/{id}

```json
{
  "title": "The Reverence",
  "duration": 3000,
  "author": "Mablahaguru Sambant",
  "narrator": "Derek O' Gulan",
  "upload_date": "2021-03-14"
}
```

10. Delete Audio book example:

DELETE /audiobook/{id}

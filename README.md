# Forum API
This is a simple forum built using python and flask. It relies on API calls and has no front end (for now).

The sample database is populated with televangelists discussing their opinions on modern programming languages.


---
## 1) GET ALL FORUMS    
**API_CALL:** 
```
curl http://127.0.0.1:5000/forums  
```
**RESPONSE:** 
```  
[
  {
    "creator": "marek.sautter", 
    "id": 1, 
    "title": "Python"
  }, 
  {
    "creator": "jesus.christ", 
    "id": 2, 
    "title": "Java"
  }, 
  {
    "creator": "ray.comfort", 
    "id": 3, 
    "title": "C++"
  }
]
```
**SUC_CODE:**   200 OK  
**ERR_CODE:**   N/A  
**REQ_AUTH:**   FALSE  

## 2) POST A NEW FORUM
**API_CALL:**   
```
curl -d '{"name":"Python"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/forums 
``` 
**RESPONSE:**   N/A  
**SUC_CODE:**   201 CREATED  
**ERR_CODE:**   409 CONFLICT   
**REQ_AUTH:**   TRUE  


## 3) GET THREADS FROM FORUM
**API_CALL:**   
```
curl http://127.0.0.1:5000/forums/1
```  
**RESPONSE:**
```   
[
  {
    "creator": "martin.luther", 
    "id": 1, 
    "timestamp": "2018-09-14 15:00:47.128324", 
    "title": "Python is the future of programming!"
  }, 
  {
    "creator": "billy.graham", 
    "id": 2, 
    "timestamp": "2018-09-14 15:03:17.245418", 
    "title": "How do you avoid creating 'spaghetti-code'?"
  }
]
```
**SUC_CODE:**   200 OK  
**ERR_CODE:**   404 NOT FOUND  
**REQ_AUTH:**   FALSE  

## 4) POST THREAD TO FORUM
**API_CALL:**   
```
curl -d '{"title": "Python is overated", "text":"Change my mind."}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/forums/1
```
**RESPONSE:**   N/A  
**SUC_CODE:**   201 CREATED  
**ERR_CODE:**   404 NOT FOUND  
**REQ_AUTH:**   TRUE  

## 5) GET POSTS FROM THREAD
**API_CALL:**   
```
curl http://127.0.0.1:5000/forums/1/1  
```
**RESPONSE:**   
```
[
  {
    "author": "martin.luther", 
    "text": "I love Python so much I just wanted to make my own thread about it!", 
    "timestamp": "2018-09-14 15:00:47.128324"
  }, 
  {
    "author": "mary.magdalene", 
    "text": "Python Smython, It's all about x86 Assembly!", 
    "timestamp": "2018-09-14 15:17:28.082059"
  }, 
  {
    "author": "marek.sautter", 
    "text": "Ha, try coding the next facebook on assembly code", 
    "timestamp": "2018-09-14 15:31:11.063779"
  }
]
```
**SUC_CODE:**   200 OK  
**ERR_CODE:**   404 NOT FOUND  
**REQ_AUTH:**   FALSE  

## 6) POST POST TO THREAD
**API_CALL:**   
```
curl -d '{"text": "I actually love Python and you should too!"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/forums/1/1
```
**RESPONSE:**   N/A  
**SUC_CODE:**   201 CREATED  
**ERR_CODE:**   404 NOT FOUND  
**REQ_AUTH:**   TRUE  

## 7) POST USER TO USERS
**API_CALL:**   
```
curl -d '{"username" : "mark.ruffalo", "password" : "GREEN_BIG_GUY_73"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/users
```
**RESPONSE:**   N/A  
**SUC_CODE:**   201 CREATED  
**ERR_CODE:**   409 CONFLICT  
**REQ_AUTH:**   FALSE  

## 8) PUT USER TO USERS
**API_CALL:**
```
curl -d '{"username" : "mark.ruffalo", "password" : "GR33N_BIG_GUY_73"}' -H "Content-Type: application/json" -X PUT http://127.0.0.1:5000/users
```
**RESPONSE:**   N/A  
**SUC_CODE:**   201 CREATED  
**ERR_CODE:**   409 NOT FOUND / 409 CONFLICT  
**REQ_AUTH:**   TRUE

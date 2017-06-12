### Yolo model rest service 

##### dependencies
```
pip install Django==1.11 djangorestframework==3.62
```

##### install yolomodel 
```
cd yolo
git clone https://github.com/johnsonice/yolomodel.git
```
please follow yolomodel repo and make sure environment is properly set up 

#### run server 
```
cd [RESTYolo root]
python python manage.py runserver 0.0.0.0:8080
```

#### sample request 
```
import requests
import os
import ast

url = "http://0.0.0.0:8080/yolo/api/upload/"
upfile = "preview.png"
put_url = os.path.join(url,upfile)
files = {'file': open(upfile,'rb')}
resp = requests.post(put_url,data=files['file']) ## upload file and return coordinates

#### convert byte response to dictionray 
result = ast.literal_eval(resp.content.decode())
print(result)
```

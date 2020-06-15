# STC-App-Backend
Backend routes and other stuff regarding the STC App

-``` pip install flask```
-``` pip install flask-pymongo ```
-``` pip install pymongo[srv]``` ~ for global cluster in Atlas.

## Routes (only designed by custom backend- Flask) 
- posts
- resources


### Route usage:
#### resources 
  /resources/'domain-name'/upload : to upload the content (POST Request).(domains are webdev,appdev,ml,..uniformity to be kept)
  - 'domain' (automatically generated from the route)
  - 'title' (title of the content)
  - 'date time' (upload date and time automatically generated)
  - 'link1'/'link2'/'link3' : links to particular documents.  
  
  /resources/'domain-name' : to display the content of the domain.(GET Request)
  
  #### posts
   /posts/upload method POST:
  - 'date'(datetime automatically generated)
  - 'photos' upload single photo. stored in db
  
  /posts/'filename':  method: GET to retrieve single post by its filename
  
  - eg: /posts/image.JPG
  
  

    

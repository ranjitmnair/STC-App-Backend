# STC-App-Backend
Backend routes and other stuff regarding the STC App
## Routes 
- sign up
- sign in 
- posts
- resources
- notifications


### Route usage:
#### resources
  /resources/'<domain-name>'/upload : to upload the content.
  - 'domain' (automatically generated from the route)
  - 'title' (title of the content)
  - 'date time' (upload date and time automatically generated)
  - 'link1'/'link2'/'link3' : links to particular documents.  
  
  /resources/<domain-name> : to display the content of the domain.
  
  #### notifications
  call: /notifications 
  method POST:
  - 'title' (title of the notification)
  - 'date'(datetime automatically generated)
  - 'id'(id of notif can be added)
  - 'body'(body of the notif)

    

# Blog
* Blog is a simple python application that allows a user to register,sign in ,post a  blog by category,and view posted blogs.
## By **[Dickson Kariuki](https://github.com/dicksonkariuki)**

## Description
* Blog is a python application that allows a user to register,login,create a blog based on category,post a blog, view posted blog, and comment on the posted blog.
* To be able to post a blog a user must be registered on the website.

## Behaviors of the application 


|   Behavior        | Input        | Output |
| ------------- |:-------------:| -----:|
| Register user      |email,username,password | Redirect to login page |
| Login    |email,password    | Redirect to the homepage |
| Create blog | blog category and content   |  Created blogs displayed in descending order|
|  Comment             |    A comment message          | The inputed comment message    |
|Delete message         |   Press the delete button      |       |An empty comments section
## Setup Instructions
* You can fork or clone the repository to your machine.
* Visit the requirements file and install all the requirements
* Activate the start.sh file using:chmod a+x start.sh command
* Run your application locally using ./start.sh

## Known bugs
* Currently when unregistered user tries to post a blog gets an error.

## Technologies used
* Python3.6
* Flask 
* Bootstrap
* Html
* CSS
## Contact Details
* You can Contact me via dicksonkariuki4@gmail.com for advice on how to improve the application.

## Licence
* Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, or distribute the software.
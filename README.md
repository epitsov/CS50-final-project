# CS50-final-project
#### For my final project I have used python in order to create a graphical interface application that sends the same E- mail to all customers from a database.
#### You need to give your e-mail without the greetings part (Dear Mr or Mrs), because the program automatically adds this to your text depending on the gender of the person.
#### For example if the person is male it will start as: Dear Mr. Doe and if the person is female Dear Mrs. Doe.
#### For my application i used the following libraries:tkinter for the graphical interface, ezgmail for sending the e-mails with my python application and sqlite3 to create and get the inforamtion from the database.
#### For my project I primarily used the following sources: 
#### https://automatetheboringstuff.com/2e/chapter18/
#### https://www.youtube.com/watch?v=YXPyB4XeYLA&t=2050s&ab_channel=freeCodeCamp.org,
#### https://www.youtube.com/watch?v=YXPyB4XeYLA&t=2050s&ab_channel=freeCodeCamp.org
####
#### The reason that i did this project was that I needed to start a E-mail campain to promote the new web-site of my company and knew that there is a faster and easier way than sending the 
#### same E-mail to all of your customers. Doing this project i encounter the following problems:
####
#### The first problem that i encounter with my project was how to connect and send e-mails from my python script, luckly i found a great chapter about this in the book Automate the boring stuff.
#### In order to do that we need to use ezgmail library and enable access of third party software to our g-mail account. When we do this we need to download a JSON file called credentials
#### and add it to the library that our python file is located in. When this is done we need to run a function that we take us to our browser and ask us to enter gmail username and password,
#### when we do this the function will create a new JSON file called token this file serves as a password to our g-mail and allows us to access our e-mail with the application, that's why
#### we need to be careful with this file and don't share it with anyone. After we have been connected to our gmail account we only need to take the e-mails  adresses of our customers and send the E-mails.
####
#### The second problem that i encounter was how to make this process as userfriend as possible and for that i decided to use a graphical interface that allows us to write our 'Subject' and 'e-mail text'
#### I knew that there a lot of libraries that could help me but i decided to use tkinter because i found a lot of information about it. The only problem that i encounter with it was how
#### to take the whole text from a text box but there was information about this online.
####
#### The last problem that i need to solve was that i wanted to adress all my customers with their last names and i could not use the same greeting for my female and male guests. To solve this issue
#### i added the gender to all my customers in the database and if i did not know what gender they were i simply wrote 'na'. After adding the new information to my database i was able to access the 
#### customer gender and the decide which greeting should i use based on their gender.
####
#### I am happy with my final project not only because I did it and with it i finished my CS50 course, but also because I will be able to use it the future to make my work easier.

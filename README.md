# UAlbertaDate

Thanks for downloading UAlbertaDate!
This is our entry for HackED Beta 2022, and also our attempt to play cupid on campus!

Requirements:
    - python
    - django version 4.1.3
    - pillow

How to install:
    
    1. Download and install all required packages.
    
    2. Open the directory UAlbertaDate in terminal.
    
    3. Run the following command from your python interpreter in terminal:
        
        {python interpreter} manage.py makemigrations
        {python interpreter} manage.py migrate
        {python interpreter} manage.py runserver 127.0.0.1:8000
        
        Note that python is run differently depending on your machine and system path.
        Because of this, "manage.py" may have to be replaced with simply "manage".

    4. Open the development server in your browser. This will be at http://127.0.0.1:8000/index/ .
       This runs the server with your machine as the host, using the same port that we did during development.
    
    5. Have fun! Feel free to make any changes to the database.
       Hint: To experience all of the features, make a few accounts and create some matches.
       Once the server is fully operational, I doubt you'll have much trouble getting them, though ;)

    * If you'd like to view the admin panel to see more of the database, try registering yourself as a superuser using the command
      manage.py createsuperuser, then following the instructions. The admin panel can be found at http://127.0.0.1:8000/admin/ .

Features:
    - Registration only open to ualberta email addresses. We hope to enforce this more strongly in the future via email confirmation.
    - Academic-based user profiles with personal information, photos, and a biography.
    - Database open to all sorts of user input, including images.
    - Fully-functional chat rooms between users who have "matched" with each other.
    - Input-based interactive matching view.

Our Thoughts:
Working on UAlbertaDate was a challenging yet stimulating experience for our team. One of our members dropped out due to extraneous circumstances,
but our team took this hit in stride. With minimal experience using Django, and almost zero familiarity with HTML and CSS, our team was able
to create what we think is a really good alpha version of a web app we hope to develop even further in the future :)
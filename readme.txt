Welcome to Signature comparison app!

The application is designed for working with handwritten signatures
to analyse match between them, store them and potentially use as authentication (possibly authorisation as well)

The application currently uses demos to illustrate the functionality of a potential product:
JS demo scripts in the static folder :
    demo-script -- for showing the specific functionality
    drawer -- for running the algorythm for interpreting the signature
                as a set of points  (storing the order, speed of the pen as well)

    The information about the user functionality I decided to store in each demo folder<
    so you can test the application as a whole via these prepared pages and scripts


python scripts run the back-end:
    server -- the main program which accepts and responds the requests,
                runs the libraries and services to work with data

    abstractions -- organize data for working with the DB

    authorization -- includes working code for authorization

    lib -- includes analytical algorythm(s) for analysing the signatures for match

    mongo_rom -- library designed to interact with the special entities in DB

    posts_service? sign_service -- library designed for interacting with the DB via special data entities


sensitive settings.py and migration.py are to be secured
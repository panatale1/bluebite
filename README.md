# Blue Bite
This project uses Python 2.7, PostgreSQL, and Django 1.11.

On Ubuntu:
Run `sudo ./initial_setup.sh`
This will install Python, pip, and virtualenv, if needed, as well as installing PostgreSQL and initializing the database.

As a local user, run `./local_setup.sh`
This should make the virtualenv `bluebite`, activate it, and install the requirements.
If not, run `source $(which virtualenvwrapper)` then `mkvirtualenv bluebite`, followed by `pip install -r requirements.txt`

If not running Ubuntu:
As root, install Python 2.7, pip, and PostgreSQL
Run `su -c 'psql -a -f django.psql' postgres` to set up the database
If that throws an error, run `psql -a -f django.psql` as the postgres user
Then run `pip install --upgrade virtualenv virtualenvwrapper`
At this point, you may need to open up a new shell window in order to set up the virtualenv.
Run `mkvirtualenv bluebite`, then `pip install -r requirements.txt`

Go to the middle bluebite folder and run:
`./manage.py migrate`
Run the application by using `./manage.py runserver`

The endpoints can be accessed at:
`http://localhost:8000/api/vendors/`
`http://localhost:8000/api/tags/`

The vendors endpoint can take GET or POST requests through the browsable API or through curl or Python's `requests` library.
The vendors endpoint can be filtered to show vendors with specific tags or specific metadata points as follows:
`http://localhost:8000/api/vendors/?tags__tag_id= *[tag_id goes here]* ` or
`http://localhost:8000/api/vendors/?tags__metadata__key= *[key name goes here]* &tags__metadata__value= *[value name goes here]* `

The tags endpoint is only used for GET requests, and can be filtered on tag ids or metadata values, similar to above:
`http://localhost:8000/api/tags/?tag_id=*[tag_id]*` or
`http://localhost:8000/api/tags/?metadata__key=*[key name]&metadata__value=*[value name]*`

In both cases, you can combine filtering on tag_id and metadata information using an ampersand `&` between the queries

THINGS TO DO:
Had I more time to work on this, I would have made it slightly more robust, showing only tags specific to a vendor to that vendor.
I also would have liked to add unit tests.

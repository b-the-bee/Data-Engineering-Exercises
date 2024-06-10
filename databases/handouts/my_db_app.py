import pymysql
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
host_name = os.environ.get("mysql_host")
database_name = os.environ.get("mysql_db")
user_name = os.environ.get("mysql_user")
user_password = os.environ.get("mysql_pass")


try:
    print('Opening connection...')
    # TODO Establish a database connection
    # Hint: use "with ..."



        # This bit won't compile till the "with" is done...
        print('Opening cursor...')
        # TODO open a cursor



        print('Inserting new record...')
        # TODO Add code here to insert a new record



        print('Selecting all records...')
        # TODO Add code here to select all the records



        print('Displaying all records...')
        # TODO Add code here to print out all the records



        print('Closing cursor...')
        # TODO close the cursor



    # The connection will automatically close here
except Exception as ex:
    print('Failed to:', ex)

# Leave this line here!
print('All done!')

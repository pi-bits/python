import requests,ast,logging
import json
print ("hello world")
# This is a comment.
if 5>2 :
    print(' 5 is greater than 2')

# logging.basicConfig(format='%(levelname)-8s %(message)s',level=logging.INFO)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logger=logging.getLogger(__name__)

def hello_world(): 
    response = requests.get("http://api.open-notify.org/iss-now.json")
    print(response.status_code)
    data = response.json()
    print(data["timestamp"])
    print(data["message"])
    print(data["iss_position"]["latitude"])
    print(data["iss_position"]["longitude"])
    logger.info(response.content)
    return response.json(); 

    
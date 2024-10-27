from src.exception import CustomException
from src.logger import logging
import sys

def test_exception():
    try:
        logging.info("Ki Yaha par Division by 0 error aegi")
        a=1/0
    except Exception as e:
        raise CustomException(e,sys)
    

if __name__== "__main__":
    try:
        test_exception()
    except Exception as e:
        print(e)
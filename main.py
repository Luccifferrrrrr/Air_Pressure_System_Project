from sensor.exception import CustomException
from sensor.logger import logging
import sys
from sensor.utils import dump_csv_file_to_mongodb_collection
 #   def test_exception():
 #       try:
 #           logging.info("Ki Yaha par Division by 0 error aegi")
 #           a=1/0
 #      except Exception as e:
 #           raise CustomException(e,sys)
        

if __name__== "__main__":
    file_path= r"C:\Users\aman1\ML_Projects\Air_Pressure_System_Project\aps_failure_training_set1.csv"
    database_name = "APS_DB"
    collection_name = "sensor"
    dump_csv_file_to_mongodb_collection(file_path,database_name,collection_name )

    

    
    
    #try:
     #   test_exception()
    #except Exception as e:
     #   print(e)
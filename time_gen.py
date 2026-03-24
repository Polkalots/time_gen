import argparse
import pytz
import time
import datetime
import sys

def main(timestamp):
    conv_time = get_timestamp(timestamp)
    print(conv_time)

def get_timestamp(timestamp):
    # First try conversion from epoch time to UTC
   try:
    utc_struct = time.gmtime(int(timestamp))
    utc = time.asctime(utc_struct)
    return utc
   except TypeError:
      sys.exit('Type Error: script needs an integer. Fix the code.')







if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Creates a timeline from inputted events")
    parser.add_argument("-t", "--timestamp", required=True, help='Accepts timestamps as input in the following formats: ___')
    args = parser.parse_args()
    main(args.timestamp)
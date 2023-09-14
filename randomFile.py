import json
import os
import csv
import sys
import subprocess

"""
Python Module OS
 -File system operations. Used with environment variables

Python Module sys
Runtime specific features. Data that is needed at the time the files is running

Python Module subprcess

python3 addTags.py <InstanceId> <tagKey> <tagValue>
use pythone to run cli commands
"""          

#InstanceId": "i-0831ba29a031889ff"

def addTagsV2(instance_id,tag_key,tag_value):
    #Using subprocess to run aws cli command
    try:
        aws_command = f" aws ec2 create-tags --resources {instance_id} --tags Key={tag_key},Value={tag_key}"
        subprocess.run(aws_command, shell=True, check=True)
        print("Subprocess ran successfully")
    except subprocess.CalledProcessError as e:
        print(f"Error Message:{str(e)}")

def main():
    #checking for correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: python3 addTag.py <InstanceId <Tag> <tagValue>") 
        sys.exit(1)      
    instance_id = sys.argv[1]
    tag_key = sys.argv[2]
    tag_value = sys.argv[3]

# calling add tags function
    addTags(instance_id,tag_key,tag_value)

main()
import boto.ec2
import os
region = 'ap-southeast-1'
aws_access_key_id=os.environ['AWS_ACCESS_KEY']
aws_secret_access_key=os.environ['AWS_SECRET_KEY']

instances = ['i-0542e993b3458146d']
conn = boto.ec2.connect_to_region(region, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
conn.stop_instances(instances)
#conn.start_instances(instances)
#print(dir(conn))


import boto3
import json
import botocore.exceptions
import Classic_Single_Column as template1
import Classic_Double_Column as template2
import Professional_Single_Column as template3

aws_access_key_id = 'AKIARYFQEG' + 'PBLHZZVZXJ'
aws_secret_access_key = 'h8nLYkBEHO' + '8juG9P2FipSEwi1' + '2TYP1Y5Nf80Jeag'

s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

def createbucket(username, s3):
    bucket_name = username
    
    try:
        response = s3.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'}
        )
        print(f"Storage bucket for user {username} created successfully.")
        
        public_access_block_config = {
            'BlockPublicAcls': False,
            'IgnorePublicAcls': False,
            'BlockPublicPolicy': False,
            'RestrictPublicBuckets': False
        }
        
        s3.put_public_access_block(
            Bucket=bucket_name,
            PublicAccessBlockConfiguration=public_access_block_config
        )
        print(f"Block Public Access settings disabled for bucket {bucket_name}.")
        
        bucket_policy = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Sid": "AddPerm",
                    "Effect": "Allow",
                    "Principal": "*",
                    "Action": "s3:GetObject",
                    "Resource": f"arn:aws:s3:::{bucket_name}/*"
                }
            ]
        }

        bucket_policy_str = json.dumps(bucket_policy)
        
        s3.put_bucket_policy(Bucket=bucket_name, Policy=bucket_policy_str)
        print(f"Bucket policy applied to bucket {bucket_name}.")
        
        return True
        
    except botocore.exceptions.ClientError as e:
        error_code = e.response['Error']['Code']
        if error_code == 'BucketAlreadyExists':
            return(f"The username '{bucket_name}' is unavailable. Please choose a different username.")
        elif error_code == 'BucketAlreadyOwnedByYou' :
            return(f"The username '{bucket_name}' is already taken. Try again with another username")
        elif error_code == 'InvalidBucketName' :
            return(f"The username '{bucket_name}' is not valid. Try again with another username")
        else:
            return(f"An unknown error occured, {e}")
        
    
def deletebucket(username, s3):
    try :
        objects = s3.list_objects_v2(Bucket=username).get('Contents', [])
        for obj in objects:
            s3.delete_object(Bucket=username, Key=obj['Key'])
        s3.delete_bucket(Bucket=username)
        print(f"Storage bucket for user {username} deleted succesfully.")
        return True
    except Exception as e :
        print(f"ERROR FROM deletebucket function : {e}")
        return False
    
    
def uploaddata(information, username, s3):

    # information is JSON data
    try:
        if isinstance(information, str):
            information = json.loads(information)
        data = json.dumps(information, indent=2)
        s3.put_object(Body=data, Bucket=username, Key=f"{username}.json")

        return True
    except Exception as e:
        return f"Error uploading file: {e}"
    
def uploadtemplate1(information, username, s3):
    try:
        information = template1.changedetails(information)
        print("--------------------------- TEMPLATE 1 ---------------------------")
        print(information)
        s3.put_object(Body=information, Bucket=username, Key=f"{username}_classic_single_column.tex")
        return True
    except Exception as e:
        print(e)

def uploadtemplate2(information, username, s3):
    try:
        information = template2.changedetails(information)
        print("--------------------------- TEMPLATE 2 ---------------------------")
        print(information)
        s3.put_object(Body=information, Bucket=username, Key=f"{username}_classic_double_column.tex")
        return True
    except Exception as e:
        print(e)

def uploadtemplate3(information, username, s3):
    try:
        information = template3.changedetails(information)
        print("--------------------------- TEMPLATE 3 ---------------------------")
        print(information)
        s3.put_object(Body=information, Bucket=username, Key=f"{username}_professional_single_column.tex")
        return True
    except Exception as e:
        print(e)


def readdata(username, s3):
    try:
        response = s3.get_object(Bucket=username, Key=f'{username}.json')
        data = response['Body'].read().decode('utf-8')
        json_data = json.loads(data)
        return json_data
    except Exception as e:
        return f"Error reading file: {e}"


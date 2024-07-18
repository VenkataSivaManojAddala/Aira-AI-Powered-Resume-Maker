import boto3
import hmac
import hashlib
import base64
import manage_buckets as buckets

client = boto3.client(
    'cognito-idp',
    region_name='ap-southeast-2',
    aws_access_key_id='AKIARY' + 'FQEGPBJWR25OVL',
    aws_secret_access_key='Yu6zEsLHJW' + 'AWVfPNE4l4q8g+' + 'Kfz2cAsOpA7qUiAx'
)

client_id = '2sus8eu3p7e2m' + 'kakvh5map3s2a'
client_secret = '9mgc4njlr2u' + 'aut82q649d53sprd2' + 'ar21hq4krfgiskha7r1l9vp'

def get_secret_hash(username, client_id, client_secret):
    message = username + client_id
    dig = hmac.new(client_secret.encode('utf-8'), msg=message.encode('utf-8'), digestmod=hashlib.sha256).digest()
    return base64.b64encode(dig).decode()

def signup(username, email, password):
    if check_user_existence(username):
        return (f"User {username} already exists. Try logging in instead.")
    else:
        secret_hash = get_secret_hash(username, client_id, client_secret)

        try:
            response = client.sign_up(
                ClientId= client_id,
                SecretHash= secret_hash,
                Username= username,
                Password= password,
                UserAttributes=[
                    {
                        'Name': 'email',
                        'Value': email
                    },
                ],
                ValidationData=[
                    {
                        'Name': 'email',
                        'Value': email
                    },
                ]
            )
            return True
        except Exception as e :
            return (f"Error : {str(e).split(':')[1]}")
        
    
def confirm_signup(username, validation_code):
    secret_hash = get_secret_hash(username, client_id, client_secret)

    try:
        response = client.confirm_sign_up(
            ClientId='2sus8eu3p7e2mkakvh5map3s2a',
            SecretHash = secret_hash,
            Username=username,
            ConfirmationCode=validation_code
        )
        print("Email address confirmed successfully.")
        bucket_created = buckets.createbucket(username=username, s3=buckets.s3)
        print("Checking line 64 of manage_users.py... This means bucket creation function has been called.")
        print(bucket_created)

        if bucket_created == True:
            out = True
        else :
            out = f"ERROR : {bucket_created}"
            response = client.admin_delete_user(
                UserPoolId='ap-southeast-2_0DWFQCj0M',
                Username=username
            )
            
        return out

    except client.exceptions.AliasExistsException:
        print("deleting the newly created user...")
        response = client.admin_delete_user(
            UserPoolId='ap-southeast-2_0DWFQCj0M',
            Username=username
        )
        return (f"Error : There is an account linked with the given email. Try again with another email.")
    
    except Exception as e:
        return(f"Error : {str(e).split(':')[1]}")
    

    
def delete_user (username) :
    try :
        response = client.admin_delete_user(
            UserPoolId='ap-southeast-2_0DWFQCj0M',
            Username=username
        )
        print(f"User {username} deleted succesfully")
        buckets.deletebucket(username=username, s3=buckets.s3)
    except Exception as e:
        print(e)

def forgot_password (username, password):
    response = client.forgot_password(
        ClientId=client_id,
        SecretHash=get_secret_hash(username, client_id, client_secret),
        Username=username
    )
    confirmation_code = input("Enter the confirmation code sent to the registered mail ID to reset the password : ")

    response = client.confirm_forgot_password(
        ClientId=client_id,
        SecretHash=get_secret_hash(username, client_id, client_secret),
        Username=username,
        ConfirmationCode=confirmation_code,
        Password=password
    )

def check_user_existence(username) :
    try:
        response = client.admin_get_user(
            UserPoolId='ap-southeast-2_0DWFQCj0M',
            Username=username
        )
        return True
    except client.exceptions.UserNotFoundException:
        return False

def login(username, password):
    if check_user_existence(username=username) :
            
        secret_hash = get_secret_hash(username, client_id, client_secret)
        try:
            response = client.initiate_auth(
                AuthFlow='USER_PASSWORD_AUTH',
                AuthParameters={
                    'USERNAME': username,
                    'PASSWORD': password,
                    'SECRET_HASH': secret_hash
                },
                ClientId=client_id
            )
            print("Login successful.")
            return True
        except Exception as e:
            return (f"Error : {str(e).split(':')[1]}")
    else :
        return(f"Error : User with {username} not found.")


def resend_verification_code(username) :
    try:
        response = client.resend_confirmation_code(
            ClientId=client_id,
            SecretHash=get_secret_hash(username, client_id, client_secret),
            Username=username,
        )
        return True
    except Exception as e:
        return (f"Error : {str(e).split(':')[1]}")

username = "venupulagam"
mailid = "venupulagam3926@gmail.com"
password = "helloTest@123"


#login_response = login(username, password)
#signup(username, mailid, password)
#delete_user(username=username)
#forgot_password(username, password)
#print(check_user_existence("venupulagam1"))
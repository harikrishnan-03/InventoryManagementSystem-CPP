import boto3

rds=boto3.client('rds',region_name='us-east-1')

res=rds.create_db_instance(
    DBName='ims_db',  
    DBInstanceIdentifier='x23297948-ims',
    AllocatedStorage=20,
    DBInstanceClass='db.t4g.micro',
    Engine='mysql',
    MasterUsername='root',
    MasterUserPassword='kausthubham',
    BackupRetentionPeriod=7,
    StorageEncrypted=True,
    MultiAZ=False,  
    StorageType='gp2',  
    PubliclyAccessible=True, 
    )
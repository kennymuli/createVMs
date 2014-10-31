import boto.ec2
import time
import os
# EDIT BELOW THIS LINE --------------------------->
#The access key and secret access key can be found in the IAM section of the AWS console. You need to create a user with those credentials if you haven't already, and then assign privileges.
access_key = 'ENTER ACCESS KEY HERE'
secret_access_key = 'ENTER YOUR SECRET ACCESS KEY HERE'

#You need to create a keypair or use an existing one here. AWS Instances can only connect with keypairs, no password options. Make sure your computer has a copy or you will not be able to access your instance.
aws_keypair = 'ENTER YOUR KEY NAME HERE'

#The region codes are as follows (you can copy and paste the one that you need):
# US (N. Virginia)	    		= 'us-east-1'
# US (N. California)	    	= 'us-west-1'
# US (Oregon)				        = 'us-west-2'
# Europe (Frankfurt)	    	= 'eu-central-1'
# Europe (Ireland) 			    = 'eu-west-1'
# South America (Sao Paulo) = 'sa-east-1'
# Asia Pacific (Singapore)	= 'ap-southeast-1'
# Asia Pacific (Sydney)	  	= 'ap-southeast-2'
# Asia Pacific (Tokyo)	  	= 'ap-northeast-1'
region = 'ENTER THE REGION HERE (e.g., us-east-1)'

#Each region's AMI has a unique AMI ID, and it's too exhaustive to list.
ami = 'ENTER YOUR AMI HERE (e.g., ami-9eaa1cf6 is Ubuntu 14.04 LTS for US East 1 region.'


# YOU DON'T NEED TO EDIT BELOW THIS LINE --------------------------------->
#Connect to your EC2 account
conn = boto.ec2.connect_to_region(region, aws_access_key_id = access_key, aws_secret_access_key = secret_access_key)

#If there is an error in your access key, the bottom message will not print.
print('Successfully connected to your account.')
time.sleep(1)

#Select your server size
print ('\n\n\n===================================================================================\n| ID | INSTANCE NAME | vCPUs | RAM | LOCAL DISK | $ PER HOUR LIN | $ PER HOUR WIN |\n|  1 |   t2.micro    |   1   |  1  |    NONE    |     $0.013     |     $0.018     |\n|  2 |   t2.small    |   1   |  2  |    NONE    |     $0.026     |     $0.036     |\n|  3 |   t2.medium   |   2   |  4  |    NONE    |     $0.052     |     $0.072     |\n|  4 |   m3.medium   |   1   | 3.75|    4 SSD   |     $0.070     |     $0.133     |\n|  5 |   m3.large    |   2   | 7.5 |   32 SSD   |     $0.140     |     $0.266     |\n|  6 |   m3.xlarge   |   4   | 15  |   80 SSD   |     $0.280     |     $0.532     |\n|  7 |   m3.2xlarge  |   8   | 30  |  160 SSD   |     $0.560     |     $1.064     |\n|  8 |   c3.large    |   2   | 3.75|   32 SSD   |     $0.105     |     $0.188     |\n|  9 |   c3.xlarge   |   4   | 7.5 |   80 SSD   |     $0.210     |     $0.376     |\n| 10 |   c3.2xlarge  |   8   | 15  |  160 SSD   |     $0.420     |     $0.752     |\n| 11 |   c3.4xlarge  |  16   | 30  |  320 SSD   |     $0.840     |     $1.504     |\n| 12 |   c3.8xlarge  |  32   | 60  |  640 SSD   |     $1.680     |     $3.008     |\n| 13 |   g2.2xlarge  |   8   | 15  |   60 SSD   |     $0.650     |     $0.767     |\n| 14 |   r3.large    |   2   | 15  |   32 SSD   |     $0.175     |     $0.300     |\n| 15 |   r3.xlarge   |   4   | 30.5|   80 SSD   |     $0.350     |     $0.600     |\n| 16 |   r3.2xlarge  |   8   | 61  |  160 SSD   |     $0.700     |     $1.080     |\n| 17 |   r3.4xlarge  |  16   | 122 |  320 SSD   |     $1.400     |     $1.944     |\n| 18 |   r3.8xlarge  |  32   | 244 |  640 SSD   |     $2.800     |     $3.500     |\n| 19 |   i2.xlarge   |   4   | 30.5|  800 SSD   |     $0.853     |     $0.973     |\n| 20 |   i2.2xlarge  |   8   | 61  | 1600 SSD   |     $1.705     |     $1.946     |\n| 21 |   i2.4xlarge  |  16   | 122 | 3200 SSD   |     $3.410     |     $3.891     |\n| 22 |   i2.8xlarge  |  32   | 244 | 6400 SSD   |     $6.820     |     $7.782     |\n| 23 |   hs1.8xlarge |  16   | 117 | 49152 SATA |     $4.600     |     $4.931     |\n===================================================================================\n\n\n\n\n')
instance_selection = raw_input('Please enter the corresponding ID of the instance size you would like to provision from the chart above (e.g., enter 1 for a t2.micro size): ')
while True:
	if instance_selection == '1':
		aws_instance = 't2.micro'
		break
	elif instance_selection == '2':
		aws_instance = 't2.small'
		break
	elif instance_selection == '3':
		aws_instance = 't2.medium'
		break
	elif instance_selection == '4':
		aws_instance = 'm3.medium'
		break
	elif instance_selection == '5':
		aws_instance = 'm3.large'
		break
	elif instance_selection == '6':
		aws_instance = 'm3.xlarge'
		break
	elif instance_selection == '7':
		aws_instance = 'm3.2xlarge'
		break
	elif instance_selection == '8':
		aws_instance = 'c3.large'
		break
	elif instance_selection == '9':
		aws_instance = 'c3.xlarge'
		break
	elif instance_selection == '10':
		aws_instance = 'c3.2xlarge'
		break
	elif instance_selection == '11':
		aws_instance = 'c3.4xlarge'
		break
	elif instance_selection == '12':
		aws_instance = 'c3.8xlarge'
		break
	elif instance_selection == '13':
		aws_instance = 'g2.2xlarge'
		break
	elif instance_selection == '14':
		aws_instance = 'r3.large'
		break
	elif instance_selection == '15':
		aws_instance = 'r3.xlarge'
		break
	elif instance_selection == '16':
		aws_instance = 'r3.2xlarge'
		break
	elif instance_selection == '17':
		aws_instance = 'r3.4xlarge'
		break
	elif instance_selection == '18':
		aws_instance = 'r3.8xlarge'
		break
	elif instance_selection == '19':
		aws_instance = 'i2.xlarge'
		break
	elif instance_selection == '20':
		aws_instance = 'i2.2xlarge'
		break
	elif instance_selection == '21':
		aws_instance = 'i2.4xlarge'
		break
	elif instance_selection == '22':
		aws_instance = 'i2.8xlarge'
		break
	elif instance_selection == '23':
		aws_instance = 'hs1.8xlarge'
		break
	else:
		instance_selection = raw_input('Incorrect input. Please only enter a number 1-23 from the table above (e.g., enter 1 for a t2.micro size): ')

print ('Okay, we will provision '+ aws_instance + '.')

#Name the instance you are about to provision
instance_name = raw_input('Please name your instance: ')

#Script will create the machine
image = conn.get_image(ami)

reservation = conn.run_instances (ami,
	key_name = aws_keypair,
	instance_type = aws_instance,
	security_groups = ['universal'])

instance = reservation.instances[0]
conn.create_tags([instance.id], {"Name" : instance_name})

#Wait for the machine to enter the "running" state, and then collect its IP information (before it enters the "running" state, it will not be assigned an IP)
while instance.update() != "running":
    time.sleep(5)
instance_ip = instance.ip_address

#Once the instance is up, information about it is outputted
print ('\n\n\nMachine created.')
print ('Name: ' + instance_name)
print ('IP Address: ' + instance_ip)

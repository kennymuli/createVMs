import digitalocean
import time
import os

# EDIT BELOW THIS LINE ----------------------------->
#Constants: change these to match the information in your Digital Ocean account.
do_token= 'INSERT YOUR DIGITAL OCEAN TOKEN HERE'
key = (Insert the key here, don not use quotes)

#Image: replace this with the image you would use to build the server. 
#https://assets.digitalocean.com/oslist.png <--- for a full list of the available images.
#Format example: Ubuntu 14.04 x64 would be ubuntu-14-04-x64
image_name ='ubuntu-14-04-x64'

# YOU DON'T NEED TO EDIT ANYTHING BELOW THIS LINE -------------------------> 

def create_droplets():
	#Input for the name of the Droplet.
	cloud = raw_input('Name of the Droplet you want to create: ')

	#Select the size of the Droplet you want to provision.
	size_input = '\n\nHere are the available sizes on Digital Ocean: \n\n (1) 512MB \n (2) 1GB \n (3) 2GB \n (4) 4GB \n (5) 8GB \n (6) 16GB \n (7) 32GB \n (8) 48GB \n (9) 64GB \n\nPlease enter the corresponding size you wish to provision: '
	sizes = raw_input(size_input)
	while True:
		if sizes == "1":
			print 'Okay, will provision 512MB server.'
			rawsize= '512MB'
			break
		elif sizes == "2":
			print 'Okay, will provision 1GB server.'
			rawsize= '1GB'
			break
		elif sizes == "3":
			print 'Okay, will provision 2GB server.'
			rawsize= '2GB'
			break
		elif sizes == "4":
			print 'Okay, will provision 4GB server.'
			rawsize= '4B'
			break
		elif sizes == "5":
			print 'Okay, will provision 8GB server.'
			rawsize= '8GB'
			break
		elif sizes == "6":
			print 'Okay, will provision 16GB server.'
			rawsize= '16GB'
			break
		elif sizes == "7":
			print 'Okay, will provision 32GB server.'
			rawsize= '32GB'
			break
		elif sizes == "8":
			print 'Okay, will provision 48GB server.'
			rawsize= '48GB'
			break
		elif sizes == "9":
			print 'Okay, will provision 64GB server.'
			rawsize= '64GB'
			break


	#Select your region
	region_input = '\n\nHere are the available regions on Digital Ocean: \n\n (1) New York City 1 \n (2) New York City 3 \n (3) New York City 3 \n (4) Amsterdam 1 \n (5) Amsterdam 2 \n (6) Amsterdam 3 \n (7) San Francisco \n (8) Singapore \n (9) London \n\nPlease enter the corresponding region you wish to provision (we test NYC 2 by default): '
	region = raw_input(region_input)
	while True:
		if region == "1":
			print 'Okay, will provision in NYC.'
			rawregion= 'nyc1'
			break
		elif region == "2":
			print 'Okay, will provision in NYC.'
			rawregion= 'nyc2'
			break
		elif region == "3":
			print 'Okay, will provision in NYC.'
			rawregion= 'nyc3'
			break
		elif region == "4":
			print 'Okay, will provision in Amsterdam.'
			rawregion= 'ams1'
			break
		elif region == "5":
			print 'Okay, will provision in Amsterdam.'
			rawregion= 'ams2'
			break
		elif region == "6":
			print 'Okay, will provision in Amsterdam.'
			rawregion= 'ams3'
			break
		elif region == "7":
			print 'Okay, will provision in San Francisco.'
			rawregion= 'sfo1'
			break
		elif region == "8":
			print 'Okay, will provision in Singapore.'
			rawregion= 'sgp1'
			break
		elif region == "9":
			print 'Okay, will provision in London.'
			rawregion= 'lon'
			break

	#Create machines based on inputs above
	droplet = digitalocean.Droplet(token=do_token,
	                               name=cloud,
	                               region=rawregion, 
	                               image=image_name,
	                               size_slug=rawsize,
	                               ssh_keys=[key])
	droplet.create()

	#If successfully created, this will print.
	print '\n\nYour ' + rawsize + ' virtual machine was successfully provisioned in the \'' +rawregion+ "' region. You VM is called '"+cloud+".'"

	#Collect the IP address of the machine that was just provisioned
	while True:
		time.sleep(1)
		droplet.load()
		if droplet.ip_address:
			droplet_ip = droplet.ip_address
			break
	time.sleep(1)

	#Use the IP to do continuous ping tests to let you know when the VM is up
	print 'Checking now to let you know when your server is up. Please wait...'
	print ''
	up = os.system('ping -t 1' + droplet_ip)
	while True:
		if up == 0:
			print 'It is up, the program will continue.'
			break
		else:
			time.sleep(3)
			up = os.system('ping -c 1 ' + droplet_ip)

	#Once the system is up, this will print with IP address information
	print ''
	print 'It is up! Your server is ready.'
	print 'Your server IP address is: ' + droplet_ip + '\n\n\n'

#Running the program
confirm_create = raw_input('Do you want to create a machine? (Yes/No): ')
while True:
	if confirm_create == 'yes':
		create_droplets()
		confirm_create == raw_input('Do you want to create another machine?')
	elif confirm_create == 'no':
		print ('Okay, thank you for using the program.')
		break
	else:
		confirm_create = raw_input("Sorry, I don't recognize this input. Please say either yes or no (Yes/No): ")

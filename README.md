createVMs
=========
<P><B>INTRODUCTION/SETTING UP/GETTING STARTED</B>
<P>This project is based on koalalorenzo's <a href="https://github.com/koalalorenzo/python-digitalocean" target="_blank">python-digitalocean</a>. Currently, this version provisions only Ubuntu 14.04 (x64).
<P>There are two things you need to get from your Digital Ocean account to get started:
<BR><BR>
<P><B>GENERATING YOUR DIGITAL OCEAN TOKEN</B>
<P>You should create one by going into your control panel at <a href="http://cloud.digitalocean.com">cloud.digitalocean.com</a>. Once you log in, click Apps & APIs on the left-hand menu at the bottom. Click "Generate a New Token" in the "Personal Access Tokens" section of the new screen. Record the token code, it will not show up again.
<BR><BR>
<P><B>GENERATING YOUR SSH KEY AND ADDING IT INTO YOUR DIGITAL OCEAN ACCOUNT</B>. 
<P>Well, technically this program can run just fine without an SSH key, but it just makes your life easier. See below if you need to create an SSH Key and pair it with your Digital Ocean account.
</ol>
<p>Generate an SSH Key with the following command below if you do not already have one yet.
```python
ssh-keygen -t rsa -C 'YOUR@EMAIL.COM'
```
It will ask you to save it somewhere. Just saving hitting Enter is fine, unless you have a specific directory. Same with passwords.
<p>Afterwards, you'll want to read the file and copy all of its contents. To read the file, use the command below. Then highlight the output and copy it.
```
cat ~/.ssh/id_rsa.pub
```
<p>Go into your <a href="http://cloud.digitalocean.com" target="_blank">Digital Ocean</a> control panel and click on "SSH Keys" on the left side. Click "Add SSH Key" on the top right of the new screen. For a name, put in one that you can associate with the computer you generated the SSH Key with (only the computers with the same SSH key will be able to use that key to get into the server). 
<BR><BR>
<P><B>SETTING UP THE HOST MACHINE</P></B>
<P>In order to use this script, you have to make sure you have koalalorenzo's <a href="https://github.com/koalalorenzo/python-digitalocean" target="_blank">python-digitalocean</a> package. You can get it by installing it with the command below.
```python
pip install digitalocean
```
If you do not have pip, please install it by using the command below:
```python
sudo apt-get install python-pip
```

Ping-Wizard
==================
This python file was originally created to ping a few [League of Legends](http://na.leagueoflegends.com/) server regions (NA, EUW, EUNE, OCE). However, you can use 
this class to ping any url/ip. You can simply create an instance of the PingWizard class and change the title, thread count or most importantly, the urls or ips 
you want to check. The console output will display title, threads pinging what url/ip and then then the output line in this format: name (ip address): ping ms. If an 
ip address is invalid it will automatically be removed before threads are assigned. If an ip address does not respond, the output line will read: name (ip address): 
did not respond.

###Dependencies

ping-wizard requires Python 2.7.3 or newer.

###Download games

You can obtain this program package by either going [here](https://github.com/EricDalrymple91/ping-wizard) :octocat: and downloading the zip file, or 
cloning this repo to your machine using:

	git clone https://github.com/EricDalrymple91/ping-wizard.git
	
###Execution
----------------
In command line/terminal, navigate to the parent directory and run *ping_wizard.py*.

	Examples:
		python ping_wizard.py
	
You will then get an output that looks something like this:
```
League of Legends pings:
Thread 1: Pinging 104.160.131.3
Thread 2: Pinging 104.160.141.3
Thread 3: Pinging 104.160.156.3
Thread 4: Pinging 104.160.142.3
NA (104.160.131.3): 80 ms
EUW (104.160.141.3): 184 ms
EUNE (104.160.142.3): 185 ms
OCE (104.160.156.3): 187 ms
```

## Import ping_wizard.py

As stated above you can simply import this class into another file and make changes to what you want to ping. 
```python
from ping_wizard import PingWizard
```
Create an instance of PingWizard:
```python
pw = PingWizard()
```
You can change the title:
```python
pw.title = "Hello World!"
```
You can change amount of threads to use:
```python
pw.thread_count = 2
```
You can add an ip address:
```python
pw.ips["NA2"] = "104.160.131.3"
```
You can also add an ip address in the form of a url:
```python
pw.ips["NA2"] = "104.160.131.3"
```
Additionally, you can change the entire ips dictionary if you want:
```python
pw.ips = {"NA2": "104.160.131.3", "google": "www.google.com"}
```
Finally, you have to call the *get_pings* method to run the class instance:
```python
pw.get_pings()
```

## License

The MIT License (MIT)

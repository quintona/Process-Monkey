Process-Monkey
==============

This is a process level chaos monkey. There is already an excellent chaos monkey available from the guys at Netflix (https://github.com/Netflix/SimianArmy), however it is geared towards killing instances in an AWS based architecture. This doesn't suite our purposes for 2 reasons:

- Our production environment isn't AWS based
- We need a lower level of granularity for the chaos, because our production environment doesn't use a hypervisor for multi-tenancy, rather we have selected to use a multi-layer resource scheduler, thus an instance or VM isn't good enough. I suspect there will be many more in this situation in the near future given Mesos, Yarn and things like docker. 

Usage
======

At the moment things are very simple, you just install a cron tab to run the monkey, I suggest doing this at a time when you are at work, something to this effect (business hours, every 10 minutes):

```
*/10 08-17 * * 1-5 sudo python3 /your_path/process_monkey.py
```

You will have to install psutil for the script to work. In order to install psutil you will have to install the following packages:
- build-essentials
- python3 
- pip
- python-dev
- psutil (via pip)


Coming soon
===========

The script is extremely basic at the moment, I will soon add the required puppet automation such that you can control the monkeys from within your puppet master instance or simply via your code repo (in a distributed puppet model)

Authors
========

- Quinton Anderson (quintona@gmail.com, @qanderson7)


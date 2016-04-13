#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Ping url/ips to get information on speed

Running this file alone will return your ping in relation to different LoL regions

You can customize the url/ips you want to ping as well as the amount of threads to use

Works for Windows, Mac OS X, Linux
"""
import threading
import subprocess
import socket
import time
import platform
from Queue import Queue


class PingWizard(object):

    def __init__(self):
        """Instance variables:
        title: First thing printed out in the console just as information
        ips: Dictionary of ips you want to ping. Follow this format {title: ip} both as strings
        thread_count: The amount of threads to use in processing the input ips
        lock: Used to make sure print statements don't fall on the same output line=
        """
        self.title = "League of Legends pings:"
        self.ips = {"NA": "104.160.131.3",
                    "EUW": "104.160.141.3",
                    "EUNE": "104.160.142.3",
                    "OCE": "104.160.156.3"}
        self.thread_count = len(self.ips)
        self.lock = threading.Lock()
        self.data = list()

    def get_pings(self):
        """ Creates threads based on self.thread_count

        Filter the urls/ps to delete any that are not valid and convert urls to ips

        Creates a queue for threads to pick ips and return the ping. Unnecessary by default because the length of the
        dictionary (self.ips) creates the thread count. However, if you have a dictionary with many more ips and
        want to alter the thread count to limit processing power, the queue system will be very helpful.

        Start the threads with the target as the ping_ips method and join all the threads.
        """
        print self.title

        invalid_ips = list()
        for test in self.ips:
            ip = self.convert_to_ip(self.ips[test])
            if ip[0] == "error":
                print ip[1]
                invalid_ips.append(test)
            else:
                self.ips[test] = ip
        for invalid_ip in invalid_ips:
            del self.ips[invalid_ip]

        queue = Queue()
        for i in range(self.thread_count):
            worker = threading.Thread(target=self.ping_ips, args=(i + 1, queue))
            worker.setDaemon(True)
            worker.start()
        for ip in self.ips.values():
            queue.put(ip)
        queue.join()
        for data in self.data:
            print data

    def ping_ips(self, i, q):
        """ Pings an ip address

        :param i: Thread name/number
        :param q: The Queue

        Prints the thread number and the ip that is being pinged

        Records the time it takes and output in milliseconds

        Prints the ip title and calculated ping
        """
        while True:
            ip = self.convert_to_ip(q.get())
            name = "".join([x for x in self.ips if self.ips[x] == ip])
            with self.lock:
                print 'Thread {0}: Pinging {1} ({2})'.format(i, name, ip)
            system = platform.system()
            start = time.time()
            ret = subprocess.call('ping {0} 1 {1}'.format("-n" if system == 'Windows' else '-c', ip),
                                  shell=True, stderr=subprocess.STDOUT,
                                  stdout=open('{0}'.format('nul' if system == 'Windows' else '/dev/null'), 'w'))
            duration = time.time() - start
            if ret == 0:
                with self.lock:
                    self.data.append("{0} ({1}): {2} ms".format(name, ip, int(round(duration * 1000))))
            else:
                with self.lock:
                    self.data.append('{0} ({1}): did not respond'.format(name, ip))
            q.task_done()

    @staticmethod
    def convert_to_ip(value):
        """
        Checks if an ip is valid
        Converts a url into an ip or pass if it is a valid url

        :param value:
        :return: String of an ip
        """
        try:
            socket.inet_aton(value)
            return value
        except socket.error:
            try:
                return socket.gethostbyname(value)
            except socket.error:
                return 'error', '{0} is invalid!'.format(value)

if __name__ == "__main__":
    p = PingWizard()
    p.get_pings()

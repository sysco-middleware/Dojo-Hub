[elhosb@elhosb1-prod serverHealthCheck]$ cat sendmail.py
import os
import datetime
import sys
import re

server_url= str(sys.argv[1])
port= str(sys.argv[2])
username= str(sys.argv[3])
password=str(sys.argv[4])
conn_url = "t3://%s:%s" % (server_url, port)

def sendMail():
        os.system('mailx -r "root@server.com" -s "OSB SERVER HEALTH REPORT:" -a status.html -S smtp="smtp.server.com:25" -S smtp-use-starttls -S ssl-verify=ignore -S nss-config-dir="/etc/pki/nssdb/" team@company.com)

statusfile= open("status.html", 'a+')

connect(username, password, conn_url)

def getServerNames():
        domainConfig()
        return cmo.getServers()

def serverStatus(server):
        cd('/ServerLifeCycleRuntimes/' +server)
        return cmo.getState()

def Status():
        sys.stdout = statusfile
        print """<html>
        <head>
        <title>Server Status</title>
        </head>
        <body>
        <br>
        <table border="1" CELLSPACING="0" CELLPADDING="5"> <caption> OSB SERVER's STATUS </caption>"""
        print "<tr><th>Server</th><th>Status</th><th>Health</th><th>Stuck Threads</th><th>Hogging Threads</th></tr>"
#       serverNames= getServerNames()
        domainRuntime()
        cd('ServerRuntimes')
        servers=domainRuntimeService.getServerRuntimes()
        for server in servers:
                s=server.getName()
                state= serverStatus(server.getName())
                cd('/ServerRuntimes/' + s + '/ThreadPoolRuntime/ThreadPoolRuntime')
                h=get ('HealthState')
                health=h.toString().split(',')[1].split(':')[1]
                hogging = get('HoggingThreadCount')
                stuck = get('StuckThreadCount')
                print "<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % (
                str(server.getName()), str(state), str(health), str(stuck), str(hogging))

        print """</table><br>
        </body></html>"""

def HeapStatus():
        sys.stdout = statusfile
        print "\n"
        print """<html>
        <head>
        <title>Heap Status</title>
        </head>
        <body>
        <br>
        <table border="1" CELLSPACING="0" CELLPADDING="5"> <caption> OSB HEAP MEMORY STATUS </caption>"""
        print "<tr><th>Server</th><th>Total memory allocated</th><th>Free memory</th><th>Memory in use</th></tr>"
        serverNames= getServerNames()
        domainRuntime()
        for Name in serverNames:
#                sys.stdout = statusfile
                cd("/ServerRuntimes/"+Name.getName()+"/JVMRuntime/"+Name.getName())
                totalMemory = get('HeapSizeCurrent')
                freeMemory  = get('HeapFreeCurrent')
                usedMemory  = (totalMemory - freeMemory)
                sys.stdout = statusfile
                print "<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % (
                str(Name.getName()), str(totalMemory), str(freeMemory), str(usedMemory))
        print """</table><br>
        </body></html>"""

def jmsStatus():
        print """<html>
        <head>
        <title>JMS Status</title>
        </head>
        <body>
        <br>
        <table border="1" CELLSPACING="0" CELLPADDING="5"> <caption> JMS QUEUE CURRENT MESSAGES AND CONSUMPTION PAUSE STATUS </caption>"""
        sys.stdout = statusfile
        print "\n"
        print "<tr><th>Destination</th><th>Paused Status</th><th>Current Messages in Queue</th></tr>"
        servers = domainRuntimeService.getServerRuntimes();
        if (len(servers) > 0):
                for server in servers:
                        jmsRuntime = server.getJMSRuntime();
                        jmsServers = jmsRuntime.getJMSServers();
                        for jmsServer in jmsServers:
                                destinations = jmsServer.getDestinations();
                                for destination in destinations:
                                         print "<tr><td>%s</td><td>%s</td><td>%s</td></tr>" % (
                str(destination.getName()), str(destination.isPaused()), str(destination.getMessagesCurrentCount()))
                print """</table><br>
                </body></html>"""

def dataSource():
        print """<html>
        <head>
        <title>DataSource Status</title>
        </head>
        <body>
        <br>
        <table border="1" CELLSPACING=0 CELLPADDING=5><caption> OSB DATASOURCE STATUS </caption>"""
        sys.stdout = statusfile
        print "<tr><th>DataSource</th><th>Status</th></tr>"
        print "\n"
        allServers=domainRuntimeService.getServerRuntimes();
        if (len(allServers) > 0):
                for tempServer in allServers:
                        jdbcServiceRT = tempServer.getJDBCServiceRuntime();
                        dataSources = jdbcServiceRT.getJDBCDataSourceRuntimeMBeans();
                        if (len(dataSources) > 0):
                                for dataSource in dataSources:
                                        state=dataSource.getState()
                                        print "<tr><td>%s</td><td>%s</td></tr>" % (
                str(dataSource.getName()), str(dataSource.getState()))
                print """</table><br>
                </body></html>"""

Status()
HeapStatus()
jmsStatus()
dataSource()
sendMail()
disconnect()


[elhosb@elhosb1-prod serverHealthCheck]$

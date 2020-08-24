#!/bin/python

import json
import requests
import urllib

scom_authN_Uri = 'https://<scom_server>/OperationsManager/authenticate'
scom_alerts_Uri = 'https://<scom_server>/OperationsManager/data/alert'
scomHeader = {'Content-Type': 'application/json; charset=utf-8'}
scom_authN_Body = ''
scom_alerts_body = "{\"criteria\":\"((Severity = '2') AND (ResolutionState = '0'))\",\"displayColumns\":[\"severity\",\"monitoringobjectdisplayname\",\"name\",\"age\",\"repeatcount\"],\"classId\":\"\"}"

response = requests.request( "POST", scom_authN_Uri, headers=scomHeader, data = scom_authN_Body, verify=False )

decodeToken = urllib.unquote(response.cookies['SCOM-CSRF-TOKEN'])
scomHeader.update({'SCOM-CSRF-TOKEN': decodeToken})
scomHeader.update({'Cookie': "SCOMSessionId=" + response.cookies['SCOMSessionId']})
print(scomHeader)

response = requests.request( "POST", scom_alerts_Uri, headers=scomHeader, data = scom_alerts_body, verify=False )
print(response.json())
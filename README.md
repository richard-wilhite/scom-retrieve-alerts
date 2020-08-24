# scom-retrieve-alerts
Python example for retrieving scom alert data via REST API for 2019 UR1 and newer

I created this example because I struggled to find info about connecting to the SCOM REST API with anything other than powershell. I was working on an integration for a single pane of glass monitoring tool which ran on linux, so powershell wasn't an option.

You'll need to update the script to include the path to your scom server, by updating these variables. Replace '<scom_server>' with your server's name.
```python
scom_authN_Uri = 'https://<scom_server>/OperationsManager/authenticate'
scom_alerts_Uri = 'https://<scom_server>/OperationsManager/data/alert'
```

For the scom_authN_Body variable you will need to get a UTF8, Base64 encoded string of your account. I found this easiest to do just on the SCOM server in powershell.
```powershell
$creds = Get-Credential
$bodyraw = "AuthenticationMode:$($creds.UserName):$($creds.GetNetworkCredential().Password)"
$Bytes = [System.Text.Encoding]::UTF8.GetBytes($bodyraw)
$EncodedText =[Convert]::ToBase64String($Bytes)
Write-Host $EncodedText
```

Copy/paste the output from the ps terminal into your script, inside the single quotes. Obviously you would not want to leave your non-encrypted credentials in the script were you to put it into a production environment, but I'm sure I don't need to tell you that. ;)

Tweaking the scom_alerts_body variable can expand or alter your results.

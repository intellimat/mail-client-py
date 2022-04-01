# mail-client-py
### Script that lets you connect to an SMTP server, login and send emails.
#### To use this script you need to create a folder named 'configs' in the root.
#### This folder will contain:
- credentials.json
- emailData.json
- smtp_config.json
### The JSON files need to have the following structure
#### credentials.json:
```
{
    "email": string,
    "password": string
}
```
#### emailData.json: 
```
{
  "from": string,
  "to": string,
  "subject": string,
  "body": string
}
```
#### smtp_config.json:
```
{
  "server_address": string,
  "port": number
}
```

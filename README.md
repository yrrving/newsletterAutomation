# newsletterAutomation
An example of how you can build a newsletter automation script in Python

This script reads a CSV file containing a list of subscribers and their email addresses, connects to a Gmail server using the SMTP class, logs in with the specified sender email and password, and then sends an email to each subscriber in the list with the specified subject and message. 
The CSV file should have headers "email" and the rows should be the email addresses.

You can use this script to send automated newsletters to a large number of subscribers. 
You can schedule the script to run at a specific time and date using a task scheduler like 
crontab, or you could use a service like AWS Lambda, Azure Functions, or Google Cloud Functions to run the script at a scheduled interval.

It's important to note that to use this script you need to enable less secure apps to access your gmail account, also you need to have a google account to use this script.

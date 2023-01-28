import win32com.client
import os
import datetime
from datetime import timedelta
import shutil

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
print("OUTLOOK CONNECTED - ")
inbox = outlook.GetDefaultFolder(6) # "6" refers to the inbox
messages = inbox.Items
print("EMAILS LOADED")
# Get the last 48 hours emails
messages = messages.Restrict("[ReceivedTime] >= '" + (datetime.datetime.now() - timedelta(hours=48)).strftime('%m/%d/%Y %I:%M %p') + "'")
print("EMAILS FILTERED BY LAST 48 HOURS")

keywords = ["pdf attachment", "spectrum", "comcast"]
email_addresses = ["", "example@gmail.com", ""]

for message in messages:
    if message.SenderEmailAddress in email_addresses and any(keyword in message.Subject for keyword in keywords) and message.Attachments.Count > 0 and message.UnRead == True:
        # Extract the pdf attachment
        print("found email and matched subject")
        attachment = message.Attachments.Item(1)
        if attachment.FileName.endswith(".pdf"):
            print("found pdf attachement")
            # Save the attachment to the desktop
            fileName = message.Subject + "_EddieTest_" + attachment.FileName
            attachment_path = "C:/Users/eruiz/OneDrive - One Source Communications/Desktop/"

            if not os.path.exists(attachment_path):
                print("path doesnt exist")
                os.makedirs(attachment_path)
            attachment.SaveAsFile(
                os.path.join(os.path.expanduser(attachment_path),
                             fileName))
        message.UnRead = False
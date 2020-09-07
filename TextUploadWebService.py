#!/usr/bin/env python3

import os
import requests

feedbackDir = "/data/feedback"
feedback = dict.fromkeys(["title","name","date","feedback"])
print(feedback)

# list all files
files = [f for f in os.listdir(feedbackDir)]

# traverse through each file
for f in files:
  if f.endswith(".txt"):
    # serialize information into dictionary
    with open(feedbackDir + "/" + f) as fp:
      feedback["title"] = fp.readline()
      feedback["name"] = fp.readline()
      feedback["date"] = fp.readline()
      feedback["feedback"] = fp.readline()
      #print(feedback)

      #POST to feedback
      r = requests.post('http://34.121.68.83/feedback/', data = feedback)
      #if not okay, raise exception
      if not r.ok:
        raise Exception("POST failed with status code {}".format(r.status_code))
    fp.close()
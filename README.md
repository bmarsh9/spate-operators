# spate-operators

### What is this repo used for?  
This repo is used by `spate-ui` to periodically sync official operators into the platform. For example, if we want to add a new "official" operator (e.g. add row to google sheet), we can add the code here and `spate-ui` will pull it in.

### How do I add a new operator?
+ Under the `operators` directory, copy the `template.py` file and re-name it (e.g. network_connection.py).
+ Add your code to the newly created file
+ Edit the `manifest.json` file
+ The `uuid` key must be unique and varchar (length 10)
+ Sync your code from `spate-ui` under the `Operators` tab

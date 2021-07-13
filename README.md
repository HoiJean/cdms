# Client Data Management System
A complex system to manage clients information using python via command line with worlds most secure techniques used in WW2.

**By: Jean Rukundo (0902403) & Kevin Kroos (0892112)**

# System requirements
- Mac/Windows/Linux
- Python 3.8+

# How to run the application.
- Go inside the root project.
Run the command:
```shell
$ python3 main.py
```
# Guide
Every user has it's own role defined by **is_admin** in the database. For every role a different menu array is being loaded. You can login with the credentials discussed in the section login information.  
When the user login an menu will show up. The menu shows an number with an item. For example: '1. Create user'. The user can type the ID into the terminal and the menu will open.  
  
  
**Warning!**
When an operation is executed, the user will not be able to exit out of the command. **The command must be finished**. That mean's for example when an advisor is editing an client in the system, he needs to fill in the complete form in order to return back into the main menu.  
  
**Note:**. 
Allthough an command must be finished, with edit operations all the fields are optional, that means you can simply press enter and the value will not be updated in the database.
  
  
The system can create logs, they will be encrypted and can only being viewed inside the application itself. The logs will be in log.csv file in the root directory of the application. If an system administrator created an backup a zipfile will also occur in the root directy with a prefix name 'backup' and a timestamp after.  
  
If an input is invalid the system will ask to enter the correct one untill the input is successfull. Inputs has also a default minimum requirement of 3 characters and a maximum of 100 characters unless differently specified.  


# Login information

**Advisor**  
Username: advisor  
Password: Ab123456!   
  
**System Administrator**  
Username: sysadmin  
Password: Ab123456!  
  
**Super admin [ Hardcoded ]**  
Username: superadmin  
Password: Admin!23  
  
## Features
- List users
- Manage and search clients 
- Manage advisors
- Manage system administrators
- Reset (temporarily) passwords
- View logs
- Make system backups


#### Disclaimer
Our encryption does not encrypt numbers only letters.

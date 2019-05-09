# PytomationMail
Simple Email Broadcaster with simple adjustment for custom usage.

Work well for DevOps Engineer that need to report to Developers and QA when finish running a CI/CD.

Work well too for Administrator that need to broadcast information to some people frequently and need fast reaction.

## Requirements
- Python 3.5
- Active Email
- Experience using PyCharm IDE (recommended)
- Basic programming skill
- Dockerfile (optional)

## Guide to Use
1. Change variable and other needs
   - I assume you use one of the most popular free email service like gmail or outlook.

   - What you need to do is, change the variable base on your needs. If you want to change the date time format and print out format, you can do it too base on your needs.

   - For variables: check the ```pytomationvar.py```

   - For date time format: check into the the ```pytomationfunc.py``` in the get_date_time function

   - For print out: check into the ```PytomationMail.py```

   - Above explanation is for splitted automation code that suitable for clean customization when need to add many list of receiver name and receiver email.

   - If you prefer run this automation code with single file that contain the complete part you can check the ```PytomationMailStandalone.py``` that I already make it and just edit the variable or anything based on your needs.

2. Execute the Automation Code
   - You can run this automation code from terminal or directly from PyCharm IDE.
   
   - If you are using PyCharm IDE, after you open folder this automation code make sure you mark the ```PytomationMailCore``` folder as source root from PyCharm IDE, else PyCharm IDE will raise an error for import module part. Just click right the folder then search for ```Mark Directory as``` then choose ```Sources Root```

   - Then you can execute the automation code without worry if you already change the variable correctly like email and password then your SMTP email provider.
   
3. Insert to the Dockerfile (Optional)
   - You can insert this automation code in your Dockerfile but make sure you already have python3 on your docker image.
   - You can insert to your Dockerfile for python3 with this command ```RUN apt-get update && apt-get install -y python3```
   - After that you can execute the automation code like you run it on terminal but in Dockerfile format like this example: ```RUN python3 /path/to/yourfile.py```
   
Let me know if something wrong or strange happen just email me at: rienslw@outlook.com

Thank You :D

# Desktop_vocabulary_notifier
Notifies new word with its meanings at customizable interval

## How it works? </br>
* Download source code, csv file and .ico image </br>
* Keep them in same directory
* In source code, add path address of the excel file 
  * In my case it is ``` "C:\\Users\\Shambhavi\\Desktop\\Projects\\Daily Word\\dictionary.csv" ```  
  - PS : Don't forget to use ```\\```
* Compile and Run.

## Add time interval of your choice
* In line 16 
  * You can modify timeout acoording to your need i.e how long you want notification to stay on your screen
      * Like here ```timeout  = 30```  it will last for 30 sec
* In line 19
  * You can modify at what interval you want every new word
     *  Like here ```time.sleep(60*60*4)```, in every 4 hours a new word with its meaning will be notified

## How to make it run in background?
* Win + R -> type cmd -> press enter
* Go to the directory where above mentioned files are
* Type ```pythonw.exe.\Desktop_reminder.py``` 

## Screenshot
<img width="273" alt="Screenshot (138)" src="https://user-images.githubusercontent.com/97522167/154407291-d5a200ba-49c3-4216-a2b3-b8f20c5c4640.png">

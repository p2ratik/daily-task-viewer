#Importing all necessary libraries
import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend
import matplotlib.pyplot as plt
import os
from datetime import datetime
import uuid
#Extracting task and time spent from the data set and plotting it on a pie chart
def pieplot(dic):
    activity = []                    #Task
    time_spnt = []                   #Time spent on each task
    values = list(dic.values())
    for value in values:
        if(value.isdigit()):
            time_spnt.append(value)
        else:
            activity.append(value)    
    #plotiing pie chart
    plt.pie( 
        time_spnt, 
        labels=activity, 
        #colors=colors, 
        autopct='%1.1f%%',
        shadow=True,
        wedgeprops={'edgecolor': 'black', 'linewidth': 2, 'linestyle': '--'} 
    )
    plt.title("Time Spent per task")
    #Creating unique file names for dynamic charts
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    unique_id = uuid.uuid4().hex[:6]
    file_name = f"task_piechart{timestamp}_{unique_id}.png"
    path = os.path.join("static", file_name)
    plt.savefig(path)
    plt.close()
    return file_name
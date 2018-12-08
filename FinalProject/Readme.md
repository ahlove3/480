## IA 480: Detecting Chinese Cyber Actors

### The Problem

**_How to quickly identify likely cyber actors based on associated locations, targets, softwares, and techniques after an attack._**

	This project focused on cyber actors in China. Our aim was to identify and predict which techniques are most likely to be seen in future attacks among various cyber adversaries. We hope that this would allow an organization to quickly classify the likely cyber actors as information is collected specifying details of an attack. We collected all of our data from the not-for-profit think tank MITRE. MITRE collected their supplementary information and data from a variety of cybersecurity firms such as McAfee, RSA, and Crowdstrike. 
	Our dataset was hand filled and contains the name, aliases, targets, softwares, techniques, location or IP address associated with the groups, as well as common times for the groups to attack. Not all the data could be found among the various groups. Between the three groups Night Dragon had information on common times associated with their attacks, whereas the others did not. In comparison, Deep Panda had a significant amount of IP addresses associated with them as well as much more alias than the other cyber adversaries.   
	The actors of focus are Night Dragon, Deep Panda, and Putter Panda. Each group has a variety of associated aliases. Night Dragon is associated with the alias Musical Chairs. Deep Panda can also be associated with the names ShellCrew, WebMasters, KungFu Kittens, PinkPanther, and Black Vine. Putter Panda is commonly associated with the names APT2 and MSUpdater. 
	The groups target a variety of different entities and are all known for utilizing different softwares. The techniques are the only common elements among the adversaries and when combined with each adversaries associated targets, softwares, and aliases, can be used as a means of identification in the future.  The common techniques found among the various groups include: File Deletion, Command-Line Interface, as well as Process Discovery. 
	Night Dragon is known to target oil, gas, and petrochemical companies. Deep Panda targets various industries governments, defense, financial, and telecommunication while Putter Panda targets space, satellites, and remote sensing technology. 
	While building and testing our model we ran into a few unforeseen problems. It makes sense, In hindsight, for our model to have lower kappa and accuracy scores because of the data of choice. All information on the cyber actors was collected and utilized because the actors and their associated attacks are open source knowledge. Much of the critical information which would be useful in a machine learning model, such as ours, may not be easily accessible in the public domain. Cyber actors of interest, if successful, will not have a large amount of information known on their techniques, software utilized, and known IP address associations. If this knowledge is commonly known and easily accessible on the internet, it is assumed the actors would change associated techniques and methods for attacks, otherwise they would not be successful in the future. 

### The Data



Our data was compiled from the open-source data provided by [MITRE](https://attack.mitre.org/groups/)

From their data we created a spreadsheet that contained:
- The groups we were focused on
- Their known aliases
- The industries they typically target
- The software they are known to use
- Any specific techniques that they are known to use
- The location of the IP address typically associated with their attacks (if available)
- The known times of attacks

### Trained Models
**Deep Learning**
![Image of Deep Learning](DeepLearning/Deep_Learning_Results.PNG)
[Deep Learning Model](DeepLearning/Deep_Learning_Process.xml)

**Decision Tree**
![Image of Decision Tree](DecisionTree/Decision_Tree.PNG)
[Decision Tree Model](DecisionTree/Decision_Tree_Process.xml)

### Justification of the selection of models and parameters;

### Conclusion and limitation of your research, and suggestions for improving your model

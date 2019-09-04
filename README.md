# Agile Sprint Success Simulation

## Table of Contents
1.	INTRODUCTION
	*	Background and Problem Description
	*	Simulation Considerations and Limitations
2.	BASIC DATA ELICITATION
	*	Random Parameter Generation
	*	Model Parameters Boolean Specification
3.	MODEL CONSTRUCTION, VERIFICATION, AND VALIDATION
4.	MODEL DESIGN
5.	RESULT ANALYSIS
6.	CONCLUSION
7.	APPENDIX

### 1.	INTRODUCTION

This simulation study tries to predict the probability of success for an agile sprint. Agile methodology is used by almost all major companies to organize and conduct software development. To make the most out of a sprint, companies adhere to several standards and recommendations. Some of these recommendations include effective sprint length, story point estimation etc. The aim of this study is to present an argument for the most important parameters in sprint success and develop an equation. This can be beneficial to the corporate sector as it can provide a tool for the stakeholders to decide whether their plan is adhering to the industry standards and detect if there are any red flags. 

#####	BACKGROUND AND PROBLEM DESCRIPTION

Despite immense effort from the stakeholders, there is no industry standard tool to predict whether a sprint plan has been effectively designed. Every company’s culture is different and thus every sprint plan has to be unique. There are several factors like nature of job, expertise of the team etc. that separate teams and their sprints from each other. The equation helps the team to validate their sprint plan and prevents any catastrophic project planning disaster.
	
##### SIMULATION CONSIDERATIONS AND LIMITATIONS

The simulation considers three major factors which are team size, sprint length, and story point estimation. There are several sub factors that are considered by the study to decide upon the chosen factors. All of the three factors are listed below along with the subfactors:

1. Team Size
	*	Nature of work
	*	Size of company
	*	Software project
2.	Sprint Length
	*	Pre and Post Sprint Planning
	*	Buffer time
	*	Team type (Hardware / Software)
3.	Story Point Estimation
	*	Task
	*	Technology
	*	Estimation Accuracy
 
The study has its own limitation and data collection is the biggest one. Data collection from agile scrum boards is the biggest challenge as the required data for verification and validation is not publicly available. It contains high amounts of sensitive information regarding ongoing or past projects for the companies and this data is usually kept private by the company for internal use. Companies employing agile protect this information, so no open source data is available. Solutions to this problem is using scientific methods to elicit data. However, there is an online application called Jumble for Jira which generates sample data. This sample data can be used to verify and validate the model but there is no evidence that the sample data for verification and validation represents a data set from the industry.

### 2.	BASIC DATA ELICITATION

Data elicitation will be done using random number generator. After the numbers have been generated the model parameters will need to be assigned their associated tag. The tag for the model variables in this context are Booleans. The model uses three primary parameters: team size, sprint length, and story point estimation. The range and the Boolean cutoff values for the parameters are discuss below. 

#####	RANDOM PARAMETER GENERATION

Data is randomly generated in excel using the RANDBETWEEN([LOW], [HIGH]) function. The low and high bounds for the function are discussed below:  

*	Team Size: The range for the low and high is between 2 and 15. 
*	Sprint Length: Range for the low is 1 weeks and high is 4 weeks. 
*	Story Point Estimation: Range for minimum story points per sprint is 40 while the maximum is 570.

According to Mark Levison, whenever a new person is added to the team, he/she increases the productivity but that also increases the communications overhead. The formula for communications within a team there are n*(n-1)/2 connections (2016). This dictates the recommended range for the size of the team. The lower bound for the team size is two as a team cannot be smaller than two people. A single person cannot constitute a team, but the determination of the upper limit is not that easy as a team can be made as large as the team manager wants it to be. But there is the issue that it can lead to a highly inefficient team as the communication overhead is very large. For the calculation of purpose of the higher limit, the recommended team size is multiplied by a factor of two which comes out to be fifteen people in a team. The recommended team size is discussed in the next section.
Sprint length is another important factor that affects a sprint success and a sprint has multiple steps like the backlog management, sprint planning, story point estimation etc. Thus, anything smaller than one week will be too short to create a meaningful sprint. “Originally, Scrum called for one-month sprints, but nowadays many teams have been successful with two-week or even one-week sprints” (Mitch Lacey and Associates, n.d.). So, the lower limit for the sprint length is one week which is suitable for small projects. Whereas, two-week sprints are most common for software development projects. Some projects like hardware naturally take longer to complete and thus require longer sprints. Four-week sprints are more suitable for these projects. Anything longer than four-week sprint will deprive the team of the checkpoints that are required to have a successful sprint (Orgler, 2018). Hence, four weeks is chosen as the upper limit for the range. 

Story point estimation range depends on the crucial assumption that the upper baseline for the story point is twenty. The upper baseline is defined as the story point limit for one user story. The recommended metric to define the upper limit is that no user story is more than sixteen hours of work (Radigan, n.d.). Based on that assumption if twenty story points is upper limit then forty can be the minimum story points in a sprint for a team of seven people. In a similar fashion, five hundred and seventy story points is the maximum story points that a team of seven developers should take on for a two-week sprint. This gives us the range of forty to five hundred and seventy.

#####	MODEL PARAMTERS BOOLEAN SPECIFICATION

The model parameters are assigned Booleans to determine whether a specific parameter would contribute to the success of a sprint. The range of success for team size is three to seven after much research into the industry standard practices. A sprint of length of two to three weeks is considered as a part of the success range. For the story point estimation, the middle fifty percent is selected as the success range.

### 3.	MODEL CONSTRUCTION, VERIFICATION, AND VALIDATION

The model is constructed as a discrete event model in SimPy. The model takes a CSV file as an input for the simulation and returns Boolean output for whether a certain sprint will be successful or not. The model equation and parameters are derived from articles and research papers. Author credibility is taken into consideration when the equations and parameters are decided. Please refer to the resources on the last page for further reference and credibility verification. The model equation is verified by referring to credible sources and it is validated by creating a small sample data set and manually checking the results of the model execution. The model can be further verified and validated with the availability of real-world sprint run data. From several sprints, the data can be extracted and compiled into a CSV which can passed to the simulation. The project owner or the scrum master can be asked to add annotations for the sprints and decide whether the sprint was successful or not. The project owner’s answers can be cross checked with the simulation output to see whether the model is accurate.
 
### 4.	MODEL DESIGN

The model is constructed in python using SimPy library. The model executes by looping through the entities passed in from the CSV and passing the parameter values to the environment process. The environment runs and the output is printed on the console. The input schema for the sprint data consists of three columns. The simulation code is appended in the Appendix. The code can also be accessed online on GitHub at Sprint Success Prediction Model GitHub. Sample input data is shown below along with the result output. 
 
 
### 5.	CONCLUSION

The agile sprint success prediction model is an attempt to create a computer model to predict the chances of success of a sprint. There are several research papers that try to achieve the same outcome using analytics driven testing, regression modelling etc., but it is the one of the first paper to tackle the problem from a simulation point of view. The model constructs a basic framework for further research and development of the model. One of the biggest challenges of the project is the availability of data. For further improvement, real life data should be used. It is also discovered that elicited data leads to false output from the model execution. With the availability of data this simulation can be verified, and validated for further development and use. 


### RESORUCES

* Choosing the Team Size in Scrum. (2016, October 10). Retrieved from 
[https://agilepainrelief.com/notesfromatooluser/2016/10/choosing-the-team-size-in-scrum.html](https://agilepainrelief.com/notesfromatooluser/2016/10/choosing-the-team-size-in-scrum.html)

* Determining Sprint Length. (n.d.). Retrieved from 
[https://www.mitchlacey.com/blog/determining-sprint-length](https://www.mitchlacey.com/blog/determining-sprint-length)

* Orgler, M. (2018, November 12). What is the optimal sprint length in Scrum? Retrieved from 
[https://hackernoon.com/what-is-the-optimal-sprint-length-in-scrum-368e966f3243](https://hackernoon.com/what-is-the-optimal-sprint-length-in-scrum-368e966f3243)

* Atlassian. (n.d.). Secrets to agile estimation and story points. Retrieved from 
[https://www.atlassian.com/agile/project-management/estimation](https://www.atlassian.com/agile/project-management/estimation)

### APPENDIX
1.	Simpy Code

```python
import simpy
import csv
from prettytable import PrettyTable

team_size = []
sprint_length = []
story_point_estimation = []

with open('Simulation_Test_Data - Sheet1.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for i in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            team_size.append(int(i[0]))
            sprint_length.append(int(i[1]))
            story_point_estimation.append(int(i[2]))
            line_count += 1


env = simpy.Environment()
no_of_entity = len(team_size)


def sprint_run(team_size, length, story_point_estimation):
    # Team Size Parameter Decision
    if team_size >= 5 and team_size <= 7:
        team_size_bool = True
    else:
        team_size_bool = False
    # Sprint Length Parameter Decision
    if length == 2 or length == 3:
        sprint_length_bool = True
    else:
        sprint_length_bool = False
    # Story Point Parameter Decision
    if story_point_estimation <= 40 and story_point_estimation >= 10:
        story_point_estimation_bool = True
    else:
        story_point_estimation_bool = False
    yield env.timeout(0)
    # Final Decision
    if team_size_bool == True and sprint_length_bool == True and story_point_estimation_bool == True:
        p.add_row([team_size, length, story_point_estimation, "True", "All parameters satisfied"])
        return True
    elif team_size_bool == True and sprint_length_bool == True and story_point_estimation_bool == False:
        p.add_row([team_size, length, story_point_estimation, "True", "Story Point Estimation is not right"])
        return True
    elif team_size_bool == True and sprint_length_bool == False and story_point_estimation_bool == True:
        p.add_row([team_size, length, story_point_estimation, "True", "Sprint Length is not within the recommended range"])
        return True
    elif team_size_bool == False and sprint_length_bool == True and story_point_estimation_bool == True:
        p.add_row([team_size, length, story_point_estimation, "True", "Team size is not in the bounds"])
        return True
    else:
        p.add_row([team_size, length, story_point_estimation, "False", "More than 1 parameter is false"])
        return False


p = PrettyTable(["Sprint Team Size", " Sprint Run Length", " Sprint Story Point Estimation", " Decision", "Description"])
```

# Considering 1 sprint equal to 1 entity
# Run the simulation

```python 
for i in range(no_of_entity):
    sprint_run_team_size = team_size[i]
    sprint_run_length = sprint_length[i]
    sprint_run_story_point_estimation = story_point_estimation[i]
    env.process(sprint_run(sprint_run_team_size, sprint_run_length, sprint_run_story_point_estimation))

output = env.run()
print(p)

data = p.get_string()

with open('console_output.txt', 'w+') as f:
    f.write(data)

f.close()
```


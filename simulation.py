import simpy
import csv

team_size = []
sprint_length = []
story_point_estimation = []

with open('Simulation_Test_Data - Sheet1.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for i in csv_reader:
        if line_count == 0:
            print('Columns names are ', i[0], i[1], i[2])
            line_count += 1
        else:
            team_size.append(i[0])
            sprint_length.append(i[1])
            story_point_estimation.append(i[2])
            line_count += 1
    print(team_size, '\n', sprint_length, '\n', story_point_estimation)


env = simpy.Environment()
no_of_entity = len(team_size)


def sprint_run(sprint_run_team_size, sprint_run_length, sprint_run_story_point_estimation):
    # Team Size Parameter Decision
    if sprint_run_team_size >= 5 and sprint_run_team_size <= 7:
        team_size_bool = True
    else:
        team_size_bool = False
    # Sprint Length Parameter Decision
    if sprint_run_length == 2 or sprint_run_length == 3:
        sprint_length_bool = True
    else:
        sprint_length_bool = False
    # Story Point Parameter Decision
    if sprint_run_story_point_estimation <= 40 and sprint_run_story_point_estimation >= 10:
        story_point_estimation_bool = True
    else:
        story_point_estimation_bool = False
    # Final Decision
    if team_size_bool == True and sprint_length_bool == True and story_point_estimation_bool == True:
        return True
    else:
        return False

# We are considering 1 sprint equal to 1 entity
# Run the simulation
for i in range(no_of_entity):
    sprint_run_team_size = team_size[i]
    sprint_run_length = sprint_length[i]
    sprint_run_story_point_estimation = story_point_estimation[i]
    env.process(sprint_run(sprint_run_team_size, sprint_run_length, sprint_run_story_point_estimation))

env.run()

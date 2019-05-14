import simpy
import csv
from prettytable import PrettyTable

team_size = []
sprint_length = []
story_point_estimation = []

def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

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

# We are considering 1 sprint equal to 1 entity
# Run the simulation
for i in range(no_of_entity):
    sprint_run_team_size = team_size[i]
    sprint_run_length = sprint_length[i]
    sprint_run_story_point_estimation = story_point_estimation[i]
    env.process(sprint_run(sprint_run_team_size, sprint_run_length, sprint_run_story_point_estimation))

output = env.run()
print(p)

import numpy as np
from database import paswords, usernames
from config import processes

total_pwd = []
total_usr = []
def get_data(processes=processes, usernames=usernames, paswords=paswords):
    for i in np.array_split(paswords, processes):
        total_pwd.append(list(i))
    for i in np.array_split(usernames, processes):
        total_usr.append(list(i))
    return total_usr, total_pwd
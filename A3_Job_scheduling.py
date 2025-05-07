# job scheduling by priority queue

processes = [
    ('P1',0,2),
    ('P2',1,3),
    ('P3',1,5),
    ('P4',2,6),
    ('P5',2,4)
]

#This list contains tuples of processes in the format: (Process ID, Arrival Time, Burst Time).

# E.g., 'P1' arrives at time 0 and needs 2 units to complete.



def jobscheduling(joblist):  #Function definition for scheduling the jobs.
    jobs = sorted(joblist,key=lambda x:x[1])  #Sorts jobs by their arrival time.
    n = len(jobs)  #n: total number of jobs.
    time = 0  # time: keeps track of current CPU time.
    current_queue = [] #current_queue: stores jobs available at current time.
    order = []  #order: list to store the sequence of executed jobs.

    def add_to_current_queue():
        for job in jobs:
            if(job[1]==time):
                current_queue.append(job)   #Adds all jobs that arrive at the current time to the ready queue.
    
    def choose_job():
        choice = None
        for job in current_queue:
            if(choice == None or job[2] > choice[2]):
                choice = job
        if(choice) : current_queue.remove(choice)
        return choice
# Chooses the job with the highest burst time (priority).

# Removes it from the queue after selection.
    
    while(len(order) < n):   #Loops until all jobs are executed.
        add_to_current_queue()
        cur = choose_job()
        if(cur) : order.append(cur[0])
        time = time+1
    return order

# At each time unit:

# Add new jobs to queue.

# Select the highest burst time job.

# Append its ID to order.

# Increment time.

print(jobscheduling(processes))  #Runs the function and prints the job execution order.

#OUTPUT : 

# ['P1', 'P3', 'P4', 'P5', 'P2']

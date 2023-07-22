"""
Module 2 - Slowness
-- Bottleneck
-- Top command on linux to check process
-- iotop disk io usage
-- MacOs Activity Monitor
-- Windows Resource Monitor and Performance Monitor

How Computers Use Resources
- If it's a variable that's currently being used in a function, the data will be in the CPU's internal memory, and our program will 
retrieve it really fast. If the data is related to a running program but maybe not the currently executing function, it will likely
be in RAM, and our program will still get to a pretty fast. If the data is in a file, our program will need to read it from disk, 
which is much slower than reading it from RAM, and worse than reading from disk, is reading information from over the network. 
In this case, we have a lower transmission speed, and we also need to establish the connection to the other endpoint to make the transmission possible,
which adds to the total time needed to get to the data. 

- a cache stores data in a form that's faster to access than its original form. There's a ton of examples of caches in IT. 
A web proxy is a form of cache. It stores websites, images, or videos that are accessed often by users behind the proxy. 

Possible Causes of Slowness
- Process of elimination
- When computer slow
- Out of RAM
- Bottleneck
- Bug
- Logrotate

Slow Web Server
The user encountered slow performance on one of their company's web servers and decided to investigate the issue. They used the Apache Benchmark tool (ab) 
to measure the response time of the website and found that it was slower than expected. Upon connecting to the web server, they discovered that ffmpeg 
processes were consuming excessive CPU, causing an overload.
The user attempted to improve performance by adjusting process priorities using the nice and renice commands but saw minimal improvement. 
They then identified that the ffmpeg processes were being triggered in parallel, leading to an overload. To resolve this, they modified the script that
 called ffmpeg to run the conversions sequentially, and they stopped the existing ffmpeg processes using the killall -STOP command. They implemented a 
 script with a loop to run the ffmpeg processes one by one, significantly improving the server's response time.
With the issue resolved, the user planned to discuss further performance improvement strategies by optimizing the code in the subsequent videos.


SLOW CODE

Writing Efficient Code
Writing clear and maintainable code and only optimizing for speed when necessary. Small time gains may not be worth the effort for infrequently 
executed scripts, but for tasks performed frequently on a large scale, optimization can be beneficial.
The key to making code more efficient is to reduce unnecessary work for the computer. This can be achieved through techniques such as 
storing pre-calculated data, using appropriate data structures, and optimizing code to keep the computer busy while waiting for slow sources of data (e.g., disk or network).
To identify sources of slowness, profilers are essential tools. Profilers measure the resources used by the code, revealing where the program spends most of its time. 
This helps identify functions that are called excessively or unexpectedly slow. By restructuring the code to avoid expensive operations, such as time-consuming file parsing 
or network interactions, overall performance can be significantly improved.
cProfile module used for count functions calls

Using the Right Data Structures
Lists are sequences of elements that allow for adding, removing, and modifying elements. While adding or removing elements at the end is fast, doing so in the 
middle can be slow due to repositioning. Accessing elements by position is fast, but finding an element in an unknown position can be slow for long lists.
Dictionaries store key-value pairs and offer fast key lookup. They are ideal for situations where data needs to be associated with specific keys. 
Unlike lists, dictionaries are not efficient for accessing elements by position or iterating through all elements.
Using lists when elements need to be accessed by position or iterated through entirely. On the other hand, dictionaries are recommended for situations 
requiring frequent key lookups.
Additionally, creating unnecessary copies of data structures, as it can be costly in terms of performance, especially for large structures.

Expensive Loops
expensive operations inside loops can significantly impact the overall performance of a script.
To improve efficiency, moving expensive operations outside the loop whenever possible. 
For example, when sending emails to employees, parsing the data file outside the loop and storing it in a dictionary can save unnecessary parsing time for each employee.
Another optimization tip is to make the loop iterate only over the necessary elements. If only a few elements out of a large list are required, it's wasteful to loop through the entire list.
The use of the "break" statement to exit a loop early when the desired data is found. This can be helpful when the required data is near the beginning of the loop, 
preventing unnecessary iterations through the rest of the list.
The example of displaying the last five users on an internal website illustrates the benefits of optimizing loops. By keeping track of the last logins in memory and updating the list, 
the script can avoid searching the entire log every time it needs to display the latest users.
The segment concludes by emphasizing that the optimal solution may vary depending on the problem and the size of the dataset. 
Small datasets might not require special optimization, while large datasets demand efficient strategies to avoid performance issues.

Keeping Local Results
to avoid expensive operations like parsing large files or downloading data over the network, which can slow down scripts. One approach is to create a local cache, 
storing data in a faster-access format than its original form. Caches are particularly useful for scripts executed regularly and can significantly improve performance.
Caches need to be handled carefully, considering factors like how often to update them and how to handle out-of-date data. For long-term stats, caching can be updated 
less frequently, but for time-sensitive data, the cache might need to be short-lived or updated more frequently.
To validate if the cache is still valid, checks can be added based on modification dates of files or other logic. Decisions about cache frequency should consider
 how often data changes, how critical it is to have the latest data, and how frequently the script runs.
Caches don't always need to be complex structures; they can be simple variables storing temporary results instead of recalculating them each time. 
For example, counting unique users in different groups can be done by using a dictionary to avoid redundant counting.

Slow Script with Expensive Loop
A meeting reminder script that became slow when sending personalized emails to a long list of recipients. They use the time command to measure the execution time of 
the script and identify the part responsible for the slowdown.
To further investigate the performance, they use the pprofile3 profiler with the callgrind file format. The profiler reveals that most of the time is spent in the
 `get_name` function, which opens a CSV file and searches for the name corresponding to each email address in the list.
To optimizes the code by creating a `read_names` function that reads the CSV file once and stores the relevant data in a dictionary. This way, the `get_name` function 
is no longer called repeatedly for each email address, and the script's execution time improves.
Additionally, the profiler now indicates that the `message_template` function is the next bottleneck. This suggests that further optimization could be done to improve 
the script's overall performance.
The video concludes with a summary of the topics covered: using the time command to measure execution time, using a profiler to analyze performance bottlenecks, 
and optimizing code by avoiding expensive loops and using data structures like dictionaries.

Parallelizing Operations
the concept of concurrency and its potential to improve script performance by allowing operations to run in parallel. It emphasizes that in typical scripts involving 
disk or network operations, the script is blocked, wasting CPU idle time. Concurrency enables multiple tasks to execute simultaneously, making better use of the CPU's resources.
The narrator presents two ways to achieve parallelism: splitting tasks into different processes and using threads within a process. They highlight that processes do not 
share memory, while threads can share some memory within the same process. Python provides modules like Threading and AsyncIO for implementing threading.
However, the video also cautions that excessive parallelism may lead to diminishing returns or even slower performance due to resource contention. The right balance needs 
to be found to keep the computer busy without overwhelming it.
The benefits of concurrency are demonstrated through a practical example of data migration, where optimizing code with separate threads per file and distributing the 
workload across multiple machines significantly improved migration speed.
The segment encourages viewers to take time to understand these concepts at their own pace, acknowledging that some aspects may feel complex but are crucial for IT 
specialists and developers seeking to optimize code for resource-intensive tasks.
Threads let us run parallel task inside a process
python using threading and async module.

Slowly Growing in Complexity
The example used is a secret Santa script, which starts with a simple CSV file to store names and emails for a small group of people. 
However, as the service grows and gains popularity, more features are added, such as wish lists, machine learning algorithms, and gift history tracking. 
As the system becomes more complex and handles a larger user base, the choice of technology for storing and handling data needs to evolve accordingly.

The progression in data storage technology is as follows:
1. CSV file: Suitable for a small group, where parsing the file is not a significant performance issue.
2. SQLite: A lightweight database system that works well for handling data as the service grows and includes additional features.
3. Database server: As the user base continues to expand, using a full-fledged database server running on a separate machine becomes necessary.
4. Caching service (e.g., memcached): To further improve performance, a caching service can be added in front of the database server to store
commonly used results in RAM, reducing unnecessary queries.

Similarly, the user-facing side of the project also undergoes a similar progression:
1. Sending emails: Initially, the service sends emails to the participants.
2. Website: As the project grows, a website is added to allow users to check their assigned person and create wish lists.
3. Caching service (e.g., Varnish): For a heavily used website, a caching service can speed up the load of dynamically created pages.
4. Load balancing and cloud deployment: As demand increases, the service may need to be distributed across multiple servers using a load balancer. 
Cloud-based virtual machines offer scalability and flexibility to adapt to changing loads.

The key takeaway is the importance of selecting the right solution for each problem based on its specific requirements and the projected growth of the system. 
Over-engineering a solution that is too complex for the current scale may not be cost-effective, while underestimating future needs could lead to performance 
issues as the system grows.

Dealing with Complex Slow Systems
The focus is on dealing with large complex systems and how to address performance issues in such systems. The example used is an e-commerce site, which involves 
multiple components, including web servers, database servers, billing systems, fulfillment systems, reporting systems, and more. With so many interconnected parts, 
it can be challenging to identify and resolve performance bottlenecks.

To address slow performance in a complex system, the following steps are suggested:
1. Implement a good monitoring infrastructure: Having a monitoring system in place can help identify where the system is spending the most time, allowing you 
to pinpoint potential bottlenecks.
2. Optimize database performance: Check the database for appropriate indexes on frequently queried fields. Ensure a good balance of indexes to improve read 
performance without sacrificing write performance.
3. Consider caching: Implement caching mechanisms to reduce the need for repetitive or resource-intensive calculations.
4. Distribute the workload: If the CPU on a single server is saturated due to high demand, distribute the workload across multiple computers. This may
 involve reorganizing the code to enable distributed processing.
5. Review the necessity of certain components: As systems evolve, layers of complexity can accumulate. Evaluate the necessity of each component to avoid unnecessary work.
6. Seek help from colleagues: When dealing with complex systems, don't hesitate to seek assistance and expertise from colleagues.
The message conveyed is that while dealing with complex systems may seem daunting, there are strategies and tools available to analyze and optimize performance effectively. 
Collaboration and team effort can also play a significant role in overcoming challenges associated with complex systems.

Using Threads to Make Things Go Faster
The focus is on improving the speed of a script that creates thumbnails for a large number of images. 
The script initially takes about two seconds to process 1,000 test images, and the goal is to optimize it further as there are tens of thousands of images to process.

To speed up the process, the script is modified to use parallel processing using Python's `concurrent.futures` module. Two different types of executors are tested: 
`ThreadPoolExecutor` and `ProcessPoolExecutor`.
1. ThreadPoolExecutor: This executor uses threads for parallel processing. The `submit` function is used to schedule tasks for processing in parallel.
2. ProcessPoolExecutor: This executor uses processes for parallel processing. Like with threads, the `submit` function is used to schedule tasks, but 
the underlying processing is done in separate processes.

After implementing both approaches, it's observed that using processes with `ProcessPoolExecutor` yields the best results. The script now takes less than a 
second to finish, and the user time (time used on all processors combined) increases even more.
The video highlights that using threads and processes has different overheads due to safety features in threads. Threads may end up waiting for their turn 
to write to variables, resulting in a small difference in performance compared to processes.

Overall, the addition of threading support to the script improved processor utilization and significantly reduced the processing time for a large batch of images.

It's mentioned that additional improvements can be made, such as checking if thumbnails exist and are up to date before conversion, or adding a progress bar 
while waiting for tasks to finish.

FINAL LAB
sudo apt install python3-pip
pip3 install psutil
python3
import psutil
psutil.cpu_percent()
psutil.disk_io_counters()
psutil.net_io_counters()

ls ~/scripts
sudo chmod +x ~/scripts/multisync.py
./scripts/multisync.py
nano ~/scripts/dailysync.py
./scripts/dailysync.py

#!/usr/bin/env python3
import subprocess
from multiprocessing import Pool
import os


def backup(src):
    dest = os.getcwd() + "/data/prod_backup/"
    print("Backing up {} into {}".format(src, dest))
    subprocess.call(["rsync", "-arq", src, dest])


if __name__ == "__main__":
    src = os.getcwd() + "/data/prod/"
    list_of_files = os.listdir(src)
    all_files = []

    for value in list_of_files:
        full_path = os.path.join(src, value)
        all_files.append(full_path)

    with Pool(len(all_files)) as pool:
        pool.map(backup, all_files)
        
"""
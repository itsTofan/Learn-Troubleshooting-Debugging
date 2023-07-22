"""
CRASHING PROGRAM

1. System Crash
    When encountering an unexpectedly terminated program, the first step is to gather information and narrow down the scope of the problem. 
    If the issue is machine-specific, it may be related to the installation or configuration on that specific computer. Checking if the problem happens 
    reliably and investigating if it's limited to one specific action or customer can further reduce the scope. If the application crashes randomly but only on one machine, 
    it might indicate a hardware or OS-related problem.
    To reduce the scope further, one can try using default configurations or reinstalling the application. If the issue persists, it could be hardware-related. 
    Testing the hard drive on a different computer can help identify if the problem lies in the drive or the rest of the computer. If the issue is not with the hard drive, 
    checking the RAM for errors using tools like memtest86 and examining sensor data for overheating can be helpful.

    If the problem remains unresolved after checking the hardware, it may be related to the OS installation. At this point, reinstalling the OS might be a faster and
    simpler solution than digging into the specific OS issues.
    For application-specific problems, the cause is likely in the application's code, where certain unexpected situations are not accounted for. Identifying and 
    addressing these situations can resolve the issue.
    Overall, diagnosing and troubleshooting system instability requires a systematic approach of narrowing down the scope, checking hardware components, and investigating 
    software-related factors to find the root cause of the problem.

    memtest86

2. Understanding Crashing Applications
    When an application crashes, the first step is to look for logs that might provide information about the failure. On Linux, the system log files in `/var/log` and 
    user log files are examined, while on macOS, the Console app is used, and on Windows, the Event Viewer is utilized. Checking the logs for error messages around the 
    time of the crash can help identify the cause of the problem.

    If the logs don't contain useful error messages, enabling debugging logging in the application may provide more information. This can be done through configuration settings 
    or command-line parameters. Debugging logs can reveal the specific actions and system calls the application is making, helping to pinpoint the root cause.
    If there are no logs or error messages, tools like `strace` on Linux, `dtruss` on macOS, or Process Monitor on Windows can be used to trace the system calls the program 
    is executing. This can provide insights into what files, network connections, or resources the application is accessing.
    If the application used to work fine and recently started crashing, it's essential to investigate what changes occurred. This could be due to a new version of the application,
    changes in libraries or services, or alterations in the overall environment, such as configurations or file locations.
    Having a reproduction case, which is a specific set of steps or inputs that trigger the crash, is crucial for debugging and fixing the issue. Reproduction cases help 
    understand the problem, facilitate quick checking during the debugging process, and assist in reporting bugs to the developers.
    In summary, to find the root cause of a crashing application, one needs to analyze logs, trace system calls, investigate recent changes, and create a concise reproduction case.

3. What to do when you can't fix the program?
    When faced with an application crash in software written by others, there are several options to work around the problem:
    1. Data Input Format: If crashes occur due to incompatible data input formats, a script can be written to preprocess the data and convert it into the format the program expects.
    2. External Service Compatibility: If the application relies on an external service that is no longer compatible, a wrapper can be created to act as a compatibility layer 
    between the application and the service.
    3. System Environment: Ensuring that the application's environment matches the one recommended by the developers may resolve compatibility issues.
    4. Virtual Machines or Containers: Running the application inside a virtual machine or container can provide a separate environment, useful when the required 
    environment conflicts with other applications.
    5. Watchdog: Implementing a watchdog process can automatically restart the application if it crashes, ensuring continuous availability.

    Regardless of the workaround applied, it is essential to report the bug to the application developers. Providing a good reproduction case, detailed steps, and expected 
    vs. actual outcomes can significantly help developers in understanding and fixing the issue.
    Troubleshooting application crashes involves a systematic approach and utilization of these techniques to find workarounds and ensure the application remains functional.

4. Internal Server Error
    In this scenario, a colleague reported that a webpage on the Web server (site.example.com/blogs) is not working, and the server responded with a 500 error. 
    The investigation process involved:
    1. Checking logs: Examining the server logs (/var/log) and the site-specific log (/var/log/site.log) but finding no useful information.
    2. Identifying the web server software: Using `netstat` to discover that the web server running on port 80 is "nginx."
    3. Checking configuration: Examining the configuration files for nginx and uwsgi (a common solution to connect web servers to programs generating dynamic pages).
    4. Enabling debugging: Adding debugging information to the Python script (prod.py) executed by uwsgi.
    5. Identifying the root cause: Discovering that the application was getting a permission denied error when trying to open the var/log/site.log file, 
    which was owned by the root user instead of the application's user.
    6. Fixing the immediate problem: Changing the ownership of the site.log file to the appropriate user (dub-dub-dub data).
    7. Long-term remediation: Suspecting an issue with log rotation configuration and planning to investigate further.
    The troubleshooting process involved utilizing various tools like `netstat`, examining configuration files, enabling debugging, and 
    investigating file permissions to identify and resolve the issue.
    The process showcases the valuable skills needed for diagnosing and resolving IT issues effectively.


CODE THAT CRASHES
1. Accessing Invalid Memory
    When an application crashes due to accessing invalid memory, it means the process attempted to read or write to a memory address outside of its valid range. 
    This commonly happens with low-level languages like C or C++, where programmers need to manage memory manually using pointers.
    To understand why the crash is happening and fix it, one can attach a debugger to the faulty program. Debuggers provide information about the function where 
    the crash occurred, the parameters received, and the address that caused the fault. Debugging symbols need to be included in the executable binary for effective debugging.
    Valgrind and Dr. Memory are powerful tools to detect invalid memory operations, even if they don't lead to a crash. They can identify issues like accessing uninitialized 
    variables, failing to free memory, and invalid pointers.
    After identifying the cause of the crash, one can fix the code themselves or request the developers to do so. If the application is part of an open-source project, 
    patches might already be available, or one can contribute a fix and create a patch.
    In high-level languages like Python, the interpreter usually catches such issues and throws exceptions instead of letting the program crash due to invalid memory access. 
    Dealing with exceptions will be covered in the next video. The skills learned throughout the program can be applied to any piece of code, irrespective of the programming language used.

2. Unhandled Errors and Exceptions
    In high-level languages like Python, Java, or Ruby, programs can trigger errors or exceptions when they encounter unexpected conditions. These errors occur when code 
    makes wrong assumptions, accesses invalid data, or encounters unexpected inputs. Unhandled errors can cause the program to crash unexpectedly.
    When an error occurs, the interpreter will print an error message and traceback, which shows the sequence of function calls leading to the error. However, this may 
    not always be sufficient to identify the root cause.
    To understand and fix the problem, developers can use debugging tools specific to the programming language, such as the BDB interactive debugger for Python. 
    Additionally, developers can use "printf debugging" by adding print statements to the code to display relevant data during the program's execution. The logging module 
    in Python provides a more controlled and flexible way to add debug messages that can be easily enabled or disabled.
    Once the cause of the error is identified, the code can be fixed to handle unexpected conditions properly. This can include ensuring variables are initialized, 
    adding checks for boundary conditions, and making the program more resilient to failures. The goal is to prevent unexpected crashes and provide informative error 
    messages to users, guiding them on how to resolve the issue.
    When working with someone else's code, the same debugging and error-handling principles apply. It's essential to understand the code, identify the problematic areas,
    and apply appropriate fixes while considering the original code's design and requirements.
    Handling errors and exceptions effectively improves the reliability and user experience of the software. By catching and properly handling unexpected conditions, 
    developers can ensure the program behaves more predictably and gracefully recovers from potential issues.

3. Fixing Someone Else's Code
    Understanding and working with code written by others is a common task in IT jobs. When faced with code that lacks comments and documentation, developers can improve their 
    understanding by adding comments as they read through the code. These comments not only help the developer but can also benefit others who may come across the code in the future.
    Reading the tests associated with the code can provide insight into the expected behavior of each function. Tests can also reveal which use cases were considered and which ones were 
    potentially overlooked. If there are insufficient tests, developers can write their own tests to improve code comprehension and ensure that modifications do not introduce new issues.
    When dealing with large codebases, it may not be feasible to read the entire code. Instead, focus on the specific functions or modules related to the problem at hand. Start with 
    the function where the issue occurred, then follow the call hierarchy to understand the context that led to the problem.
    While it's easier to work with a programming language one is familiar with, it's possible to fix bugs in code written in other languages with sufficient debugging and understanding 
    of the problem. Practice is key to improving code reading and comprehension skills, and developers can do this by exploring code they use regularly or contributing to open-source projects.
    By actively working on fixing issues in existing projects, developers not only improve their skills but also contribute to the overall improvement of the codebase and project quality.
    The ability to read and understand someone else's code is a valuable skill in the IT industry, and developers can enhance their proficiency through continuous practice and exposure 
    to diverse codebases.

4. Debugging a Segmentation Fault
    When an application crashes with a segmentation fault, it's useful to have a core file to analyze the crash later. Core files store all the information related to the crash, 
    acting like a snapshot of the crash when it happens.
    To enable the generation of core files, we used the `ulimit -c unlimited` command before running the crashing program again. Once the crash occurred and the core file 
    was generated, we used the GDB (GNU Debugger) to analyze it. We started GDB by running `gdb -c core example`, where `core` is the core file and `example` is the location of 
    the executable that crashed.
    When GDB started, it showed the backtrace of the crash, indicating the function calls that led to the segmentation fault. By using the `up` command, we moved to the calling 
    function in the backtrace to inspect the code around the crash site.
    In the C code, we identified the faulty line in the for loop, which was causing an off-by-one error. This error occurred when the loop iterated one element too many in the 
    `argv` array. By printing the values of the variables involved, we identified the issue and corrected it by changing the less than or equal sign to a strictly less than sign.
    This example showed us how to use GDB to analyze and debug segmentation faults in C programs. In the next video, we'll explore how to debug Python applications that crash with exceptions.
    gdb -c core example

5. Debugging a Python Crash
    We encountered a Python script that was crashing with a KeyError when processing a CSV file generated by a specific user. We began by examining the contents of the 
    file and identified the presence of a Byte Order Mark (BOM), which is used in UTF-16 to distinguish between little-endian and big-endian. As the file was in UTF-8, 
    the BOM caused the script to fail with a KeyError.
    To understand the issue further, we used the Python debugger, pdb3, to step through the code and inspect the variable "row" at the point of failure. This allowed us 
    to see the presence of the BOM before the actual "product code" key.
    To fix the problem, we used the special encoding value "utf-8-sig" when opening the file. This parameter tells Python to remove the BOM if present, and if not, 
    it behaves like regular UTF-8.
    After making this change, we reran the script, and it successfully processed the CSV file without any exceptions.
    The video also mentioned that debuggers like GDB (GNU Debugger) and PDB (Python Debugger) have many advanced features, such as setting breakpoints, watch points, 
    and step-by-step execution. While these features were not covered in detail in the video, they can be valuable for in-depth debugging.
    In the next reading, you can find more information about advanced debugging techniques if you're interested. Additionally, there's a practice quiz to reinforce the 
    concepts covered in the videos.

HANDLING BIGGER INCIDENTS
1. Crashes in Complex Systems
    We learned how to approach troubleshooting and fixing problems in complex systems involving multiple services and computers. When dealing with such systems, 
    we need to consider a bigger picture and examine interactions between different components. Here are the key steps we discussed:
    1. Check the Logs: Investigate log messages in the servers providing the service to find any additional information related to the issue. Look for service-specific 
    logs and system logs to identify any problems affecting the server in general.
    2. Identify Recent Changes: Determine what changes were made between when the system was working correctly and when it started failing. Check for new versions of 
    underlying systems, such as databases, authentication services, or other back-end servers.
    3. Rollback Changes: If possible, roll back any recent changes that might be causing the issue. Rolling back can help restore the service to a healthy state or 
    eliminate the change as a potential cause.
    4. Improve Error Messages: If error messages are unhelpful, update them to include more information about the request, response, and why the error occurred. 
    This can provide valuable context for future debugging.
    5. Investigate Logs First: Don't assume that a recurring problem has the same cause. Always look at the logs first and see what information they provide to 
    avoid premature conclusions.
    6. Remove Faulty Servers: If you identify a faulty server causing issues, remove it from the pool of servers to prevent users from encountering further errors.
    7. Have Good Logs and Monitoring: In complex systems, good logging and monitoring are crucial for understanding what's happening. Monitoring helps keep track of
    the service's behavior, while logs provide insights into specific incidents.
    8. Use Version Control: Keep all changes under version control so that you can quickly check what has changed and roll back when necessary.
    9. Quick Server Deployment: Have a rapid and reliable process for deploying new servers when needed. This can be achieved through standby servers or automated deployment pipelines.
    10. Consider External Limits: When servers run as virtual machines, external limits on resources like CPU, RAM, or network bandwidth may apply. Be aware of these limits 
    and adjust resource usage if necessary.
    By following these steps and best practices, you can effectively troubleshoot and fix issues in complex systems, ensuring that your services run smoothly and meet the 
    needs of your users. Communication and documentation play a significant role in handling bigger incidents, and we'll explore that aspect in the next topic.

2. Communication and Documentation During Incidents
    The importance of effective communication and documentation when troubleshooting and resolving issues. Here are the key points:
    1. Documenting the Process: Keep track of what you've tried and the results in a bug or ticket system, text file, wiki, or any accessible documentation tool. 
    This helps you remember your actions and share information with other team members.
    2. Clear Communication with Affected Users: Regularly update users on the progress of issue resolution, available workarounds, and expected timeframes for a solution.
    Clear communication allows users to plan and organize their activities accordingly.
    3. Task Distribution: In large incidents involving multiple team members, agree on who will work on specific tasks. Designate roles such as someone handling temporary 
    workarounds, someone investigating the root cause, and a communications lead to keep users informed.
    4. Incident Commander/Controller: Designate a person to oversee the incident response, ensure effective resource utilization, avoid duplication of work, and control 
    changes to the production system.
    5. Post-Incident Summary: After resolving the issue, provide a summary including the root cause, diagnosis process, remediation steps, and measures to prevent the 
    problem from reoccurring. Depending on the severity and scope of the incident, this summary can be a final update in the bug/ticket or a more detailed postmortem.
    By implementing effective communication and documentation practices, you can ensure smoother troubleshooting processes, reduce downtime, and minimize user frustration 
    during incidents. The next topic will cover postmortems and how to conduct them effectively.

3. Writing Effective Postmortems
    Writing postmortems is a valuable practice to learn from incidents, prevent future issues, and improve the overall system. Here are the key points about postmortems:
    1. Purpose: Postmortems are documents that describe incident details, not to assign blame, but to learn from mistakes and prevent similar issues in the future.
    2. Content: Include what caused the issue, its impact, how it was diagnosed, short-term remediation, and long-term recommendations for prevention.
    3. Structure: The postmortem's structure may vary based on the incident, but it typically includes a summary of root cause, impact, and prevention steps for easy sharing.
    4. Highlighting Success: Acknowledge what went well during the incident response, including effective tools, systems, and processes that helped mitigate or resolve the problem.
    5. Practice Makes Perfect: You can practice writing postmortems for any situation, not just major incidents. It helps improve your understanding and problem-solving skills.
    6. Mental Notes: Not every postmortem needs to be a full document. Even mental notes or short summaries can help you learn from experiences and improve in the future.
    Remember, the key focus of postmortems is continuous improvement, not blame. By applying these practices, teams can become more resilient, proactive, and efficient in 
    handling incidents. The next topic will be a quiz to reinforce your understanding of the concepts covered.

    
FINAL LAB
cd /
python3 /usr/bin/infrastructure
sudo apt install python3-pip -y
pip3 install matplotlib
python3 /usr/bin/infrastructure
cd ~
ls
mv data.bak data.csv
cd /
python3 /usr/bin/infrastructure
cat ~/data.csv
sudo chmod 777 ~/data.csv
nano ~/data.csv

"""
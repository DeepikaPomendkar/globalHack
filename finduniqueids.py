new = open("E:/PythonProjects/globalHack/new_job_ids.txt", "a")
jobs = new.read()
new_job_ids = jobs.split("\n")

old = open("E:/PythonProjects/globalHack/ob_ids.txt", "a")
old_jobs = old.read()
old_job_ids = old_jobs.split("\n")
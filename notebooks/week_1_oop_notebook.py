# WEEK 1: OBJECT-ORIENTED PROGRAMMING IN PYTHON
# ============================================
# This is a learning notebook for strengthening your understanding of classes,
# objects, and object-oriented programming in Python — with later applications to
# scheduling and optimization problems.

# --------------------------------------------
# SECTION 1 — BASICS OF CLASSES AND OBJECTS
# --------------------------------------------

# Exercise 1.1: Define a basic class `Job` with attributes: job_id, processing_time, due_date.
# Add a method that returns a string with job information.

# YOUR CODE HERE


# Exercise 1.2: Instantiate 3 Job objects with made-up data and store them in a list.
# Print each job using the method from above.

# YOUR CODE HERE


# Exercise 1.3: Add a method to compute the completion time of a job given a start time.
# Example: job.compute_completion(start_time=5) should return 5 + processing_time.

# YOUR CODE HERE


# --------------------------------------------
# SECTION 2 — CLASS COMPOSITION
# --------------------------------------------

# Exercise 2.1: Create a class `Schedule` that takes a list of Job objects.
# Add a method that calculates start and completion times for a sequential schedule (single machine).
# Store the results in internal attributes.

# YOUR CODE HERE


# Exercise 2.2: Add a method to your `Schedule` class that computes:
# (a) makespan (i.e. the total time needed to complete all jobs)
# (b) total tardiness (sum of max(0, completion - due_date))

# YOUR CODE HERE


# --------------------------------------------
# SECTION 3 — EXTENDING CLASSES VIA INHERITANCE
# --------------------------------------------

# Exercise 3.1: Create a subclass `MultiMachineSchedule(Schedule)` that takes an
# additional parameter: number of machines.
# Extend the schedule method to assign jobs round-robin to machines.

# YOUR CODE HERE


# --------------------------------------------
# SECTION 4 — APPLYING TO AN OR CONTEXT
# --------------------------------------------

# Exercise 4.1: Load job data from a CSV file using pandas (jobs.csv).
# Create Job objects from this data.

# YOUR CODE HERE


# Exercise 4.2: Sort the jobs by due date (EDD rule) and re-evaluate the schedule.

# YOUR CODE HERE


# --------------------------------------------
# SECTION 5 — SOLUTIONS
# --------------------------------------------
# You can find the complete solution in `notebooks/week1_oop_solution.ipynb`.
# Do not look before you try solving yourself! :)

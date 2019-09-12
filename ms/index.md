# Milestone Instructions

Table of Contents:
* [Introduction to the Project](#introduction-to-the-project)
* [General Milestone Instructions](#general-milestone-instructions)
* [The Issues Backlog](#the-issues-backlog)
* [Milestone 1](#milestone-1)

## Introduction to the Project

The initial focus of your team project is to create a command-line utility that
allows people to track how they spend their time.  Questions your team will want
to answer right away are:

1. What name should you give this command-line utility?
1. What arguments should drive its use?  That is, what is the command-line
interface for tracking time?

For example, if you gave your utility the incredibly boring name `timer`, you
might elect to have users track time spent on Software Engineering class like
this:

```
timer start softeng
timer stop softeng
```

This is just an example.  Again, you will determine what the command-line interface will look like, though over the course of the semester you will be restricted somewhat by the instructions for each milestone.

## General Milestone Instructions

The Project Manager (PM) for your first milestone will be the first person listed on the [team rosters](../teams.md).  The PM role will shift in round-robin fashion from there forward (i.e., the second person listed will be PM for milestone 2, the third will have milestone 3, etc.).  After the last person has served as PM, the rotation will start over with the first person serving as PM again.

All project issues, features, bugs, etc., will be described in separate GitHub Issues in your project's repository.  We will refer to this as your *backlog*.  Your PM will be responsible for adding these.  Some issues will come from individual milestone descriptions (see below).  Some may be entered by your instructor.  Some can come from your own creative ideas (e.g., "Wouldn't it be cool if we supported Feature X...?").

At the start of each milestone sprint, your team will have a stand-up meeting in your team's work location (to be assigned by the instructor).  Your PM will place the issues you will work on for the sprint into a GitHub Milestone.  Each issue will be assigned to no fewer than two developers.

Coding work on an issue should be done in Git branches.  Branches should be merged through the creation of a Pull Request (PR).  One of the assigned developers should create the PR.  It is the responsibility of the PM to assign at least two reviewers to each PR.  There should be *substantive* discussion on each PR before the associated code is merged into the `master` branch.  A comment like "Looks good!" is only acceptable if the code is exceptionally bullet-proof and well-organized with respect to known design principles (e.g., coupling, cohesion, SOLID, etc.), and even then you should probably comment on *why* the code looks exceptionally bullet-proof and well-organized.

All issues and the milestone should be appropriately closed by class time on the due date.  If for some reason an issue is not completed, the reason should be thoroughly documented via a comment on the GitHub Issue itself.

## The Issues Backlog

Over time, it is likely that you will have more issues in GitHub Issues than you have as part of your current milestone.  Issues are a great way to track not only needed code for features and bug fixes, but also needed design discussions (e.g., "Where should we store our timer information and what should the format look like?").

## Milestone 1

*Stand-up: 9/17, Due: 9/24*

For this milestone, you'll need to do three things.

* Give your timer program a `start` subcommand that works.  You get to choose the name and syntax.
* Give your timer program a `stop` or `end` subcommand that works.  You get to choose the name and syntax.
* Agree on where you will store the data your timer records and the format of that data.  This should be documented in its own issue.

Separate developer pairs should work on each of the above.
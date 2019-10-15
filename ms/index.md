# Milestone Instructions

Table of Contents:
* [Introduction to the Project](#introduction-to-the-project)
* [General Milestone Instructions](#general-milestone-instructions)
* [The Issues Backlog](#the-issues-backlog)
* [Grading of Milestones](#grading-of-milestones)
* [Milestone 1](#milestone-1)
* [Milestone 2](#milestone-2)
* [Milestone 3](#milestone-3)

## Introduction to the Project

The initial focus of your team project is to create a command-line utility that
allows people to track how they spend their time.  Questions your team will want
to answer right away are:

1. What name should you give this command-line utility?
1. What arguments should drive its use?  That is, what is the command-line
interface for tracking time?

For example, if you gave your utility the incredibly boring name `tracker`, you
might elect to have users track time spent on Software Engineering class like
this:

```
tracker start softeng
tracker stop softeng
```

This is just an example.  Again, you will determine what the command-line interface will look like, though over the course of the semester you will be restricted somewhat by the instructions for each milestone.

## General Milestone Instructions

The Project Manager (PM) for your first milestone will be the first person listed on the [team rosters](../teams.md).  The PM role will shift in round-robin fashion from there forward (i.e., the second person listed will be PM for milestone 2, the third will have milestone 3, etc.).  After the last person has served as PM, the rotation will start over with the first person serving as PM again.

All project issues, features, bugs, etc., will be described in separate GitHub Issues in your project's repository.  We will refer to this as your *backlog*.  Your PM will be responsible for adding these.  Some issues will come from individual milestone descriptions (see below).  Some may be entered by your instructor.  Some can come from your own creative ideas (e.g., "Wouldn't it be cool if we supported Feature X...?").

At the start of each milestone sprint, your team will have a stand-up meeting in your team's work location (to be assigned by the instructor).  Your PM will place the issues you will work on for the sprint into a GitHub Milestone.  Each issue will be assigned to no fewer than two developers.  The name of the acting PM should be specified in the milestone's description.

Coding work on an issue should be done in Git branches.  Branches should be merged through the creation of a Pull Request (PR).  One of the assigned developers should create the PR.  It is the responsibility of the PM to assign at least two reviewers to each PR.  There should be *substantive* discussion on each PR before the associated code is merged into the `master` branch.  A comment like "Looks good!" is only somewhat acceptable if the code is exceptionally bullet-proof and well-organized with respect to known design principles (e.g., coupling, cohesion, SOLID, etc.), and even then you should probably also comment on *why* the code looks exceptionally bullet-proof and well-organized.

All issues for the milestone should be closed by class time on the due date.  If for some reason an issue is not completed, the reason should be thoroughly documented via a comment on the GitHub Issue itself.

## The Issues Backlog

Over time, it is likely that you will have more issues in GitHub Issues than you have as part of your current milestone.  Issues are a great way to track not only needed code for features and bug fixes, but also needed design discussions (e.g., "Where should we store our tracker information and what should the format look like?").

## Grading of Milestones

Milestones will be evaluated on the following criteria.

* How well you curate issues and group them into a milestone.
* How well you participate in evaluation of Pull Requests, and whether issues are closed using Pull Requests whenever the issue is resolved by merging code into the master branch.  Issues should be automatically closed by the closing of a PR provided you properly reference the issue number in the body of the PR (see ["Closing issues using keywords"](https://help.github.com/en/articles/closing-issues-using-keywords))
* How well you code.  Did you close issues, and to what degree is your code *reliable* and *maintainable*?  This includes the elimination of debugging code, junk files, etc.  Is your code easy to crash, or does it properly check inputs and preconditions?  Does your code comply with PEP8 (hint: use the `pycodestyle` tool to check code for you)?

Starting with milestone 3, you will also be judged on the presence of unit tests and the test coverage of your code base.

Also, starting in a future milestone (to be determined), you will be judged on your design documentation.  You will be notified in that future milestone description when it is posted.

Finally, you will be judged based on your participation on the team for each milestone.  If it's clear an individual is not participating adequately, that individual's grade will be reduced.

## Milestone 1

*Stand-up: 9/17, Due: 9/24*

For this milestone, your primary focus is to do three things. Each of the three should reside in its own issue.

1. Give your tracker program a `start` subcommand that works.  You get to choose the name and syntax.  It should be clearly documented in your issue description and/or issue comments.
1. Give your tracker program a `stop` or `end` subcommand that works.  You get to choose the name and syntax.  It should be clearly documented in your issue description and/or issue comments.
1. Agree on where you will store the data your tracker records and the format of that data.  This should be documented in its own issue.  Note that this issue will not be closed by a PR since it is not resolved through code.  Your PM will close the issue manually.  However, you may want to finish this issue first through commentary as a team since the previous two issues depend on it.

Separate developer pairs should work on each of the above.

After you have completed the above three things, you must update your project's
`README.md` file.  At a bare minimum, the `README.md` file must briefly describe
the project and then provide information on how to run your tracker program.

## Milestone 2

*Stand-up: 9/24, Due: 10/1*

Prior to beginning this milestone, please consider the following reminders.

* The code in `master` should always be runnable code.  It should never possess "compile" errors.  This should be true not just at the end of each sprint/milestone, but throughout the entire life of the project.

* *All* code changes must be reviewed as part of a pull request.  If you create issues and fix them via code beyond the issues your instructor assigns, that code must still be reviewed as part of a pull request.  All code gets reviewed by other developers before it gets merged into `master`.  All PRs should automatically close one or more issues (again, see ["Closing issues using keywords"](https://help.github.com/en/articles/closing-issues-using-keywords)).

* Code should be reliable and maintainable. It should be reliable in that it is devoid of bugs.  It should be maintainable in the sense that it is organized in such a way that it anticipates the addition of future features.

With these considerations in mind, in this milestone you will complete the following.

1. Give your tracker program a `labels` subcommand that displays a listing of the labels that have been tracked so far by your tracker program.

1. Give your tracker program a `summary` subcommand that displays the amount of time spent on each label as well as an overall percentage of how much time has been spent on each label.

1. Give your tracker program an `init` subcommand that re-starts the tracking of your timing data.  If this is the first use of the tracker program, `init` should simply prepare your data folders/files/databases/etc. for use.  If you already have data stored, `init` should first ask interactively whether you wish to overwrite your existing data.  Here is an example (and this is only an example) if your data were to be stored under the directory `~/.tracker`.

    ```
    shep@galaxy:~$ tracker init
    /Users/shep/.tracker exists. Do you wish to overwrite (y/n)?
    ```

1. Update your `README.md` to include precise instructions on installing, developing, and running your code.

1. Identify bugs introduced in [Milestone 1](#milestone-1), create issues for them (labeled 'bug'), and fix them.

## Milestone 3

*Stand-up: 10/8, Due: 10/22 (Note new due date)*

Complete the following, at a minimum.

1. Modify your `init` subcommand to accept an optional argument. The argument will be a "data store name" for a completely new data store of timing information.

    Suppose the user typed `tracker init` and then `tracker start softeng` and `tracker stop softeng`.  This sequence of commands would  initialize your data in the default location and then track the timing in that default location.  The name of the default location should be called `default`. That is, `tracker init` should be synonymous with `tracker init default`.

    Then, if one were to type `tracker init gaming` and then `tracker start reddead2` and `tracker stop reddead2`, this would create an entirely new data store separate from where the user previous timed their `softeng` task.

1. Create a `switch` subcommand that switches from one data store to another given a required argument the data store's name.  For example, and in reference to the previous requirement, suppose users typed `tracker switch default`.  Then, they would only be able to see summary information for the `softeng` task they have timed.  If they switched back using `tracker switch gaming`, they would then see the `reddead2` information they timed while tracking under the `gaming` data store.

1. Implement *unit tests* using `pytest` as we did in class.  Cumulatively, your tests should run as much of your project code as possible.  You will want to clearly separate your code into two subfolders: one for your project code itself, and one for testing (name your testing folder `tests`).  Your tests must be *isolated*.  This means that the tests should run in their own environment and should not affect or pollute any pre-existing time data that you have tracked.

1. Create a StarUML class diagram of your classes, and place the `.mdj` file into a folder named `doc`.  Use the class diagram to refactor your code and make it more object-oriented.  This will ultimately make your code easier to test.

1. Keep your `README.md` file up to date (do this always!). One thing to think about is whether moving your project code to a separate folder requires you to modify how you are now running the program (e.g., `python -m tracker start softeng`).

1. Identify bugs introduced in [Milestone 2](#milestone-2), if any.  Create issues for them (labeled 'bug') and fix them.

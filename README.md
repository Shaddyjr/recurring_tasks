# Recurring Tasks #

## Problem:
- Previous task and scheduling applications are disjointed and not collaborated to my personal work style


## Proposal:
I want an application that can handle:
1. Task Management
    1. Recurring and one-off tasks
    1. ~Long, medium, and long term tasks~
    1. Maintain separate “domains”
1. Record keeping
    1. Record completed tasks
1. Usable via phone & (website/API and/or bash script)

## Spec:
1. V0 - MVP locally managed DB (django?) with logic in Python script
1. V1 - Add API connection w/phone app Google Keep
1. V2 - Create React Web App and generalize to include users w/authentication

## Helpful links:
- https://github.com/kiwiz/gkeepapi

## TODO:
- add date validation & others
- implement TCP congestion control (additive increase, multiplicative decrease = probing for bandwith) recurring tasks
- implement RecurringContact model & RecurringContactManagementService & API & CLI
- write tests for services
- Set up Google Keep API webhooks
- Fix recurring tasks not being included in "today's tasks"
- Set up Python typing
- Add TaskPeriod Service
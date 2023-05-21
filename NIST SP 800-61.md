---
tags:
- standard
---
Another from the [[NIST]].

## Executive Summary
- preventive defences are good, but something will always get through
- continuous monitoring is needed in order to identify a baseline, and deviations from it
- relationships with other subject matter experts are necessary for this to work
- to create an incident response capability, you must first create the universe. Then:
	- create an [[incident response]] policy and plan
	- develop procedures for performing incident handling and reporting
	- set guidelines for communicating with outside parties regarding incidents
	- select a team structure and staffing model (all in house, hybrid, mostly outsourced...)
	- establish relationships with internal (legal dept, board) and external (law enforcement, regulator) bodies
	- determine what the scope of the incident response team is, and what services it should provide
	- staff and then train the incident response team
- Reduce the frequency of [[incident|incidents]] as much as possible by doing the work to secure [[network|networks]], systems, and applications
- Document how you interact with other organisations, external and internal, with regards to incidents
- Be generally prepared for any incident, but drill on those that use common [[attack vector|attack vectors]]
- Incident detection and analysis is vital, but requires some forethought - both to set a baseline, but also to ensure you're logging the right things
- Write down what your priotisation criteria are, and make sure your team and organisation know what they are
	- what tools, if any, are there for convincing colleagues that their incidents are not a P1?
- Learn from incidents - both the good and the bad

## Chapter 1: Introduction

## Chapter 2: Organizing a computer security incident response capability

### Events and incidents
- an event is any observable occurence in a system of network. From this we can build [[event-driven architecture]], of which this system is an interesting and complex example.
- adverse events are events that are events with a negative consequence
	- this is a bad definition, because it's retrospective. An event is neutral, but we may find out later that it's adverse. A user clicking a link is an event, and me deleting a database is an event. There's no way to know ahead of time whether or not it's adverse
- a computer security incident is a violation, or imminent threat of violation, of computer security policies, acceptable use policies, or standard security practices
	- oooh, pre-crime. *fun*
- 
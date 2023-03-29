Resilience is a tricky one, because it means a lot of different things across different disciplines. Within ours, however, we consider resilience in the following four ways:
- as a security and survivability problem for managing assets in the pursuit of a mission
- as a capability problem with a focus on the means to plan, absorb, recover and adapt to harmful incidents
- as a business continuity problem, in that it is an outcome and wider than simply being able to react effectively to incidents
- as a capacity and measurement problem, which focuses on the use of data to anticipate, withstand, recover from, and adapt to threats, atacks, stressors, or compromises

## approaches
In order for a system to be resilient and recover quickly, there are a couple of important techniques we can master:
- backups: automated, regular backups mean we can revert to a previous state, limiting disruption
- uninterrupted power supplies (UPS): a device that provides backup power sources in the case of power outages
- fallback processes: in the case of a process being rendered inoperable, the mission can be continued (even in a less effective state). This might mean reversion to paper-based processes, using candles over electric lights, or physical telephone lines over satellite connections
- dependency awareness/modelling: understanding and appreciating the dependency graph of the mission (cf [[Wardley map]]) enables us to prioritise where to focus resilience-building activities. This is to an extent linked with [[risk management]], because we're trying to balance likelihood with expense. For example: building software in containers means there's a lower cost to moving, if our cloud provider goes bust - but also means more expense, as they're not as cheap as the platform's proprietary [[FaaS]].

## Linkov et al. 2014
Linkoev et al. model systems resilience as a curve with four phases:
- plan (before an incident)
- absorb (during an incident)
- recover (after an incident)
- adapt (after recovery)

### CERT-RMM
CERT-RMM defines mission success as security and survivability in the following ten domains:
1. asset management
2. controls management
3. configuration and change management
4. vulnerability management 
5. incvident management
6. service continuity management
7. risk management 
8. external dependencies management
9. training and awareness
10. situational awareness
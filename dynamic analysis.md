Dynamic analysis is the process of examining programs by executing them and observing their behaviour. It involves testing the system with different inputs and studying the resulting outputs to identify potential vulnerabilities, flaws or other issues. Dynamic analysis can also be performed manually or using automated  
tools, such as dynamic analysis tools.

This is more about fuzzing or [[QA testing]], trying to see what will happen if you give the software something unexpected to deal with.

Dynamic code can to some degree look for input validation and check function arguments, but at the cost of run-time performance. Typically, we make use of dynamic analysis during testing.

It's also useful to identify [[malware]], which may only activate when the software is run - thereby evading [[static analysis]].

## tools
- debuggers
- sandboxes
- emulators
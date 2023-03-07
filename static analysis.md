Static analysis is the process of examining source or binary code, or other artifacts (without running it), to identify potential vulnerabilities, flaws or other concerns. Static analysis can detect unsafe functions and lack of input validation. 

Static analysis can be performed manually or using automated tools, such as static code analysis tools. A detailed list of static analysis tools can be found on OWASP’s Source code analysis tool. Many compilers today  
also provide facilities to detect vulnerabilities.

Static code is good for looking for unsafe functions (e.g. `gets()` in `C`), code that's never run (and therefore can be safely removed), memory safety, and type checking (depending on language, making sure types behave the way they are intended to behave). It is unable to conduct input validation or check for all types of function arguments, for which you might need [[dynamic analysis]].
An [[operating system]] that has been developed slowly over time. In the past it was considered fairly insecure, perhaps due to the naivety of the developers, who assumed it would be used in a safe environment. 

In Unix systems, there is a superuser/root account, which has almost limitless ability to work around all security constraints. The only thing they cannot do is read plaintext [[password|passwords]], because the `crypt` function is a one-way [[hash function]]. However, they could overwrite it with, say, `hunter2`.

Users can be organised into groups, and inherit the permissions of that group. Each group has a group ID (GID)

## Processes
Principals - users - are separate from subjects, which in Unix are processes. A process has a real and effective user ID (UID) and a real and effective group ID (GID). 

## Objects
All resources in a Unix system are stored as resources
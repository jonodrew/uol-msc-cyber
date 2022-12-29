A flip-flop is a circuit that can be used to store a [[bit]] value. Consider the design below:

![[Screenshot 2022-10-31 at 08.39.15.png]]

We have two inputs. The lower input, B, goes directly to a NOT gate, and then feeds into an AND gate. The output of the AND gate is one of two inputs to an OR gate. The other input is the upper input, A.

If both inputs are `0`, the output of the circuit will be `0`. If we temporarily change A to `1`, the flow through the circuit will become:
![[Screenshot 2022-10-31 at 08.44.56.png]]
And the circuit will return a `1` value. Similarly, pulsing input B so that it's `1` will switch the circuit to `0`, because of the NOT gate.
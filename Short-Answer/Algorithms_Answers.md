#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)

Run time would be O(n). The while loop won't stop until a is greater than n


b)

I feel like the run time of this one could be O(n*logn). The loop main for loop will run n number of times. The value controlling whether the while loop continues will double every iteration of the while loop.


c)

The run time here would be O(n). With the recursive call of the function it would run equal to the number of times of the input bunnies.

## Exercise II

My approach to this would be to create a function

My function would take in both the number of eggs and the number of floors

Set a variable called floor_check to the len of the floors input

Divide the length of floors by 2 rounding down

Set a variable called egg_check equal to the eggs input

Drop egg_check and check if eggs is greater than temp_eggs

If it is, decrement the floor limit by 1

Otherwise, return floor_check


The run time for this should be O(n) because we'll always start at the half way point of n and move down to the end of the floors input.







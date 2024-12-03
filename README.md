# some-linear-programming
Modelling and solving an optimization problem in production management using matrices and Simplex.
This code comes as a part of my homework assignment for my _Computational Methods_ elective course.

## Context and Description
Given a company's cost function and monthly demand estimates, this code models and optimizes the company's operations to meet production customer demand at the lowest possible cost.


## Notes:
Since the domain for some of the cost inputs (e.g. number of workers) has to be integers, a better solution for this problem would use integer progamming - a much harder method of convex optimization. This implementation uses simple linear programming with outputs over real numbers, which is not ideal for the specific context.

🔍 Prime Factorization
Overview
The prime_factor function computes the prime factors of a given integer. It returns a list of tuples where each tuple contains a prime factor and its exponent.

Function
prime_factor(val)
Parameters:

val (int): The integer for which to compute the prime factors.
Returns:

A list of tuples, each containing a prime factor and its count.
Description:
The function finds the prime factors of the given number by dividing it iteratively by each prime divisor starting from 2. It tracks the count of each prime factor and returns a list of these prime factors along with their counts.

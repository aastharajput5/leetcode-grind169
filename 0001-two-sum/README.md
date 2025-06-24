# leetcode-grind169

# Two Sum

**Problem Link:** [https://leetcode.com/problems/two-sum](https://leetcode.com/problems/two-sum)

## Description
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

## Example
Input: nums = [2,7,11,15], target = 9
Output: [0,1]


## Solution
Uses a hash map to store visited numbers and their indices. Checks if the complement of the current number exists in the map.

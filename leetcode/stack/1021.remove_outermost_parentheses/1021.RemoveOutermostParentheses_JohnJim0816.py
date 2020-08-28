#!/usr/bin/env python
# coding=utf-8
'''
Author: John
Email: johnjim0816@gmail.com
Date: 2020-08-28 09:44:53
LastEditor: John
LastEditTime: 2020-08-28 09:45:06
Discription: 
Environment: 
'''
# Source : https://leetcode.com/problems/remove-outermost-parentheses/
# Author : JohnJim0816
# Date   : 2020-08-28

##################################################################################################### 
#
# A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid 
# parentheses strings, and + represents string concatenation.  For example, "", "()", "(())()", and 
# "(()(()))" are all valid parentheses strings.
# 
# A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to 
# split it into S = A+B, with A and B nonempty valid parentheses strings.
# 
# Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + 
# P_k, where P_i are primitive valid parentheses strings.
# 
# Return S after removing the outermost parentheses of every primitive string in the primitive 
# decomposition of S.
# 
# Example 1:
# 
# Input: "(()())(())"
# Output: "()()()"
# Explanation: 
# The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
# After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
# 
# Example 2:
# 
# Input: "(()())(())(()(()))"
# Output: "()()()()(())"
# Explanation: 
# The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + 
# "(()(()))".
# After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".
# 
# Example 3:
# 
# Input: "()()"
# Output: ""
# Explanation: 
# The input string is "()()", with primitive decomposition "()" + "()".
# After removing outer parentheses of each part, this is "" + "" = "".
# 
# Note:
# 
# 	S.length <= 10000
# 	S[i] is "(" or ")"
# 	S is a valid parentheses string
# 
#####################################################################################################
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        '''
        借助栈来判断，把非外层括号放进答案中。
        '''
        res, stack = "", []
        for c in S:
            # 什么情况下，某个括号要加入结果中呢？非外层括号。
            # 怎么判断是非外层括号？ 1. 左括号加入前，栈不为空。2. 右括号加入并消括号后，栈不为空
            if c == "(": 
                if stack: res += c
                stack.append("(")
            if c == ")": 
                stack.pop()
                if stack: res += c
        return res

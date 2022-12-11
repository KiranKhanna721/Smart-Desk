import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

import cohere
co = cohere.Client('nE237kNXwduF9qeMaou4mGXzbfMmnrfWgiECpDHq')


def app():
    st.title("Programming")
    text = st.text_input("Program Question")
    submit = st.button('Submit')
    if submit:
        if text!=None:
            prompt1 = f"""  
            Question: Write a program to reverse an array or string
            Code:
            def reverseList(A, start, end):
                while start < end:
                    A[start], A[end] = A[end], A[start]
                    start += 1
                    end -= 1
                    
            --  
            Question: You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
            Code:
            def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
                head = ListNode(0)
                curr= head
                carry=0
                while l1!=None or l2!=None or carry!=0:
                    l1val = l1.val if l1 else 0
                    l2val = l2.val if l2 else 0
                    s = l1val+l2val+carry
                    carry = s//10
                    newNode = ListNode(s%10)
                    curr.next  =newNode
                    curr = newNode
                    l1 = l1.next if l1 else None
                    l2 = l2.next if l2 else None
                return head.next
                
            --  
            Question: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
            Code:
            def twoSum(self, nums: List[int], target: int) -> List[int]:
                for i in range(len(nums)-1):
                    for j in range(i+1,len(nums)):
                        n = nums[i]+nums[j]
                        if n==target:
                            return [i,j]
            --  
            Question: Given an array of strings strs, group the anagrams together. You can return the answer in any order.
            Code:
            def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
                answer=[]
                dic = dict()
                for word in strs:
                    key=''.join(sorted(word))
                    if key not in dic:
                        dic[key]=[]
                    dic[key].append(word)
                for a in dic.values():
                    answer.append(a)
                return answer
            --
            Question:"""+str(text)+"""
            Code:
        """
        response = co.generate(model='xlarge',  
                                prompt = prompt1,  
                                max_tokens=500,  
                                temperature=0.6,  
                                stop_sequences=["--"])
        answers = response.generations[0].text
        st.write(answers)
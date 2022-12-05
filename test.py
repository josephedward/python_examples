#!/bin/python3

import math
import os
import random
import re
import sys


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

#
# Complete the 'insertNodeAtPosition' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST llist
#  2. INTEGER data
#  3. INTEGER position
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#


def insertNodeAtPosition(llist, data, position):
    # Write your code here
    if position == 0:
        node = SinglyLinkedListNode(data)
        node.next = llist
        return node
    else:
        node = llist
        for i in range(position-1):
            node = node.next
        new_node = SinglyLinkedListNode(data)
        new_node.next = node.next
        node.next = new_node
        return llist


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input().strip())

    for tests_itr in range(tests):
        llist_count = int(input().strip())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input().strip())
            llist.insert_node(llist_item)

        data = int(input().strip())

        position = int(input().strip())

        llist_head = insertNodeAtPosition(llist.head, data, position)

        print_singly_linked_list(llist_head, ' ', fptr)
        fptr.write('

')

    fptr.close()


def solution(n):
    # TODO convert int to roman string
    roman = ""
    while (n >= 1000):
        roman += "M"
        n -= 1000
    while (n >= 500):
        roman += "D"
        n -= 500
    while (n >= 100):
        roman += "C"
        n -= 100
    while (n >= 50):
        roman += "L"
        n -= 50
    while (n >= 10):
        roman += "X"
        n -= 10
    while (n >= 5):
        roman += "V"
        n -= 5
    while (n >= 1):
        roman += "I"
        n -= 1
    return roman

             def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # sorted = False
        # answer = []
        l1 = list1
        l2 = list2

        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if (l1.val < l2.val):
            l1.next = self.mergeTwoLists( l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists( l2.next, l1)
            return l2



def increment_string(strng):
    head = strng.rstrip('0123456789')
    tail = strng[len(head):]
    if tail == "": return strng+"1"
    return head + str(int(tail) + 1).zfill(len(tail))

    def increment_string(strng):
    if strng == "":
        return "1"
    lead = 0
    num = 0
    if(strng[len(strng)-1]).isdigit() == True:
        revStr = strng[::-1]
        strs =""
        for x in range(0, len(strng)-1):
            if not revStr[x].isdigit():
                strs = revStr[x:]
                strs = strs[::-1]
                print("strs : ", strs)
                num = revStr[:x]
                num = num[::-1]
                break
        listNum = list(str(num))
        num = int(num)+1
        print("strng : ", strng)
        print("strs: ", strs)
        print("listNum : ",listNum)
        print("num : ",num)
        if strs == "":
            listNum = list(strng)
            num = int(strng)+1
        count = len(str(num))
        if len(listNum)>len(list(str(num))):
            print("strs+''.join(listNum[:len(listNum)-count])+str(num) : ", strs+''.join(listNum[:len(listNum)-count])+str(num))
            return strs+''.join(listNum[:len(listNum)-count])+str(num)
        else:
            return(strs+str(num))
    else:
        strng+="1"
        return strng



        lol = lambda lst, sz: [lst[i:i+sz] for i in range(0, len(lst), sz)]


        def isValidParentheses(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in s:
            if i == '(':
                stack.append(')')
            elif i == '[':
                stack.append(']')
            elif i == '{':
                stack.append('}')
            elif not stack or i != stack.pop():
                return False


#Step 1: Traverse the string from left to right. Let’s call the string test_str, and the individual characters in the string char.
#Step 2: If the first character char is an opening bracket (, {, or [, push it to the top of the stack and proceed to the next character in the string.
#Step 3: Now, check if the next character (char) is an opening or a closing bracket.
#Step 3.1: If it’s an opening bracket, push it again onto the stack.
#Step 3.2: If you encounter a closing bracket instead, pop off the stack top, and proceed to step 4.
#Step 4: Here again, there are 3 possibilities based on the value popped off the stack:
#Step 4.1: If is an opening bracket of the same type, loop back to step 3.
#Step 4.2: If it is an opening bracket of a different type, you can again conclude that it is not a valid parentheses string.
#Step 4.3: The final possibility is that the stack is empty. Again, this is the case of an invalid string, as you’ve run into a closing bracket that doesn’t have a matching opening bracket.
def isValid(self, s):
    stack = []
    for char in s:
        if char in ['(', '{', '[']:
            stack.append(char)
        else:
            if not stack:
                return False
            top = stack.pop()
            if (top == '(' and char != ')') or (top == '{' and char != '}') or (top == '[' and char != ']'):
                return False
    return not stack






    class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        self.nums = nums
        return self.recurseSearch(nums,target)


    def recurseSearch(self, nums, target):
        print()
        print("  def recurseSearch(self, nums, target): ")
        print()
        pointer = int(math.floor(len(nums)/2))
        print("nums : ", nums)
        print("pointer : ", pointer)
        print("target : ", target)
        print("nums[pointer] : ", nums[pointer])

        if(nums[0]>target):
            return self.nums.index(nums[0])
            # return nums.index(nums[0])

        if(nums[pointer]==target):
            print("self.nums.index(nums[pointer]) : ",self.nums.index(nums[pointer]))
            return self.nums.index(nums[pointer])

        if(nums[len(nums)-1]<target):
            return len(nums)

        print("nums[pointer]<target : ", nums[pointer]<=target)
        if(nums[pointer]<=target):
            if(nums[pointer]==target):
                return (self.nums.index(nums[pointer]))
            # if(len(nums)==1):
            #     print(pointer+1)
            #     return pointer + 1
            print("nums[pointer:] : ",nums[pointer:])
            if (len(nums[pointer:])==1):
                print("self.nums.index(nums[pointer]) : ",self.nums.index(nums[pointer]))
                return(self.nums.index(nums[pointer]))
            
            return self.recurseSearch(nums[pointer:], target)

        print("nums[pointer]>target : ", nums[pointer]>=target)
        if(nums[pointer]>=target):
            if(nums[pointer]==target):
                return (self.nums.index(nums[pointer]))
            # if(len(nums)==1):
            #     print(pointer-1)
            #     return pointer - 1
            print("nums[:pointer] : ",nums[:pointer])
            if (len(nums[:pointer])==1):
                print("self.nums.index(nums[:pointer][0]) : ", self.nums.index(nums[:pointer][0]))
                return(self.nums.index(nums[pointer]))
            
            return self.recurseSearch(nums[:pointer], target)

   

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
        # You must write an algorithm with O(log n) runtime complexity.
        
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif nums[i] > target:
                return i
        return len(nums)

        

""" Question 1: Given a string S, return the "reversed" string where all characters 
                that are not a letter stay in the same place, and all letters reverse their positions.

1. Test Input and Output
input: "abc-d-ef-dH"
output: "Hdf-e-dc-ba"

2. Pseudocode
Have left and right index, and set them at either ends of the string.
Loop through the input string and check to see if the left end element is a letter or not
If the left end is not a letter then add to an array to hold the reverse string
Move the left index over by one to move along the string
Also, check to make sure the right element is a letter, if not then the right needs to  minus 1 otherwise the array
holding the reverse string will add the characters other than letter.
However, if the left end is a letter then add the element of the right index, while decrementing the right index by one
to move down the array. 

3. Time Complexity: 
This would have a run time of O(n) for best and worst cases because the while loop runs 
however many letters there are in the string, which is n. All the other lines of the code take O(1) time so
we can ignore them when analyzing time complexities.
"""

string_input = "abc-d-ef-dH"
string_output = "Hdf-e-dc-ba"

def reverse(string):
  left = 0
  right = len(string) - 1

  opposite = []

  while len(opposite) != len(string):
    if not string[left].isalpha():
      opposite.append(string[left])
    elif not string[right].isalpha():
      right -= 1
      continue
    else:
      opposite.append(string[right])
      right -= 1
    left += 1

  return "".join(opposite)


"""
Question 2: Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, 
            find the one that is missing from the array.

1. Test Input and Output
input: [9,6,4,2,3,5,7,0,1]
output: 8
input: [3,1,0]
outpt: 2

2. Pseudocode
Sort the array
Loop through the array
Compare the current element to the next element and check to see if the next element is one higher than the 
current element
If it's higher than no nothing but if it's not then return the current element plus one because that will be 
the missing one

3. Time Complexity
The run time for this function is O(n) because it's looping through all the elements and checking to see whether
the following element is one higher. The sort function take O(log(n)) time but since the for loop take O(n) which is longer,
we say this function runs O(n) time.
"""

n_input = [9,6,4,2,3,5,7,0,1]
n_output = 8

def find_missing_n(array_n):
    array_n.sort()

    for i in range(len(array_n) - 1):
        if array_n[i] + 1 != array_n[i + 1]:
            return array_n[i] + 1


if __name__ == "__main__":
    if (reverse(string_input)) == string_output:
        print("reverse function works")
    else:
        print("reverse function does NOT work")

    if find_missing_n(n_input) == n_output:
        print("find missing n function works")
    else:
        print("find missing n function does NOT work")


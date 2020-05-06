""" Question 1: Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.

1. Test Inputs
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



"""
input1 = "abc-d-ef-dH"
# output1 = "Hdf-e-dc-ba"

def reverse(string):
  left = 0
  right = len(string)-1

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

"""


if __name__ == "__main__":
    print(reverse(input1))


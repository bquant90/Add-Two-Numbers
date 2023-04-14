# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def addTwoNumbers(self, l1, l2):
    dummy = ListNode()
    current = dummy

    carry = 0
    while l1 or l2 or carry:
        digit_l1 = l1.val if l1 else 0 # Get the digits of l1, otherwise set it to 0 if it's null.
        digit_l2 = l2.val if l2 else 0
        carry, value = divmod(digit_l1 + digit_l2 + carry, 10) # Get the carry and value in one go. Ex: 15 -> 1 for first parameter, 5 for second parameter.
        
        current.next = ListNode(value)
        current = current.next
        l1 = l1.next if l1 else None # Update the next pointer, otherwise leave it at null.
        l2 = l2.next if l2 else None
    
    return dummy.next

# Create linked list for number 342
l1_2 = ListNode(2)
l1_4 = ListNode(4, l1_2)
l1_3 = ListNode(3, l1_4)

  # Create linked list for number 465
l2_4 = ListNode(5)
l2_6 = ListNode(6, l2_4)
l2_5 = ListNode(4, l2_6)

s = Solution()
result = s.addTwoNumbers(l1_3, l2_5)

# Construct a list of values from the linked list result
result_vals = []
while result:
  result_vals.append(result.val)
  result = result.next

print(f"The first num is: [{l1_2.val}, {l1_4.val}, {l1_3.val}]")
print(f"The second num is: [{l2_4.val}, {l2_6.val}, {l2_5.val}]")
print(f"[{l1_2.val}, {l1_4.val}, {l1_3.val}] + [{l2_4.val}, {l2_6.val}, {l2_5.val}] = {result_vals}")

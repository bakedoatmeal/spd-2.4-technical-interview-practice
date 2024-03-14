# Palindrome linked list
# https://leetcode.com/problems/palindrome-linked-list/description/

def is_palindrome(head)
  current = head
  arrayValues = []
  while current != nil
      arrayValues << current.val
      current = current.next
  end
  halfarray = (arrayValues.length / 2)
  (0..halfarray).each do |index|
      if arrayValues[index] != arrayValues[(-index)-1]
          return false
      end
  end

  return true
end
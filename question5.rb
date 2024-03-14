# Reverse linked ilst
# https://leetcode.com/problems/reverse-linked-list/

# Done in ruby
def reverse_list(head) 
    current = head
    previous = nil
    nextNode = nil
    while current != nil
        nextNode = current.next 
        current.next = previous 
        previous = current
        current = nextNode
    end
    return previous
end
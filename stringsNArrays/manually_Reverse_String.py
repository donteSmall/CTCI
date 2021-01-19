

class linkedListNode:
    def __init__(self, value, nxtNode= None):
        self.value = value
        self.nxtNode  = nxtNode
# -> 3 -> 7 -> 10



#intalize nodes to be linked 
node1 = linkedListNode("3")
node2 = linkedListNode("7")
node3 = linkedListNode("10")

#link nodes together
node1.nxtNode = node2 #node1 -> node2 : "3" -> 7
node2.nxtNode = node3 #node 2 -> : "7" -> 10

# complete linkedlist var
# node1 -> node2 -> node3
currentNode = node1
#Need to fix implementation 
def reversedLinkedlist(head):
    curr = head
    pervious = None 
   
    while True:
        print curr.value + " ->",  

        
        #iterate forward 
        #3 | 
        nxt = curr.nxtNode
        
        curr.nxtNode = pervious

        #3 | None
        pervious = curr 

        if curr.nxtNode is None:
            print("None")
            break
        #b | c
        curr = nxt

    return curr
  
    
reversedLinkedlist(currentNode)

def manuallyReverseString(word):
    lengthOfWrd= len(word)
    reversedStrContainer = []

    while lengthOfWrd > 0:
        # save the value of str[index-1] in reverseString
        reversedStrContainer += word[lengthOfWrd - 1]
        lengthOfWrd = lengthOfWrd -1  #decrement index to stop while loop
    

    return reversedStrContainer

def reversedStringwithJoin(word):
    word = ''.join(reversed(word))
    reversedStrContainer = [    ]
    for letter in word:
        reversedStrContainer.append(letter)

    return reversedStrContainer + [word] 

# print(manuallyReverseString("goat"))

print(reversedStringwithJoin("goat"))
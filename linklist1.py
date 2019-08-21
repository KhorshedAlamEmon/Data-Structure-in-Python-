class linklistNode:
    def __init__(self, value, nextNode=None):
        self.value=value
        self.nextNode=nextNode

node1 = linklistNode("1")
node2 = linklistNode("2")
node3 = linklistNode("3")

node1.nextNode=node2
node2.nextNode=node3

currentNode = node1
while True:
    print(currentNode.value)
    if currentNode.nextNode is None:
        print("None")
        break
    currentNode = currentNode.nextNode
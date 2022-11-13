class Linked():
    def __init__(self):
        self.Head = ""
class Node():
    def __init__(self,Val):
        self.Val = Val
        self.Next = ""

List = Linked()
Node_1 = Node(44)
List.Head = Node_1
Node_2 = Node(36)
Node_1.Next = Node_2

Node_3 = Node(90)
Node_2.Next = Node_3
Node_4 = Node(10)
Node_3.Next = Node_4
Node_5 = Node(60)
Node_4.Next = Node_5
Node_6 = Node(99)
Node_5.Next = Node_6

############## Insert 104 ##########################
Node_7 = Node(104)
Node_7.Next = Node_1
List.Head = Node_7
####################################################

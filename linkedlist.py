class Node:
#function initialise node object
    def __init__(self,data):
        self.data=data #data assign
        self.next=None #initilise next as null

class LinkedList:#linklist class contains a node object

    def __init__(self):#function to initilise head
        self.head=None

    def listprint(self):
        printval=self.head

        while printval is not None:
            print(printval.data)
            printval= printval.next


    def _inset_at_Begining(self,newdata):#add new data
        newNode=Node(newdata)
        newNode.next=self.head
        self.head=newNode
    

    


l1=LinkedList()
l1.head =Node("BMW")
l2= Node ("audi")
l3=Node ("porsche")
l4=Node("lamogini")
l1.head.next=l2
l2.next=l3
l3.next=l4
l1.listprint()

print("")
l1._inset_at_Begining("Benz")
l1.listprint()
print("")
l1._inset_at_Begining("Ferari")
l1.listprint()

        

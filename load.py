import socket
import random
import statistics
# from server import port1
# from server2 import port2

# class Tree:
# 	def __init__(self,val=None,l=None,r=None):
# 		self.value=val
# 		self.left=l
# 		self.right=r

# 	def insert(self,root,val):
# 		if root==None:
# 			return Tree(val)
# 		if root.value<=val:
# 			root.right=self.insert(root.right,val)
# 		if root.value>val:
# 			root.left=self.insert(root.left,val)

# 	def connection_hash(self,root,val):
# 		if root.value<=val and root.right!=None:
# 			return self.connection_hash(root.right,val)
# 		if root.value<=val and root.right==None:
# 			return root
# 		if root.value>val and root.left!=None:
# 			return self.connection_hash(root.left,val)
# 		if root.value>val and root.left!=None:
# 			return root

# def generate_tree(list):
# 	#root_val=statistics.median(list)
# 	root_val=list[0]
# 	T=Tree(root_val)
# 	root=T
# 	for i in range(1,len(list)):
# 		T.insert(root,list[i])
# 	return T	

# server_node_list=[port1,port2]
# T=generate_tree(server_node_list)

s=socket.socket()
port=3000
s.bind(('127.0.0.1',port))
while True:
    s.listen(100)
    c,addr=s.accept()
    print("got connection from "+str(addr))

    # if addr[1]%2==0:
    #     c.send(str("3001").encode())
    # else:
    #     c.send(str("3002").encode())

    # while 1:
    #     print('----round----')
    #     p=random.randint(3001,3002)
    #     flag=c.connect_ex(('127.0.0.1',p))
    #     if flag==0:
    #         c.send(str(p).encode())
    
    p=random.randint(3001,3002)
    c.send(str(p).encode())
    #code

    # rand_no=random.randrange(2000,2050)
    # root=T
    # req_node=T.connection_hash(root,rand_no)
    # c.send(str(req_node.value).encode())

c.close()
s.close()


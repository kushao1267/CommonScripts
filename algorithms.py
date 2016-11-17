#coding=utf-8

def partion(list,begin,end,optimization):#list[index]左边的数都比它小，右边的数都比它大
    if len(list)<=1:
        return (0,list)
    length=len(list)
    isodd = True if length%2==1 else False
    if optimization:
        m=length/2 if isodd else length/2-1
        flag=list.pop(m)  #优化partion
    else:
        flag=smalllist.pop(begin)
    small,big = [],[]  #此处取哨岗，可以取中间值．如果递归，取begin,end,mid而不是一个常量
    for i in list:
        if i<flag:
            small.append(i)
        else:
            big.append(i)
    index = len(small)
    list = small+[flag]+big
    return (index,list)

#Median
def mid_num(list):
    #boundary conditions
    if len(list)<=2:
        return list[0]
    #
    isodd = True if len(list)%2==1 else False
    begin,mid,end=0,len(list)/2 if isodd else len(list)/2-1,len(list)-1
    while True:   
        (index,list)=partion(list,begin,end)
        if index==mid:
            print list
            return list[index]
        elif index<mid:
            begin=index+1
        else:
            end=index-1
    
#small k
def small_k(list,k):
    #boundary conditions
    if len(list)<=k:
        return list
    if k<=0:
        return []
    #
    begin,end=0,len(list)-1
    while True:   
        (index,list)=partion(list,begin,end)
        if index==k-1:
            return list[:k]
        elif index<k-1:
            begin=index+1
        else:
            end=index-1

#quicksort 
def quicksort(list):
    if list==[]:
        return list
    flag,small,big = list.pop(0),[],[]
    for i in list:
        if i<flag:
            small.append(i)
        else:
            big.append(i)
    return quicksort(small)+[flag]+quicksort(big)

#the first number which appear only once  
def appear_once(string):
    hash = {}
    for i in string:
        if i in hash:
            hash[i]+=1
        else:
            hash[i]=1
    for k in string:
        if hash[k] == 1:
            return k

#implement add without '+ - / *'
def add(a,b):   
    if a == 0:
        return b
    sum = a^b
    carry = (a&b)<<1    #dont forget the "()"
    return add(carry, sum)

def fib(n):
    a,b,k=0,1,0
    while k<n:
        list.append(a)
        a,b=b,a+b
        k+=1
    return a

#顺时针构成矩阵

#顺时针打印矩阵
def printmatrix(matrix,columns,rows):
    if len(matrix)==0 or columns<0 or rows<0:
        return 'Invalid Matrix.'
    start=0
    while columns>start*2 and rows>start*2:
        printmatrixcircle(matrix,columns,rows,start)
        start+=1
        
def printmatrixcircle(matrix,columns,rows,start):
    endx = columns - 1 - start
    endy = rows -1 - start
    #起始处的行列一直相同
    #从左到右打印一行
    for i in range(start,endx+1):
        print matrix[start][i]
        
    #从上到下打印一列    
    if start<endy:
        for i in range(start+1,endy+1):
            print matrix[i][endx]
    
    #从右到左打印一行
    if start<endx and start<endy:
        i=endx-1
        while i>=start:
            print matrix[endy][i]
            i-=1
            
    if start<endx and start<endy-1:
        j=endy-1
        while j>=start+1:
            print matrix[i][start]
            j-=1

def number_of_1(n):
    if n==0:
        return 0
    num=0
    while n!=0:
        if n&1==1:
            num+=1
        n=n>>1
    return num

#奇数在前，偶数在后list
def odd_even_list(list):
    if len(list)<=1:
        return list
    i,j=0,len(list)-1
    while i<j:
        while list[i]%2==1:
            i+=1
        while list[j]%2==0:
            j-=1
        if i<j:
            list[i],list[j]=list[j],list[i]
    return list
                       
#旋转数组的最小数字
def rotate_list(list):
    return sorted(list)

#遍历打印，DFS,BFS
class bnode(object):
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
    #插入结点        
    def insert_lnode(self,val):#self起到结点指针的作用
        if self.left is None:
            self.left=bnode(val)
        else:
            self.left.val=val
        return self
    
    def insert_rnode(self,val):
        if self.right is None:
            self.right=bnode(val)
        else:
            self.right.val=val
        return self

    def isEmpty(self):
        if self is None:
            return True
        else:
            return False
    
    def pre_traverse(self):
        if self is not None:  
            print self.val
            if self.left is not None:
                self.left.pre_traverse()
            if self.right is not None:
                self.right.pre_traverse()
            
    def mid_traverse(self):
        if self is not None:  
            if self.left is not None:
                self.left.mid_traverse()
            print self.val
            if self.right is not None:
                self.right.mid_traverse()
            
    def aft_traverse(self):
        if self is not None:  
            if self.left is not None:
                self.left.aft_traverse()
            if self.right is not None:
                self.right.aft_traverse()
            print self.val
            
    def DFS(self):
        pass
    def BFS(self):
        pass
    
def construct_Btree():
    s=raw_input('请输入结点')
    if s == '':
        return root
        #申请两个结点空间
    root=bnode(int(s))
    root.left=construct_Btree()
    root.right=construct_Btree()
     
# print partion([5,1,3,9,8,2,4,6,7,0], 0, 9,True)
# print quicksort([1,5,3,9,8,2,4,6,7,0])
# print small_k([1,5,3,9,8,2,4,6,7,0],3)
# print mid_num([1,5,3,9,8,2,4,6,7,0,11])
# print appear_once('lliiujjiann')
# print add(4,6)
# print fib(5)
# print matrix([[1,2,3] for i in range(3)],3,3)
# print number_of_1(6)
# print odd_even_list([6,3,2,5,1,4])

#初始二叉树
bhead=bnode(1)
bhead.insert_lnode(2)
bhead.insert_rnode(3)
bhead.left.insert_lnode(4)
bhead.left.insert_rnode(5)
bhead.right.insert_lnode(6)
bhead.right.insert_rnode(7) 

bhead.pre_traverse()
bhead.mid_traverse()
bhead.aft_traverse()


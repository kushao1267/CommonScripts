#coding=utf-8

#结构体
class Node(object):
    def __init__(self,x):
        self.val=x
        self.next=None


#链表操作
class opera(object):
    
    #初始化链表
    def init_list(self,init_list):
        list = [Node(i) for i in init_list]  #创建结点列表
        for i in range(len(list)-1):    #创建结点之间的联系
            list[i].next=list[i+1]
        return list[0]

    #插入结点
    def insert_node(self,head,position,node):
        num,rp,mp,num_mid=1,head,head,1
        while head.next is not None: #计数
            num+=1
            head=head.next
        if position >= num: #插尾
            head.next=node
            return rp
        elif position<0 or position==1: #插头
            rp.val,node.val = node.val,rp.val
            node.next ,rp.next= rp.next ,node
            return rp
        else:
            while num_mid!=position:    #插中间
                mp = mp.next
                num_mid+=1
            mp.next,node.next =node, mp.next
            mp.val ,node.val = node.val, mp.val
            return rp

    #删除结点
    def delete_node(self,head,position):
        num,rp=1,head
        while head is not None:
            if num==position:
                temp = head.next
                head.val,head.next = temp.val,temp.next
            head=head.next
            num+=1
        return rp    
        
    #遍历链表
    def traverse_print_list(self,head):
        if head is None:
            print ('null')
        list = []
        while head is not None:
            list.append(head.val)
            head=head.next
        print (list)

    #倒序遍历
    def reverse_print_list(self,head):
        if head is None:
            print ('null')
        list=[]
        while head is not None:
            list.append(head.val)
            head=head.next
        list.reverse()
        print (list)


    #链表长度
    def length_list(self,head):
        num=0
        while head is not None:
            head=head.next
            num+=1
        print (num)

    #合并两个有序链表：1排序法，2递归法
    def merge_list_bysort(self,head1,head2):
        if head1 is None:
            return head2
        if head2 is None:
            return head1
        #取出所有结点值
        list = []
        while head1 is not None:
            list.append(head1.val)
            head1 = head1.next
        while head2 is not None:
            list.append(head2.val)
            head2 = head2.next
        list.sort()
        #由list构建结构体组
        return self.init_list(list)
    
    def merge_list_byrecursion(self,head1,head2):
        if head1 is None:
            return head2
        if head2 is None:
            return head1   #这里的return用于给node.next赋值

        if head1.val <= head2.val:
            node = head1   #构建一个新指针，将后面的顺序
            node.next = self.merge_list_byrecursion(head1.next,head2)
        else:
            node = head2   #构建一个新指针，将后面的顺序
            node.next = self.merge_list_byrecursion(head1,head2.next)

        return node    #node为头指针,其他结点均在它后面，将它返回 
        
    #反转链表
    def reverse_list(self,head):
        if head is None or head.next is None:
            return head
        stack,rp,mp=[],head,head
        while head is not None:
            stack.append(head.val)
            head=head.next      
        for i in reversed(stack):
            mp.val = i
            mp = mp.next
        return rp  

    #找出两个链表的交点,'Y'型
    def find_joint(self,head1,head2):
        num1,num2,p1,p2=0,0,head1,head2
        while p1 is not None:
            p1=p1.next
            num1+=1
        while p2 is not None:
            p2=p2.next
            num2+=1
        gap,p11,p22 = abs(num1-num2),head1,head2
        if num1>num2:
            while gap>0:
                p11=p11.next
                gap-=1
        else:
            while gap>0:
                p22=p22.next
                gap-=1
        while p11 and p22 :
            if p11.val==p22.val:
                print (p11.val)
                break
            p11,p22=p11.next,p22.next
            
              
if __name__ == '__main__':
    OPERATION = opera()
    
    #test for insert
    '''
    node = OPERATION.init_list([0,1,2,3,4,5,6,7,8,9])
    OPERATION.insert_node(node,6,Node(100))
    OPERATION.traverse_print_list(node)
    OPERATION.reverse_print_list(node)'''
    #test for delete
    '''
    node = OPERATION.init_list([0,1,2,3,4,5,6,7,8,9])
    OPERATION.traverse_print_list(node)
    OPERATION.delete_node(node,6)
    OPERATION.traverse_print_list(node)'''
    #test for reverse
    '''
    print ('reverse it!')
    node = OPERATION.init_list([0,1,2,3,4,5,6,7,8,9])
    res = OPERATION.reverse_list(node)
    OPERATION.traverse_print_list(res)
    OPERATION.length_list(res)'''

    #test for merge
    '''
    print ('test for merge list')
    node1 = OPERATION.init_list([0,2,4,6,8])
    node2 = OPERATION.init_list([1,3,5,7,9])
    res = OPERATION.merge_list_byrecursion(node1,node2)
    OPERATION.traverse_print_list(res)'''
    #test for joint
    
    node1 = OPERATION.init_list([0,2,4,6,8,10,11,12,13])
    node2 = OPERATION.init_list([1,3,5])#交点在10
    p1,p2=node1,node2
    while p1.val!=10:   #在'10'处相连
        p1=p1.next
    while p2.next is not None:
        p2=p2.next
    p2.next = p1

    OPERATION.find_joint(node1,node2)
    #test for circle
    





    

#coding=utf-8
import sys

from random import random
from timeit import Timer

class Sort_method(object):
    '''
    不管插入还是选择都基于这样一个规律：数组分为两段，前段有序，后段无序。
    '''
    def __init__(self):
        pass
    
    def Quicksort(self,nums):
        if len(nums)<=1:#为空或只有一个元素时，返回它自身
            return nums #递归的中断条件
        small,big=[],[]
        flag = nums.pop()#去除最右边的元素做标杆
        for i in nums:
            if i<flag:
                small.append(i)
            else:
                big.append(i)
                #递归调用记得用self.func_name,只有list之间才可以用+, list+int是错误的。
        return self.Quicksort(small)+[flag]+self.Quicksort(big)
    
    '''
    改进的冒泡,添加flag标志: 当冒了x（x<n）个泡时，已经有序，则不继续比较
    '''
    def Bubblesort(self,nums):
        flag,i=True,0   #初始化为无序标志
        while i<len(nums)-1 and flag:     #长度为n的序列，只要n-1次就可以
            flag=False  #假如上次循环没有交换一次值，说明flag=False，是已有序序列
            j=len(nums)-1
            #其实和选择排序很像，每次前i个都是已经排序的,所以j必须大于i,
            #它的每一趟互相比较并且交换值把最小的放在前面
            #而选择排序只是扫描一遍记录最小的值下标，然后与前面的交换。
            #实际上不同就在于扫描一趟和交换一趟。
            while j>i :
                if nums[j]<nums[j-1]:
                    nums[j],nums[j-1]=nums[j-1],nums[j]
                    flag=True
                j-=1
            i+=1
        return nums

    '''
        选择序列最小值与第一个交换，选择剩下序列的最小值与第二个交换,以此类推....
    '''
    def Selectsort(self,nums):
        num_len = len(nums)
        for i in range(num_len-1):
            #-----------这段代码可以计算序列最小值-----------------
            min_index=i#此处把最小值的下标做一个标记
            for j in range(i+1,num_len):
                if nums[j]<nums[min_index]:
                   min_index = j
            if min_index!=i:#避免没必要的交换，其实这个判断也可以不用
                nums[min_index],nums[i]=nums[i],nums[min_index]
            #--------------------------------------------------  
        return nums 
    
    '''
    有一个已经有序的数据序列，要求在这个已经排好的数据序列中插入一个数， 
    但要求插入后此数据序列仍然有序。
    '''        
    def Insertsort(self,nums):#打麻将字牌
        a_len = len(nums)  
        for i in range(1,a_len):#i遍历待排序序列
            j=i-1               #j遍历已排序序列，且从右到左，每个元素都往后腾一个位置
            key=nums[i]         #记录下当前的i值
            while j>=0 and nums[j]>key:
                nums[j+1]=nums[j]
                j-=1
            nums[j+1]=key       #在适当位置插入元素
        return nums  
    
    def Merge(self ,nums, first, middle, last):  
    # 切片边界,左闭右开并且是了0为开始  
        lnums = nums[first:middle+1]   
        rnums = nums[middle+1:last+1]  
        lnums.append(sys.maxint)  
        rnums.append(sys.maxint)  
        l = 0  
        r = 0  
        for i in range(first, last+1):  
            if lnums[l] < rnums[r]:  
                nums[i] = lnums[l]  
                l+=1  
            else:  
                nums[i] = rnums[r]  
                r+=1       
    def Merge_sort(self, nums, first, last):  
        ''''' merge sort 
        merge_sort函数中传递的是下标，不是元素个数 
        '''  
        if first < last:  
            middle = (first + last)/2  
            self.Merge_sort(nums, first, middle)  
            self.Merge_sort(nums, middle+1, last)  
            self.Merge(nums, first, middle,last) 
        return nums
    
    def insertion_sort(self,A):
    #插入排序，作为桶排序的子排序
        n = len(A)
        if n <= 1:
            return A
        B = [] # 结果列表
        for a in A:
            i = len(B)
            while i > 0 and B[i-1] > a:
                i = i - 1
            B.insert(i, a);
        return B
    def bucket_sort(self,A):
        """桶排序，伪码如下：
        BUCKET-SORT(A)
        1  n ← length[A] // 桶数
        2  for i ← 1 to n
        3    do insert A[i] into list B[floor(nA[i])] // 将n个数分布到各个桶中
        4  for i ← 0 to n-1
        5    do sort list B[i] with insertion sort // 对各个桶中的数进行排序
        6  concatenate the lists B[0],B[1],...,B[n-1] together in order // 依次串联各桶中的元素
        桶排序假设输入由一个随机过程产生，该过程将元素均匀地分布在区间[0,1)上。
        """
        n = len(A)
        buckets = [[] for _ in xrange(n)] # n个空桶
        for a in A:
            buckets[int(n * a)].append(a)
        B = []
        for b in buckets:
            B.extend(self.insertion_sort(b))
        return B

if __name__=="__main__":
    sort = Sort_method()
    list = [3,5,1,6,9,0,7,3,2,6]
    print "原始序列：",list
    #调用快排
    #print "快排序列：",(sort.Quicksort(list))
    
    #快排改进
    
    #归并排序
    #print "归并序列：",sort.Merge_sort(list, 0, len(list)-1)
    
    #选择排序
    #print "选择序列：",(sort.Selectsort(list))
    
    #插入排序
    #print "插入序列：",(sort.Insertsort(list))
    
    #冒泡法
    #print "冒泡序列：",(sort.Bubblesort(list))       
        
    #桶排序
    #数据为0-1的随机小数，桶排序适合：已知范围的序列排序，！大数据，牺牲空间换时间:最好O（n），最差O(n+c),是稳定
    #items = [random() for _ in xrange(10000)]
    #print "桶序列：",sort.bucket_sort(items)
    
    #堆排序
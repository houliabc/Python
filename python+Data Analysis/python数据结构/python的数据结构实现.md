# python的数据结构实现

## 栈

```python
class Stack(object):
    def __init__(self, limit=10):
        self.stack = [] #存放元素
        self.limit = limit #栈容量极限
    def push(self, data): #判断栈是否溢出
        if len(self.stack) >= self.limit:
            print('StackOverflowError')
            pass
        self.stack.append(data)
    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            raise IndexError('pop from an empty stack') #空栈不能被弹出
    def peek(self): #查看堆栈的最上面的元素
        if self.stack:
            return self.stack[-1]
    def is_empty(self): #判断栈是否为空
        return not bool(self.stack)
    def size(self): #返回栈的大小
        return len(self.stack)
```

## 单链表

```python
class Node:  
    def __init__(self, data):
        self.data = data  
        self.next = None  
class Linked_List:
    def __init__(self):
        self.head = None
    def initlist(self,data_list):    #链表初始化函数
        self.head=Node(data_list[0])   #创建头结点
        temp=self.head
        for i in data_list[1:]: #逐个为 data 内的数据创建结点, 建立链表
            node=Node(i)
            temp.next=node
            temp=temp.next
    def is_empty(self):  #判断链表是否为空
        if self.head.next==None:
            print("Linked_list is empty")
            return True
        else:
            return False
    def get_length(self):  #获取链表的长度
        temp=self.head #临时变量指向队列头部
        length=0 #计算链表的长度变量
        while temp!=None:
            length=length+1
            temp=temp.next
        return length #返回链表的长度
    def insert(self,key,value): #链表插入数据函数
        if key<0 or key>self.get_length()-1:
            print("insert error")
        temp=self.head
        i=0
        while i<=key: #遍历找到索引值为 key 的结点后, 在其后面插入结点
            pre=temp
            temp=temp.next
            i=i+1
        node=Node(value)
        pre.next=node
        node.next=temp
    def print_list(self):   #遍历链表，并将元素依次打印出来
        print("linked_list:")
        temp=self.head
        new_list=[]
        while temp is not None:
            new_list.append(temp.data)
            temp=temp.next
        print(new_list)
    def remove(self,key):  #链表删除数据函数
        if key<0 or key>self.get_length()-1:
            print("insert error")
        i=0
        temp=self.head
        while temp !=None:  #遍历找到索引值为 key 的结点
            pre=temp
            temp=temp.next
            i=i+1
            if i==key:
                pre.next=temp.next
                temp=None
                return True
        pre.next=None
    def reverse(self): #将链表反转
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
```

## 双链表

```python
class Node(object):
    # 双向链表节点
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None
class DLinkList(object):
    # 双向链表
    def __init__(self):
        self._head = None
    def is_empty(self):
        # 判断链表是否为空
        return self._head == None
    def get_length(self):
        # 返回链表的长度
        cur = self._head
        count = 0
        while cur != None:
            count=count+1
            cur = cur.next
        return count
    def travel(self):
        # 遍历链表
        cur = self._head
        while cur != None:
            print(cur.item)
            cur = cur.next
        print("")
    def add(self, item):
        # 头部插入元素
        node = Node(item)
        if self.is_empty():
            # 如果是空链表，将_head指向node
            self._head = node
        else:
            # 将node的next指向_head的头节点
            node.next = self._head
            # 将_head的头节点的prev指向node
            self._head.prev = node
            # 将_head 指向node
            self._head = node
    def append(self, item):
        # 尾部插入元素
        node = Node(item)
        if self.is_empty():
            # 如果是空链表，将_head指向node
            self._head = node
        else:
            # 移动到链表尾部
            cur = self._head
            while cur.next != None:
                cur = cur.next
            # 将尾节点cur的next指向node
            cur.next = node
            # 将node的prev指向cur
            node.prev = cur
    def search(self, item):
        # 查找元素是否存在
        cur = self._head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False
    def insert(self, pos, item):
        # 在指定位置添加节点
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            node = Node(item)
            cur = self._head
            count = 0
            # 移动到指定位置的前一个位置
            while count < (pos-1):
                count += 1
                cur = cur.next
            # 将node的prev指向cur
            node.prev = cur
            # 将node的next指向cur的下一个节点
            node.next = cur.next
            # 将cur的下一个节点的prev指向node
            cur.next.prev = node
            # 将cur的next指向node
            cur.next = node
    def remove(self, item):
        # 删除元素
        if self.is_empty():
            return
        else:
            cur = self._head
            if cur.item == item:
                # 如果首节点的元素即是要删除的元素
                if cur.next == None:
                    # 如果链表只有这一个节点
                    self._head = None
                else:
                    # 将第二个节点的prev设置为None
                    cur.next.prev = None
                    # 将_head指向第二个节点
                    self._head = cur.next
                return
            while cur != None:
                if cur.item == item:
                    # 将cur的前一个节点的next指向cur的后一个节点
                    cur.prev.next = cur.next
                    # 将cur的后一个节点的prev指向cur的前一个节点
                    cur.next.prev = cur.prev
                    break
                cur = cur.next
```

## 队列（链表形式实现）

```python
class Node(object):
    def __init__(self,elem,next=None):
        self.elem = elem #表示对应的元素值
        self.next=next #表示下一个链接的链点
class Queue(object):
    def __init__(self):
        self.head = None #头部链点为 None
        self.rear = None #尾部链点为 None
    def is_empty(self):
        return self.head is None #判断队列是否为空
    def enqueue(self, elem):
        p = Node(elem) #初始化一个新的点
        if self.is_empty():
            self.head = p #队列头部为新的链点
            self.rear = p #队列尾部为新的链点
        else:
            self.rear.next = p #队列尾部的后继是这个新的点
            self.rear =p #然后让队列尾部指针指向这个新的点
    def dequeue(self):
        if self.is_empty(): #判断队列是否为空
            print('Queue_is_empty') #若队列为空，则退出 dequeue 操作
        else:
            result = self.head.elem #result为队列头部元素
            self.head = self.head.next #改变队列头部指针位置
            return result #返回队列头部元素
    def peek(self):
        if self.is_empty(): #判断队列是否为空
            print('NOT_FOUND') #为空则返回 NOT_FOUND
        else:
            return self.head.elem #返回队列头部元素
    def print_queue(self):
        print("queue:")
        temp=self.head
        myqueue=[] #暂时存放队列数据
        while temp is not None:
            myqueue.append(temp.elem)
            temp=temp.next
        print(myqueue)
```

## 队列（数组形式实现）

```python
class Queue():
    def __init__(self):
        self.entries = [] #表示队列内的参数
        self.length = 0 #表示队列的长度
        self.front=0 #表示队列头部位置
    def enqueue(self, item):
        self.entries.append(item) #添加元素到队列里面
        self.length = self.length + 1 #队列长度增加 1
    def dequeue(self):
        self.length = self.length - 1 #队列的长度减少 1
        dequeued = self.entries[self.front] #队首元素为dequeued
        self.front-=1 #队首的位置减少1
        self.entries = self.entries[self.front:] #队列的元素更新为退队之后的队列
        return dequeued
    def peek(self):
        return self.entries[0] #直接返回队列的队首元素
```

## 二叉树

```python
class Node(object):
    def __init__(self,item):
        self.item=item #表示对应的元素
        self.left=None #表示左节点
        self.right=None #表示右节点
    def __str__(self):
        return str(self.item)  #print 一个 Node 类时会打印 __str__ 的返回值
class Tree(object):
    def __init__(self):
        self.root=Node('root')  #根节点定义为 root 永不删除，作为哨兵使用。
    def add(self,item):
        node = Node(item)
        if self.root is None:  #如果二叉树为空，那么生成的二叉树最终为新插入树的点
            self.root = node
        else:
            q = [self.root] # 将q列表，添加二叉树的根节点
            while True:
                pop_node = q.pop(0)
                if pop_node.left is None: #左子树为空则将点添加到左子树
                    pop_node.left = node
                    return
                elif pop_node.right is None: #右子树为空则将点添加到右子树
                    pop_node.right = node
                    return
                else:
                    q.append(pop_node.left)
                    q.append(pop_node.right)
    def get_parent(self, item):
        if self.root.item == item:
            return None  # 根节点没有父节点
        tmp = [self.root] # 将tmp列表，添加二叉树的根节点
        while tmp:
            pop_node = tmp.pop(0)
            if pop_node.left and pop_node.left.item == item: #某点的左子树为寻找的点
                return pop_node #返回某点，即为寻找点的父节点
            if pop_node.right and pop_node.right.item == item: #某点的右子树为寻找的点
                return pop_node #返回某点，即为寻找点的父节点
            if pop_node.left is not None: #添加tmp 元素
                tmp.append(pop_node.left)
            if pop_node.right is not None:
                tmp.append(pop_node.right)
        return None
    def delete(self, item):
        if self.root is None:  # 如果根为空，就什么也不做
            return False

        parent = self.get_parent(item)
        if parent:
            del_node = parent.left if parent.left.item == item else parent.right  # 待删除节点
            if del_node.left is None:
                if parent.left.item == item:
                    parent.left = del_node.right
                else:
                    parent.right = del_node.right
                del del_node
                return True
            elif del_node.right is None:
                if parent.left.item == item:
                    parent.left = del_node.left
                else:
                    parent.right = del_node.left
                del del_node
                return True
            else:  # 左右子树都不为空
                tmp_pre = del_node
                tmp_next = del_node.right
                if tmp_next.left is None:
                    # 替代
                    tmp_pre.right = tmp_next.right
                    tmp_next.left = del_node.left
                    tmp_next.right = del_node.right

                else:
                    while tmp_next.left:  # 让tmp指向右子树的最后一个叶子
                        tmp_pre = tmp_next
                        tmp_next = tmp_next.left
                    # 替代
                    tmp_pre.left = tmp_next.right
                    tmp_next.left = del_node.left
                    tmp_next.right = del_node.right
                if parent.left.item == item:
                    parent.left = tmp_next
                else:
                    parent.right = tmp_next
                del del_node
                return True
        else:
            return False
```

## 字典树

```python
class TrieNode:
    def __init__(self):
        self.nodes = dict()  # 构建字典
        self.is_leaf = False
    def insert(self, word: str):  
        curr = self
        for char in word:
            if char not in curr.nodes:
                curr.nodes[char] = TrieNode()
            curr = curr.nodes[char]
        curr.is_leaf = True
    def insert_many(self, words: [str]):
        for word in words:
            self.insert(word)
    def search(self, word: str):
        curr = self
        for char in word:
            if char not in curr.nodes:
                return False
            curr = curr.nodes[char]
        return curr.is_leaf
```

## 堆

```python
class heap(object):
    def __init__(self):
        #初始化一个空堆，使用数组来在存放堆元素，节省存储
        self.data_list = []
    def get_parent_index(self,index):
        #返回父节点的下标
        if index == 0 or index > len(self.data_list) -1:
            return None
        else:
            return (index -1) >> 1
    def swap(self,index_a,index_b):
        #交换数组中的两个元素
        self.data_list[index_a],self.data_list[index_b] = self.data_list[index_b],self.data_list[index_a]
    def insert(self,data):
        #先把元素放在最后，然后从后往前依次堆化
        #这里以大顶堆为例，如果插入元素比父节点大，则交换，直到最后
        self.data_list.append(data)
        index = len(self.data_list) -1 
        parent = self.get_parent_index(index)
        #循环，直到该元素成为堆顶，或小于父节点（对于大顶堆) 
        while parent is not None and self.data_list[parent] < self.data_list[index]:
            #交换操作
            self.swap(parent,index)
            index = parent
            parent = self.get_parent_index(parent)
    def removeMax(self):
        #删除堆顶元素，然后将最后一个元素放在堆顶，再从上往下依次堆化
        remove_data = self.data_list[0]
        self.data_list[0] = self.data_list[-1]
        del self.data_list[-1]

        #堆化
        self.heapify(0)
        return remove_data
    def heapify(self,index):
        #从上往下堆化，从index 开始堆化操作 (大顶堆)
        total_index = len(self.data_list) -1
        while True:
            maxvalue_index = index
            if 2*index +1 <=  total_index and self.data_list[2*index +1] > self.data_list[maxvalue_index]:
                maxvalue_index = 2*index +1
            if 2*index +2 <=  total_index and self.data_list[2*index +2] > self.data_list[maxvalue_index]:
                maxvalue_index = 2*index +2
            if maxvalue_index == index:
                break
            self.swap(index,maxvalue_index)
            index = maxvalue_index
```
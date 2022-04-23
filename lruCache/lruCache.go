package main


type node struct {
    data int
    prev *node
    next *node
}

type doublyLinkedList struct {
    len int
    tail *node
    head *node
}

func initDoublyList() *doublyLinkedList {
    return &doublyLinkedList{}
}

func (d *doublyLinkedList) Size() int {
    return d.len
}


type LRUCache struct {

}


func Constructor(capacity int) LRUCache {

  // hashMap
  // double linked list
  // 

}


func (this *LRUCache) Get(key int) int {
    // 
    
}


func (this *LRUCache) Put(key int, value int)  {
    
}


/**
 * Your LRUCache object will be instantiated and called as such:
 * obj := Constructor(capacity);
 * param_1 := obj.Get(key);
 * obj.Put(key,value);
 */

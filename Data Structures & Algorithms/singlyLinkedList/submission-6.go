type LinkedList struct {
    Head int
    Tail int
    List []int
}

func NewLinkedList() *LinkedList {
    return &LinkedList{
        List: []int{},
    }
}

func (ll *LinkedList) Get(index int) int {
    if index >= 0 && index < len(ll.List) {
        val := ll.List[index]
        return val
    } else {
        return -1
    }
}

func (ll *LinkedList) InsertHead(val int) {
    ll.List = append([]int{val}, ll.List...)
}

func (ll *LinkedList) InsertTail(val int) {
    ll.List = append(ll.List, val)
}

func (ll *LinkedList) Remove(index int) bool {
    if index < 0 || index >= len(ll.List) {
        return false
    }

    ll.List = append(ll.List[:index], ll.List[index+1:]...)
    return true
}

func (ll *LinkedList) GetValues() []int {
    return ll.List
}

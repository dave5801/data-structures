/*Test class for linked list.*/

/*requirements*/
const SinglyLinkedList = require('./linked_list.js');

/*Tests*/

test('create new singly  list', () => {
    const l = new SinglyLinkedList();
    expect(l);
});


test('test push empty list', () =>{
    const l = new SinglyLinkedList();
    l.push(5);
    expect(l.head.data).toBe(5)
});

test('test push next', () => {
    const l = new SinglyLinkedList();
    l.push(5);
    l.push(9);
    expect(l.head.next.data).toBe(9)

});

test('test list accecpt iterable', () => {
    const l = new SinglyLinkedList([1,2,3,4,5]);
    expect(l.head.data).toBe(1)
});

test('test push to list',() => {
    const l = new SinglyLinkedList([1]);
    l.push(10);
    expect(l.head.data).toBe(1)
    expect(l.head.next.data).toBe(10)
});

test('test list size',() => {
    tl = [1,2,3,4,5]
    const l = new SinglyLinkedList(tl);
    expect(l.size).toBe(tl.length);
});

test('test remove from list',() => {
    tl = [1,2,3,4,5]
    const l = new SinglyLinkedList(tl);
    l.remove(l.head)
    expect(l.size).toBe(tl.length-1)
});

test('test pop from list',() => {
    tl = [1,2,3,4,5]
    const l = new SinglyLinkedList(tl);
    l.pop()
    l.pop()
    expect(l.head.data).toBe(3)
});

test('test search for node which is present in list',() => {
    tl = [1,2,3,4,5]
    const l = new SinglyLinkedList(tl);
    res = l.search(5)
    expect(res.data).toBe(5)
});

test('test search for node which is not present in list',() => {
    tl = [1,2,3,4,5]
    const l = new SinglyLinkedList(tl);
    res = l.search(10)
    expect(res).toBe("not found")
});
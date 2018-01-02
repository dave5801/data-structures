const SinglyLinkedList = require('./linked_list.js');

test('create new list', () => {
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
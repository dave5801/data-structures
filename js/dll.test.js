/*Test class for linked list.*/

/*requirements*/
const DLL = require('./dll.js');



test('create new doubly list', () => {
    const dll = new DLL();
    expect(dll);
});


test('test push empty list', () =>{
    const dll = new DLL();
    dll.push(5);
    expect(dll.head.data).toBe(5)
    expect(dll.tail.data).toBe(5)
});


test('test push tail is next', () => {
    const dll = new DLL();
    dll.push(5);
    dll.push(9);
    expect(dll.head.next.data).toBe(dll.tail.data)

});


test('test dll accecpt iterable', () => {
    const dll = new DLL([1,2,3,4,5]);
    expect(dll.head.data).toBe(5)
    expect(dll.tail.data).toBe(1)
});


test('test push to list',() => {
    const dll = new DLL([1,2,3,4,5]);
    dll.push(10);
    expect(dll.head.data).toBe(10)
    expect(dll.tail.data).toBe(1)
});


test('test dll len',() => {
    tl = [1,2,3,4,5]
    const dll = new DLL(tl);
    expect(dll.len()).toBe(tl.length);
});


test('test remove from dll',() => {
    tl = [1,2,3,4,5]
    const dll = new DLL(tl);
    dll.remove(dll.head)
    expect(dll.len()).toBe(tl.length)
});


test('test pop from list',() => {
    tl = [1,2,3,4,5]
    const dll = new DLL(tl);
    dll.pop()
    dll.pop()
    expect(dll.len()).toBe(3)
    expect(dll.head.data).toBe(3)
    expect(dll.tail.data).toBe(1)
});


test('test shift from empty list',() => {
    
    const dll = new DLL([]);
    var x = dll.shift()
    expect(x).toBe("Empty List")
    
});

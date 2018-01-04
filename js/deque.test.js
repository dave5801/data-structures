/*Test class for double ended queue.*/

/*requirements*/
const Deque = require('./deque.js');

test('test create new deque', () => {
    const dq = new Deque();
    expect(dq);
});

test('test size on empty deque', () => {
    const dq = new Deque();
    expect(dq.size()).toBe(0);
});

test('test size after append', () => {
    const dq = new Deque();
    dq.append(5)
    dq.append(6)
    dq.append(7)
    expect(dq.size()).toBe(3);
});

test('test size after append left', () => {
    const dq = new Deque();
    dq.append_left(5)
    dq.append_left(6)
    dq.append_left(7)
    expect(dq.size()).toBe(3);
});

test('test pop empty list', () => {
    const dq = new Deque();
    expect(dq.pop()).toBe("Cannot Pop from Empty List");
});

test('pop is as expected', () => {
    const dq = new Deque();
    dq.append(5)
    dq.append(6)
    dq.append(7)
    expect(dq.pop()).toBe(7);
});

test('pop left is as expected', () => {
    const dq = new Deque();
    dq.append(5)
    dq.append(6)
    dq.append(7)
    expect(dq.pop_left()).toBe(5);
});

test('pop and pop left size values are expected', () => {
    const dq = new Deque();
    dq.append(10)
    dq.append_left(9)
    dq.append(200)
    expect(dq.pop()).toBe(200);
    expect(dq.pop_left()).toBe(9);
});

test('test peek method', () => {
    const dq = new Deque();
    dq.append_left(10)
    dq.append_left(9)
    dq.append(200)
    expect(dq.peek()).toBe(200);
});

test('test peek left method', () => {
    const dq = new Deque();
    dq.append_left(10)
    dq.append_left(9)
    dq.append(200)
    expect(dq.peek_left()).toBe(9);
});
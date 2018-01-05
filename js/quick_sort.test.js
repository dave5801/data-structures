/*tests for quick sort*/

var quick_sort = require('./quick_sort.js')

test('test quicksort', () => {
    ql = [5,4,3,2,1]
    expect(quick_sort(ql)).toEqual([1,2,3,4,5]);
});

test('test quicksort empty list', () => {

    expect(quick_sort([])).toEqual([]);
});

test('test quicksort list length 1', () => {

    expect(quick_sort([1])).toEqual([1]);
});
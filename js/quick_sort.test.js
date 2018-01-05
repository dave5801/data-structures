var quick_sort = require('./quick_sort.js')

test('test quicksort', () => {
    ql = [5,4,3,2,1]
    expect(quick_sort(ql)).toEqual([1,2,3,4,5]);
});
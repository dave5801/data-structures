//quick sort method.

var quick_sort = function(unsorted){

    if(unsorted.length <= 1){
        return unsorted
    }

    let pivot = unsorted.pop()
    let left = []
    let right = []
    let sorted = []

    for(let i = 0; i < unsorted.length; i++){
        if(unsorted[i] <= pivot){
            left.push(unsorted[i])
        }else if(unsorted[i] > pivot){
            right.push(unsorted[i])
        }
    }
    return sorted.concat(quick_sort(left), pivot, quick_sort(right));
}

unsorted = [10,7,4,200,6,8,5,28]


console.log(quick_sort(unsorted))

module.exports = quick_sort;

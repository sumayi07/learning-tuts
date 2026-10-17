// day 12

// level 1

let string = "The position of some particles on the horizontal x-axis -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers and find the distance between the two furthest particles."
const nums = string.match(/-?\d+/g)

console.log(nums)
console.log(Math.max(...nums) - Math.min(...nums))

// level 2

paragraph = `I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.`

const tenMostFrequentWords = (paragraph) => {

    allWords = paragraph.match(/[a-z]+/gi)
    freqMap = new Map()

    for (const word of allWords) {
        const key = word.toLowerCase()
        freqMap.set(key, (freqMap.get(key) || 0) + 1)
    }

    return [...freqMap.entries()].sort((a, b) => b[1] - a[1]).slice(0, 10)
}

console.log(tenMostFrequentWords(paragraph))

// level 3

string = `%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?`
const cleanText = string.replace(/[!#$%&@;]/g, "")
console.log(cleanText)
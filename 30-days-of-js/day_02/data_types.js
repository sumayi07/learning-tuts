// day 2

//level 1 exercises

let challenge = "30 days of JavaScript"
console.log(challenge)
console.log(challenge.length)
challenge.toUpperCase
challenge.toLowerCase
console.log(challenge.substring(0, 2))
console.log(challenge.substring(2))
console.log(challenge.includes("Script"))
challenge_array = challenge.split()

tech = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(",")

console.log(challenge.replace("JavaScript", "Python"))
console.log(challenge)

console.log(challenge.charAt(15))
console.log(challenge.charCodeAt("J"))

console.log(challenge.match("a"))

console.log("30 Days of ".concat("JavaScript"))
console.log("30 Days of" + "JavaScript")
console.log(challenge.repeat(5))

// level 2 exercises

console.log("The quote 'There is no exercise better for the heart than reaching down and lifting people up.' by John Holmes teaches us to help one another.")
console.log("python".includes("on") && "jargon".includes("on"))
console.log(Math.floor(Math.random() * 101))
console.log("JavaScript"[Math.floor(Math.random() * 10)])

// level 3 exercises

const sentence = 'You cannot end a sentence with because because because is a conjunction';

// Use /because/g to find all matches globally
const becauseCount = (sentence.match(/because/g) || []).length;
console.log(becauseCount);

const sentence2 = '%I \$am@% a %tea@cher%, &and& I lo%#ve %te@a@ching%;. The@re \$is no@th@ing; &as& mo@re rewarding as educa@ting &and& @emp%o@weri@ng peo@ple. ;I found tea@ching m%o@re interesting tha@n any ot#her %jo@bs. %Do@es thi%s mo@tiv#ate yo@u to be a tea@cher!? %Th#is 30#Days&OfJavaScript &is al@so \(the\)resu@lt of &love& of tea&ching';

const cleanedText = sentence2.replace(/[%\$@&#;!?]/g, '');
console.log(cleanedText); 


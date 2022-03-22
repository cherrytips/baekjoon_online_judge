var fs = require('fs');
var input = fs.readFileSync('1001/dev/stdin').toString().split(' ');

let a = input[0].toString();
let b = input[1].toString();

console.log(a - b);

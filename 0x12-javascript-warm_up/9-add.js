#!/usr/bin/node
if (isNaN(process.argv[2]) || isNaN(process.argv[3])) {
	console.log('NaN');
}
else {
	add(Number(process.argv[2]), Number(process.argv[3]));
}

function add(a, b) {
	const c = a + b;
	console.log(c);
}

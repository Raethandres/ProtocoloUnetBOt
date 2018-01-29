var fs = require('fs');

fs.readFile('file.json', 'utf8', function (err, data) {
    console.log(data)
    console.log("\n")
    var obj = JSON.parse(data);
    console.log(obj)
});
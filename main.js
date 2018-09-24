const fs = require('fs')
const esprima = require('esprima')
// const escodegen = require('escodegen')

function read (filename) {
  fs.readFile(filename, 'utf8', (err, content) => {
    if (err) throw Error('Error while reading file')
    let code = esprima.parseModule(content)
    console.log(JSON.stringify(code))
  })
}

function getOption (name) {
  let args = process.argv
  for (let i = 3; i < args.length; i++) {
    let [n, value] = args[i].slice(2).split('=')
    if (n === name) return value
  }
  return null
}

const mode = process.argv[2]
switch (mode) {
  case 'read':
    let file = getOption('file')
    if (file !== null) read(file)
    break
  default:
    throw Error('Invalid option')
}

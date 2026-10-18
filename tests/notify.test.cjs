const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const source = fs.readFileSync(require('node:path').join(__dirname,'../api/notify.js'),'utf8');
test('a general contact message does not require a booking topic', async()=>{
 const handler = new Function('process','fetch',source.replace('export default async function handler','return async function handler'))({env:{}},()=>{throw Error('No external requests expected');});
 let status=200,body;
 const res={setHeader(){},status(n){status=n;return this;},json(v){body=v;return this;}};
 await handler({method:'POST',headers:{origin:'https://spontaneouscafe.com','content-type':'application/json'},body:{name:'Test',email:'test@example.org',message:'Hello'}},res);
 assert.equal(status,200);assert.equal(body.ok,true);
});

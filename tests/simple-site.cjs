// Entirely local browser checks. No inquiry or analytics requests leave the test.
const { chromium } = require('playwright');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
(async () => {
 const browser = await chromium.launch({headless:true,channel:'chrome'});
 try {
  for (const width of [375,768,1440]) {
   const context = await browser.newContext({viewport:{width,height:900}});
   const page = await context.newPage(); const errors=[]; const missing=[];
   page.on('pageerror',e=>errors.push(e.message));
   await context.route('**/*',r=>{
    const u=new URL(r.request().url());
    if(u.hostname!=='spontaneouscafe.com')return r.abort();
    const f=path.join(__dirname,'../dist',u.pathname.endsWith('/')?u.pathname+'index.html':u.pathname);
    if(!fs.existsSync(f)){missing.push(u.pathname);return r.fulfill({status:404,body:''});}
    return r.fulfill({path:f});
   });
   await page.goto('https://spontaneouscafe.com/');
   await page.locator('[data-consent="denied"]').click();
   if(width<=900){
    assert.equal(await page.locator('#nav').isVisible(),false);
    await page.locator('.nav-toggle').click();
    assert.equal(await page.locator('#nav').isVisible(),true);
    await page.keyboard.press('Escape');
    await page.locator('#nav').waitFor({state:'hidden'});
    assert.equal(await page.locator('#nav').isVisible(),false);
   }
   for(const slug of ['', 'foraging/','private-chef/','catering/','cooking-classes/','about/','gallery/','contact/','privacy/','404.html']){
    await page.goto('https://spontaneouscafe.com/'+slug);
    await page.evaluate(async()=>{for(const img of document.images){if(!img.getAttribute('src'))continue;img.loading='eager';await img.decode();}});
    assert.equal(await page.locator('h1').count(),1,slug+' title');
    assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth),false,slug+' overflow');
    assert.equal(await page.locator('video').count(),0);
    if(['','foraging/','contact/','about/','gallery/'].includes(slug))await page.screenshot({path:'/tmp/cafe-simple-'+(slug.replace('/','')||'home')+'-'+width+'.png',fullPage:true});
   }
   for (const slug of ['private-chef','catering','foraging']) {
    await page.goto('https://spontaneouscafe.com/'+slug+'/');
    const tabs=page.getByRole('tab');
    assert.equal(await tabs.count(),4,slug+' seasonal options');
    for(let i=0;i<4;i++) {
     await tabs.nth(i).click();
     assert.equal(await page.getByRole('tabpanel').count(),1,slug+' single visible season');
     assert.equal(await tabs.nth(i).getAttribute('aria-selected'),'true');
    }
    await page.keyboard.press('Home');
    assert.equal(await tabs.first().getAttribute('aria-selected'),'true');
   }
   assert.deepEqual(errors,[]);assert.deepEqual(missing,[]);
   console.log('PASS all pages, assets, navigation and overflow:',width);
   await context.close();
  }
  const context=await browser.newContext({javaScriptEnabled:false,viewport:{width:375,height:800}});
  const page=await context.newPage();
  await page.route('**/*',r=>{const u=new URL(r.request().url());const f=path.join(__dirname,'../dist',u.pathname.endsWith('/')?u.pathname+'index.html':u.pathname);return fs.existsSync(f)?r.fulfill({path:f}):r.abort();});
  await page.goto('https://spontaneouscafe.com/');
  assert.equal(await page.locator('#nav').isVisible(),true);
  console.log('PASS navigation without JavaScript');await context.close();
 }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exit(1);});

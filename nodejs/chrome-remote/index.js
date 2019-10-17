const CDP = require('chrome-remote-interface');
const R = require("rambdax")
const robot = require("robotjs");

const main = async () => {
  const url = 'https://www.youtube.com/watch?v=-lEhWfucJMs&list=RD-lEhWfucJMs&start_radio=1';
  // const url = 'http://localhost:8888/test.html';
  const client = await CDP({port: 9222})
// Extract used DevTools domains.
  const {Page, Runtime, Input, Target} = client;
// Enable events on domains we are interested in.
  await Page.enable()
  const target = await Target.createTarget({url:'https://www.baidu.com'})
  console.log(target)
  await R.delay(1000)
  const atttarget = await Target.attachToTarget({targetId:target})
  console.log(atttarget)
  //await R.delay(1000)
  console.log('naviagete')
  Page.navigate({url: url});
// Evaluate outerHTML after page has loaded.
  Page.loadEventFired(async () => {
    Runtime.evaluate({expression: 'document.body.outerHTML'}).then((result) => {
      //client.close();
    });
    await R.delay(5000)
    Input.dispatchKeyEvent({type: 'keyDown', code: 'KeyF',key:'f'}).then((result) => {
      console.log(result);
    });
    Input.dispatchKeyEvent({type: 'keyUp', code: 'KeyF',key:'f'}).then((result) => {
      console.log(result);
    });
    const targets = await Target.getTargets()
    console.log(targets)
    await R.delay(5000)
    client.close();
  });
}
const main1 = async () => {
  const list = await CDP.List()
  await CDP.Activate({'id': list[2].id})
  return list
}
const main2 = async () => {
  // Speed up the mouse.
  robot.setMouseDelay(2);

  var twoPI = Math.PI * 2.0;
  var screenSize = robot.getScreenSize();
  var height = (screenSize.height / 2) - 10;
  var width = screenSize.width;

  for (var x = 0; x < width; x++) {
    var y = height * Math.sin((twoPI * x) / width) + height;
    robot.moveMouse(x, y);
  }
}
const main3 = async () => {
  await R.delay(5000);
  // Type "Hello World".
  robot.typeString("Hello World");

// Press enter.
  robot.keyTap("enter");
}
const main4 = async () => {
  await R.delay(3000);
  // Press enter.
  robot.keyTap("right",['command','alt']);
  //robot.keyTap("right",'command');
}
main4().then(console.log)

// For authoring Nightwatch tests, see
// http://nightwatchjs.org/guide#usage

module.exports = {
  'input test': function (browser) {
    const targetPage = browser.page.testTargetPage()
    
    targetPage.navigate()
      .assert.visible('@inputData')
      .setValue('@inputData', 'test')
      .send()
      .assert.value('@resultData', 'test')
    
    browser.end()
  } 
}

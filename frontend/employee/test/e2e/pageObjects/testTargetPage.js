const pageCommands = {
    send: function () {
        return this.waitForElementVisible('@sendButton', 1000)
            .click('@sendButton') 
    }
}
// PageObject内でCommandを定義する方法がわからん
// これがあった方が、同じロジックを何度も書かなくてよいので使いたい
// this.apiや、this.waitForElementVisibleを参照できない
// 確かにそう見えるのだが…公式のSampleはこう書いてある、なにか設定が足りない
// https://github.com/nightwatchjs/nightwatch/issues/1629
// これと同事象だった。nightwatchのsrc_foldersと同じ階層下に、
// PageObjectを指定してはいけないらしい

module.exports = {
    commands: [pageCommands],
    url: function () {
        return this.api.globals.devServerURL
    },
    elements: {
        inputData: {
            selector: 'input[name=inputData]'
        },
        sendButton: {
            selector: 'input[type=button]'
        },
        resultData: {
            selector: 'input[name=resultData]'
        }
    }
}
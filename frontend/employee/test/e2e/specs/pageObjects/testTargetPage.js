// const pageCommands = {
//     send: function () {
//         this.api.pause(1000)
//         return this.waitForElementVisible('@sendButton', 1000)
//             .click('@sendButton') 
//     }
// }

module.exports = {
    url: function () {
        return this.api.globals.devServerURL
    },
    // commands: [pageCommands],
    elements: {
        inputData: {
            selector: 'input[name=inputData]'
        },
        sendButton: {
            selector: 'input[type="button"]'
        },
        resultData: {
            selector: 'input[name=resultData]'
        }
    }
}
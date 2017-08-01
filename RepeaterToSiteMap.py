from burp import IBurpExtender
from burp import IHttpListener
from burp import IBurpExtenderCallbacks

class BurpExtender(IBurpExtender, IHttpListener, IBurpExtenderCallbacks):

    def registerExtenderCallbacks( self, callbacks):
        self._helpers = callbacks.getHelpers()

        self._callbacks = callbacks

        # set our extension name
        callbacks.setExtensionName("Repeater to Sitemap")
        callbacks.registerHttpListener(self)
        return

    '''
    void processHttpMessage(int toolFlag,
            boolean messageIsRequest,
            IHttpRequestResponse messageInfo);
    '''
    def  processHttpMessage(self, toolFlag, messageIsRequest, messageInfo):
        if toolFlag == 64: #Repeater
            if messageIsRequest == False:
                self._callbacks.addToSiteMap(messageInfo)


# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    TC746()
    
@stepResult(descriptionMsg=u"교과 > 스틸컷, 채널명, 프로그레스바, 프로그램명, 편성시간, 시청률 확인")       
def TC746():
    
    #탭4개 제공 : 실시간채널 / 초등 / 중등 / 고등
    HELP_TEXT = ("imageView1","imgChLogo","textProgramName","textProgramTime","prgbChannel","textRating")
    for searchingObj in HELP_TEXT: 
            
        rc, result = DEV1.UIWaitForName(searchingObj, 5000)
        if rc != AT_SUCCESS:
            System.Debug(u"Fail to UIWaitForName")
            return rc
        
    return AT_SUCCESS
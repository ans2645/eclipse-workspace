# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    TC742()
    
@stepResult(descriptionMsg=u"교과 > 서브메뉴를 확인.(서버편성에 따라 달라질 수 있음)")       
def TC742():
    #탭4개 제공 : 실시간채널 / 초등 / 중등 / 고등
    HELP_TEXT = (u"고등",u"중등",u"초등")
    for searchingObj in HELP_TEXT: 
            
        rc, result = DEV1.UIWaitForText(searchingObj, 500)
        if rc != AT_SUCCESS:
            System.Debug(u"Fail to UIWaitForName")
            return rc
        
    return AT_SUCCESS
             



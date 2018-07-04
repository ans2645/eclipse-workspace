# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    TC743()
    
@stepResult(descriptionMsg=u"교과 > 교과 진입 시 실시간채널 탭 화면 표시되는지 확인")       
def TC743():
    rc, result = DEV1.UIWaitForText(u'실시간채널', 5000)
    if rc != AT_SUCCESS:
        System.Debug(u"Fail to UIWaitForName")
        return rc
    
    return AT_SUCCESS
    
    
    
    
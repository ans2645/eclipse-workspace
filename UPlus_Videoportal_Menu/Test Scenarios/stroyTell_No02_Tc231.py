# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    TC231()
    
@stepResult(descriptionMsg=u"영상카드 > 스토리텔링 홈화면 타이틀 영역에 비디오LTE 홈버튼과 스토리텔링 타이틀 노출")
def TC231():
    #영상카드 찾기 
    rc = DEV1.CheckVideoCardMenuSubHomeShown()
    if rc != AT_SUCCESS:
        return rc
    return AT_SUCCESS
    
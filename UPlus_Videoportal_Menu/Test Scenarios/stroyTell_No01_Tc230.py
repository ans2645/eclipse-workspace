# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    DEV1.StopApp()
    TC230()
    
@stepResult(descriptionMsg=u"영상카드 > 진입 > 메인화면에서 스토리텔링 메뉴를 선택하여 스토리텔링 화면으로 진입")
def TC230():
    rc = DEV1.ClearAppData()
    if rc != AT_SUCCESS:
        return rc
    
    rc = DEV1.LauchApp()
    if rc != AT_SUCCESS:
        return rc
    
    rc = DEV1.ClearAppDataAgree()
    if rc != AT_SUCCESS:
        return rc
    
    rc = DEV1.CheckMainDisplayLoaded()
    if rc != AT_SUCCESS:
        return rc
    
    System.Sleep(1000) 
    
    rc = DEV1.CheckMoreMenuShown()
    if rc != AT_SUCCESS:
        return rc
    
    rc = DEV1.ClickMoreMenu()
    if rc != AT_SUCCESS:
        return rc
    
    rc = DEV1.CheckMenuEditShown()
    if rc != AT_SUCCESS:
        return rc
    
    rc = DEV1.ClickVideoCardMenu()
    if rc != AT_SUCCESS:
        return rc
    
    
    return AT_SUCCESS
    
# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    DEV1.StopApp()
    TC573()
    
@stepResult(descriptionMsg=u"해외시리즈 > 최신,인기 > 홈 버튼, 해당 페이지의 타이틀, 검색 버튼, GNB 버튼 확인")       
def TC573():
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
    
    #더보기 나타났는지 확인
    rc = DEV1.CheckMoreMenuShown()
    if rc != AT_SUCCESS:
        return rc
    
    #더보기 클릭
    rc = DEV1.ClickMoreMenu()
    if rc != AT_SUCCESS:
        return rc
    
    rc = DEV1.ClickForeignDramaMenu()
    if rc != AT_SUCCESS:
        return rc
    
    rc = DEV1.CheckForeignDramaMenuSubHomeShown()
    if rc != AT_SUCCESS:
        return rc  
    
    SERISES_TV = ("btn_gotomain", "tv_title", "btn_search", "btn_menu")        
    
    #튜플 이용해 실시간TV 상단에 홈버튼, 검색  , GNB 있는지 확인
    for searchingObj in SERISES_TV: 
        rc, result = DEV1.UIWaitForName(searchingObj, 500)
        
        if rc != AT_SUCCESS:
            System.Debug(u"Fail to UIWaitForName")
            return rc
             
        if result == False:
            System.Debug(u"Failed to find the object : "+searchingObj)
            return AT_NOT_FOUND
    
    return AT_SUCCESS
    
    
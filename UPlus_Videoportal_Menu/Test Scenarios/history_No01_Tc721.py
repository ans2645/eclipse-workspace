# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    DEV1.StopApp()
    TC721_722()
    
    
@stepResult(descriptionMsg=u"역사 > 홈 버튼, 타이틀, 검색, GNB 버튼")       
def TC721_722():
    
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
    
    #더보기 나타났는지
    rc = DEV1.CheckMoreMenuShown()
    if rc != AT_SUCCESS:
        return rc
    
    #더보기 클릭
    rc = DEV1.ClickMoreMenu()
    if rc != AT_SUCCESS:
        return rc 
    
    #인물/경영 진입
    rc = DEV1.ClickHistoryVideoMenu()
    if rc != AT_SUCCESS:
        return rc
    
    #인문/경영 찾기 
    rc = DEV1.CheckHistoryVideoMenuSubHomeShown()
    if rc != AT_SUCCESS:
        return rc
    
    SPORTS_TV = ("btn_gotomain", "tv_title", "btn_search", "btn_menu")        
    
    #튜플 이용해 실시간TV 상단에 홈버튼, 검색  , GNB 있는지 확인
    for searchingObj in SPORTS_TV: 
        rc, result = DEV1.UIWaitForName(searchingObj, 500)
        
        if rc != AT_SUCCESS:
            System.Debug(u"Fail to UIWaitForName")
            return rc
             
        if result == False:
            System.Debug(u"Failed to find the object : "+searchingObj)
            return AT_NOT_FOUND
    
    System.Sleep(3000)
    
    
    DEV1.KeyPressByAlias('back,back') 
    #닫기 나타났는지
    rc = DEV1.CheckMenuCloseShown()
    if rc != AT_SUCCESS:
        return rc
    
    #닫기 클릭
    rc = DEV1.ClickMenuClose()
    if rc != AT_SUCCESS:
        return rc   
    
        
        
    return AT_SUCCESS
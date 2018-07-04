# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    DEV1.StopApp()
    TC207()
    
@stepResult(descriptionMsg=u"대박영상 > default 화면  > 오늘의 화제 > 오늘의 화제 화면 스크롤시 지면에 편성된 동영상 외 고정 표시되는지 확인")       
def TC207():
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
    
    
    #대박영상 메뉴 클릭
    rc = DEV1.ClickDaebakVideoMenu()
    if rc != AT_SUCCESS:
        return rc
    
    
    #대박영상 메뉴 진입 확인
    rc = DEV1.CheckDaebakVideoMenuSubHomeShown()
    if rc != AT_SUCCESS:
        return rc  
    
    rc, result = DEV1.UIWaitForText(u"오늘의 화제", 5000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 오브젝트가 나타났는지 확인
        return AT_NOT_FOUND
    
    rc = DEV1.UIClickByText(u"오늘의 화제")
    if rc != AT_SUCCESS:
        return rc
    
    rc, result = DEV1.UIWaitForName("rlAutoPlayLayout", 5000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 오브젝트가 나타났는지 확인
        return AT_NOT_FOUND
    
    return AT_SUCCESS
    
    
    
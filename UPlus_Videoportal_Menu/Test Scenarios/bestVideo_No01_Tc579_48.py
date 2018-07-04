# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    DEV1.StopApp()
    TC579_48()
    
@stepResult(descriptionMsg=u"대박영상 > 진입 > 홈 / 오늘의 대박 / BEST / 장르별 / 테마추천 확인 - 좌/우 Swipe 또는 tab 영역 선택으로 tab 이동")       
def TC579_48():
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
    
    rc, result = DEV1.UIWaitForText(u"장르별", 5000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 오브젝트가 나타났는지 확인
        return AT_NOT_FOUND
    
    rc = DEV1.UIClickByText(u"장르별")
    if rc != AT_SUCCESS:
        return rc
    
    rc, result = DEV1.UIWaitForText(u"테마추천", 5000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 오브젝트가 나타났는지 확인
        return AT_NOT_FOUND
    
    
    rc = DEV1.UIClickByText(u"테마추천")
    if rc != AT_SUCCESS:
        return rc
    
    
    return AT_SUCCESS
    
    
    
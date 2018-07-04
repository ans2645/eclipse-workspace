# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    DEV1.StopApp()
    TC584()
    
@stepResult(descriptionMsg=u"대박영상 > 진입 > 홈 / 오늘의 대박 / BEST / 장르별 / 테마추천 확인 - 좌/우 Swipe 또는 tab 영역 선택으로 tab 이동")       
def TC584():
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
    
    #대박영상 메뉴 클릭
    rc = DEV1.ClickDaebakVideoMenu()
    if rc != AT_SUCCESS:
        return rc
    
    
    #대박영상 메뉴 진입 확인
    rc = DEV1.CheckDaebakVideoMenuSubHomeShown()
    if rc != AT_SUCCESS:
        return rc  
    
    rc = DEV1.UIClickByText(u"장르별")
    if rc != AT_SUCCESS:
        return rc
    
    
    rc = DEV1.UIClickByText(u"테마추천")
    if rc != AT_SUCCESS:
        return rc
    
    
    #영상스틸컷
    rc, result = DEV1.UIGetObjectByTypeIndex("avwImageView", 9004)
    if rc != AT_SUCCESS:
        System.Finish(ExecutionResult.T_FAILED, rc)
        
    #재생시간
    rc, result = DEV1.UIGetObjectByTypeIndex("avwStaticText", 9011)
    if rc != AT_SUCCESS:
        System.Finish(ExecutionResult.T_FAILED, rc)
        
        
    #제목
    rc, result = DEV1.UIGetObjectByTypeIndex("avwStaticText", 9012)
    if rc != AT_SUCCESS:
        System.Finish(ExecutionResult.T_FAILED, rc)
        
    #조회수
    rc, result = DEV1.UIGetObjectByTypeIndex("avwStaticText", 9013)
    if rc != AT_SUCCESS:
        System.Finish(ExecutionResult.T_FAILED, rc)
        
    
        
    return AT_SUCCESS
    
    
    
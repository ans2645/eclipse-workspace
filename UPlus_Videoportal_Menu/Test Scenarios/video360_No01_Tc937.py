# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    DEV1.StopApp()
    TC937()
    
@stepResult(descriptionMsg=u"360도 영상 > 메인화면 내 360도 컨텐츠 배너 또는 메뉴를 선택 시 360도 컨텐츠 페이지로 이동되어 관련 리스트 화면이 정상적으로 표시되는지 확인한다.")       
def TC937():
    rc = DEV1.ClearAppData()
    if rc != AT_SUCCESS:
        return rc
    
    rc = DEV1.LauchApp()
    if rc != AT_SUCCESS:
        return rc
    
    rc = DEV1.ClearAppDataAgree()
    if rc != AT_SUCCESS:
        return rc
    
    System.Sleep(3000)
    
    rc = DEV1.CheckMainDisplayLoaded()
    if rc != AT_SUCCESS:
        return rc
    
    
    #더보기 나타났는지
    rc = DEV1.CheckMoreMenuShown()
    if rc != AT_SUCCESS:
        return rc
    
    #더보기 클릭
    rc = DEV1.ClickMoreMenu()
    if rc != AT_SUCCESS:
        return rc 
    
    System.Sleep(3000)
    
    #360도 영상
    rc = DEV1.Click360VideoMenu()
    if rc != AT_SUCCESS:
        return rc
    
    System.Sleep(3000)
    
    #360도 영상 찾기 
    rc = DEV1.Check360VideoMenuSubHomeShown()
    if rc != AT_SUCCESS:
        return rc
    
    return AT_SUCCESS

    
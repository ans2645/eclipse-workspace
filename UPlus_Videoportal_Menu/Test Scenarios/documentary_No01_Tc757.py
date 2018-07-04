# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    DEV1.StopApp()
    TC757()
    
@stepResult(descriptionMsg=u"다큐 > 인기 > 리스트를 확인- 포스터, 제목 / - 포스터 선택 시 상세페이지로 이동")       
def TC757():
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
    
    #다큐 진입
    rc = DEV1.ClickDocuMenu()
    if rc != AT_SUCCESS:
        return rc
    
    
    #명품다큐 찾기 
    rc = DEV1.CheckDocuMenuSubHomeShown()
    if rc != AT_SUCCESS:
        return rc
    
    #제목
    rc, result = DEV1.UIWaitForName("title", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 오브젝트가 나타났는지 확인
        return AT_NOT_FOUND
    
    #포스터
    rc, result = DEV1.UIWaitForName("poster", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 오브젝트가 나타났는지 확인
        return AT_NOT_FOUND
    
    #포스터 클릭
    rc = DEV1.UIClickByTypeIndex('avwImageView', 9001)
    if rc != AT_SUCCESS:
        return rc
    
    
    DEV1.KeyPressByAlias('back,back')
    
    return AT_SUCCESS
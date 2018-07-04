# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    DEV1.StopApp()
    TC1888_632_633_635_636()
    
@stepResult(descriptionMsg=u"애니 > 테마추천 > 리스트 영역을 확인 , 각 테마의 컨텐츠 영역을 확인 ,제공된 테마의 타이틀이 제공되는지 확인 ")       
def TC1888_632_633_635_636():
    
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
    
    #애니 메뉴 클릭
    rc = DEV1.ClickAniMenu()
    if rc != AT_SUCCESS:
        return rc
    
    #애니 메뉴 진입 확인
    rc = DEV1.CheckAniMenuSubHomeShown()
    if rc != AT_SUCCESS:
        return rc   
    
    result = False
    for i in range(0,5):
        rc = DEV1.ScrollRight("avwObject", 9001)
        if rc != AT_SUCCESS:
            System.Finish(ExecutionResult.T_FAILED, rc)
            
        searchingText = u"애니월정액"
        rc, result = DEV1.UIWaitForText(searchingText, 2000, 0, UITarget.TopWindow)
        if rc != AT_SUCCESS:
            System.Debug(u"Failed to UIWaitForText")
            return rc
        
        if result == True:
            break
        
    if result == False:
        System.Debug(u"Failed to find the text : "+searchingText)
        return AT_NOT_FOUND
    
    #찾으면 클릭
    rc = DEV1.UIClickByText(u"애니월정액")
    if rc != AT_SUCCESS:
        return rc
    
    HELP_TEXT = (u"NEW/HOT",u"추리/판타지",u"순정/코믹",u"SF/액션", u"19+")
    
    for searchingObj in HELP_TEXT: 
            
        rc, result = DEV1.UIWaitForText(searchingObj, 500)
        
        if rc != AT_SUCCESS:
            System.Debug(u"Fail to UIWaitForName")
            return rc
             
        if result == False:
            System.Debug(u"Failed to find the object : "+searchingObj)
            return AT_NOT_FOUND
        #텍스트 찾기
        rc = DEV1.UIClickByText(searchingObj)
        if rc != AT_SUCCESS:
            return rc
        
        System.Sleep(2000)
        
        #- 선택한 하위 카테고리의 리스트 제공
        #- 포스터, 제목
        rc, result = DEV1.UIWaitForName("title", 3000)
        if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
            return rc
        
        if result == False:   # 오브젝트가 나타났는지 확인
            return AT_NOT_FOUND
        
        rc, result = DEV1.UIWaitForName("poster", 3000)
        if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
            return rc
        
        if result == False:   # 오브젝트가 나타났는지 확인
            return AT_NOT_FOUND
        
        rc = DEV1.ScrollUp("avwSubWindow", 9000)
        if rc != AT_SUCCESS:
            System.Finish(ExecutionResult.T_FAILED, rc)
        
        #- 포스터 선택 시 상세페이지로 이동
        #- 하위 카테고리 선택 시 해당 리스트 제공
        #상세화면 클릭
        rc = DEV1.UIClickByTypeIndex('avwSubWindow', 9038)
        if rc != AT_SUCCESS:
            return rc
        
        System.Sleep(3000)
        
        DEV1.KeyPressByAlias('back')
        
        System.Sleep(2000)
        
        #- 리스트 영역 내 상하 flicking 스크롤 제공
        for i in range(0,2):
            rc = DEV1.ScrollDown("avwSubWindow", 9000)
            if rc != AT_SUCCESS:
                System.Finish(ExecutionResult.T_FAILED, rc)
            
        for i in range(0,2):   
            rc = DEV1.ScrollUp("avwSubWindow", 9000)
            if rc != AT_SUCCESS:
                System.Finish(ExecutionResult.T_FAILED, rc)

    return AT_SUCCESS

    
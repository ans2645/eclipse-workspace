# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    DEV1.StopApp()
    TC558()
    
@stepResult(descriptionMsg=u"영화 > 최신,인기 > 콘텐츠 리스트에 포스터와 영화 제목 노출 - 리스트 영역에서 상/하 Flicking으로 스크롤 가능- Tap 시 영화 상세페이지로 이동")       
def TC558():
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
    #최신영화 진입
    rc = DEV1.ClickNewMovieMenu()
    if rc != AT_SUCCESS:
        return rc
    
    #영화 텍스트 찾기 
    rc = DEV1.CheckNewMovieMenuSubHomeShown()
    if rc != AT_SUCCESS:
        return rc
    
    
    #최신작 탭 찾기
    result = False
    for i in range(0,3):
        rc = DEV1.ScrollLeft("avwObject", 9001)
        if rc != AT_SUCCESS:
            System.Finish(ExecutionResult.T_FAILED, rc)
            
        searchingText = u"인기"
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
    rc = DEV1.UIClickByText(u"인기")
    if rc != AT_SUCCESS:
        return rc
    
    
    for i in range(0,3):
        #스크롤다운 해보기
        rc = DEV1.ScrollDown("avwSubWindow", 9001)
        if rc != AT_SUCCESS:
            return rc 
    
    
    #영화 선택 
    rc = DEV1.UIClickByTypeIndex('avwSubWindow', 9033)
    if rc != AT_SUCCESS:
        return rc
    
    
    rc, result = DEV1.UIWaitForName("backBtn", 5000)
    if rc != AT_SUCCESS:
        return rc
    
    if result == False:
        return AT_NOT_FOUND
    
    #찾으면 클릭
    rc = DEV1.UIClickByName("backBtn")
    if rc != AT_SUCCESS:
        return rc
    
           
    rc, result = DEV1.UIWaitForText(u"최신작", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 텍스트가 나타났는지 확인
        return AT_NOT_FOUND
    
    #찾으면 클릭
    rc = DEV1.UIClickByText(u"최신작")
    if rc != AT_SUCCESS:
        return rc
    
    
    rc, result = DEV1.UIWaitForName("layout_poster", 5000)
    if rc != AT_SUCCESS:
        return rc
    
    if result == False:
        return AT_NOT_FOUND
    
    
    
    #영화 선택 
    rc = DEV1.UIClickByTypeIndex('avwImageView', 9007)
    if rc != AT_SUCCESS:
        return rc
    
    
    rc, result = DEV1.UIWaitForName("backBtn", 5000)
    if rc != AT_SUCCESS:
        return rc
    
    if result == False:
        return AT_NOT_FOUND
    
    #찾으면 클릭
    rc = DEV1.UIClickByName("backBtn")
    if rc != AT_SUCCESS:
        return rc
    
    
    
    System.Sleep(3000)
    
    for i in range(0,3):
        #스크롤다운 해보기 
        rc = DEV1.ScrollDown("avwSubWindow", 9001)
        if rc != AT_SUCCESS:
            return rc
       
    
    return AT_SUCCESS
    
    
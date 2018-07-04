# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    TC575()
    
@stepResult(descriptionMsg=u"해외시리즈 > 최신,인기 > 리스트")       
def TC575():
#- 포스터, 제목
#- 포스터 선택 시 해당 상세페이지로 이동
    #인기 탭 찾기
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
    
    System.Sleep(3000)
    
    #포스터있는지 확인
    rc, result = DEV1.UIWaitForName("poster", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 오브젝트가 나타났는지 확인
        return AT_NOT_FOUND
    
    #제목 있는지 확인
    rc, result = DEV1.UIWaitForName("title", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 오브젝트가 나타났는지 확인
        return AT_NOT_FOUND
    
    #포스터 클릭
    rc = DEV1.UIClickByTypeIndex('avwSubWindow', 9020)
    if rc != AT_SUCCESS:
        return rc
    
    System.Sleep(3000)
    
    
    rc, result = DEV1.UIWaitForName("backBtn", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 오브젝트가 나타났는지 확인
        return AT_NOT_FOUND
    
    
    rc = DEV1.UIClickByName('backBtn')
    if rc != AT_SUCCESS:
        return rc
    
    System.Sleep(3000)
#- 리스트 상하 flicking으로 스크롤 가능 확인
    for i in range(0,6):
        rc = DEV1.ScrollDown("avwSubWindow", 9001)
        if rc != AT_SUCCESS:
            System.Finish(ExecutionResult.T_FAILED, rc)
    
    
    for i in range(0,6):
        rc = DEV1.ScrollUp("avwSubWindow", 9001)
        if rc != AT_SUCCESS:
            System.Finish(ExecutionResult.T_FAILED, rc)
    
    return AT_SUCCESS
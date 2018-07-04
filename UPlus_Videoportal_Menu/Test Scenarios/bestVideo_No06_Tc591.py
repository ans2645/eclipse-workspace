# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    TC591()
    
@stepResult(descriptionMsg=u"대박영상 > 테마추천 > 제공 섹션의 타이틀, 더보기 버튼 제공 확인- 더보기 버튼 : tap 시 컨텐츠 List 화면으로 전환")       
def TC591():
    rc = DEV1.ScrollUp("avwScrollView", 9000)
    if rc != AT_SUCCESS:
        System.Finish(ExecutionResult.T_FAILED, rc)
    
    #더보기 확인
    rc, result = DEV1.UIWaitForName("paper_more", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 오브젝트가 나타났는지 확인
        return AT_NOT_FOUND
    
    #더보기 클릭
    rc = DEV1.UIClickByText(u'더보기')
    if rc != AT_SUCCESS:
        return rc
    
    return AT_SUCCESS
    
    
    
    
    
    
    
    
    
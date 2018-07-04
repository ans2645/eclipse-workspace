# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    TC939()
    
@stepResult(descriptionMsg=u"360도 영상 > 360도 컨텐츠 최초 진입 시 스트리밍 분당 용량 안내화면 제공. 닫기 버튼 눌러 사라지며, 이후 재생시 노출안됨")       
def TC939():
    
    #360도 컨텐츠 진입
    rc = DEV1.UIClickByTypeIndex('avwSubWindow', 9022)
    if rc != AT_SUCCESS:
        return rc
    
    #재생하기 버튼 클릭
    rc, result = DEV1.UIWaitForName("quickViewLayout", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 오브젝트가 나타났는지 확인
        return AT_NOT_FOUND
    
    #재생하기 있는지 확인
    rc = DEV1.UIClickByName('quickViewLayout')
    if rc != AT_SUCCESS:
        return rc
    
    
    
    System.Sleep(3000)
    
    DEV1.KeyPressByAlias('back,back')
 
    
    return AT_SUCCESS
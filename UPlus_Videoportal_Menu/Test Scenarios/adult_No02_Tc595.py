# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    TC595()
    
@stepResult(descriptionMsg=u"19금 > 최신 > 포스터, 제목 정보 제공하는지 확인- 포스터 선택 시 상세페이지로 이동")       
def TC595():
    #포스터 제공 
    rc, result = DEV1.UIWaitForName("poster", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 오브젝트가 나타났는지 확인
        return AT_NOT_FOUND
    #제목 제공
    rc, result = DEV1.UIWaitForName("title", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 오브젝트가 나타났는지 확인
        return AT_NOT_FOUND
    
    #포스터 클릭
    rc = DEV1.UIClickByTypeIndex('avwSubWindow', 9020)
    if rc != AT_SUCCESS:
        return rc
    
    DEV1.KeyPressByAlias('back')
    
    return AT_SUCCESS
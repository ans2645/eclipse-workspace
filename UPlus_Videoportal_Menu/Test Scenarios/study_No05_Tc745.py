# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    TC745()
    
@stepResult(descriptionMsg=u"교과 > 편성표, 멀티뷰, 새로고침 버튼 확인")       
def TC745():
    
    #편성표 name 있는지 확인
    rc, result = DEV1.UIWaitForName("imgProgramTable", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 오브젝트가 나타났는지 확인
        return AT_NOT_FOUND
    
    #멀티뷰 name : imgMultiView
    rc, result = DEV1.UIWaitForName("imgMultiView", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 오브젝트가 나타났는지 확인
        return AT_NOT_FOUND
    
    #새로고침 name : imgRefresh
    rc, result = DEV1.UIWaitForName("imgRefresh", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 오브젝트가 나타났는지 확인
        return AT_NOT_FOUND
    
    return AT_SUCCESS
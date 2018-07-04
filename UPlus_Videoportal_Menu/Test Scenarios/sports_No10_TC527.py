# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    TC527()
    
@stepResult(descriptionMsg=u"스포츠 > 골프  > 정렬버튼 > 정렬 버튼 선택시 동작 확인 (정렬 버튼은 서버 편성에 따라 노출/비노출 될 수 있음)")
def TC527():
    #정렬버튼 찾기
    rc, result = DEV1.UIWaitForName("btnSortCurront", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 오브젝트가 나타났는지 확인
        return AT_NOT_FOUND
    
    #정렬버튼 눌러보기
    rc = DEV1.UIClickByName('btnSortCurront')
    if rc != AT_SUCCESS:
        return rc
    
    rc, result = DEV1.UIWaitForName("llTopLayout", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 오브젝트가 나타났는지 확인
        return AT_NOT_FOUND
    
    return AT_SUCCESS
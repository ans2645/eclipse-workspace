# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    TC582()
    
@stepResult(descriptionMsg=u"대박영상 > 오늘의 대박 > 찜하기 > 찜 완료 토스트 팝업 제공 마이메뉴에서 확인 가능")       
def TC582():
    #찜하기
    rc, result = DEV1.UIGetObjectByTypeIndex("avwImageView", 9005)
    if rc != AT_SUCCESS:
        System.Finish(ExecutionResult.T_FAILED, rc)
    
    #찜하기 클릭    
    rc = DEV1.UIClickByName('item_jjim')
    if rc != AT_SUCCESS:
        return rc
    
    
    return AT_SUCCESS

# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    TC563_564()
    
@stepResult(descriptionMsg=u"영화 > 장르별 > 스크롤 영역 안에서 리스트 상/ 하 flicking으로 스크롤 가능")       
def TC563_564():
    #영화 포스터 선택시 상세페이지로 이동
    rc = DEV1.UIClickByTypeIndex('avwSubWindow', 9043)
    if rc != AT_SUCCESS:
        return rc
    
    #스크롤 내려보기 
    rc = DEV1.ScrollDown("avwSubWindow", 9002)
    if rc != AT_SUCCESS:
        System.Finish(ExecutionResult.T_FAILED, rc)  
        
    
    #뒤로가기 
    DEV1.KeyPressByAlias('back')
    
    return AT_SUCCESS
        
    
    
    
    
    
    
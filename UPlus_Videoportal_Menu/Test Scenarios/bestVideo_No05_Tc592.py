# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    TC592()
    
@stepResult(descriptionMsg=u"대박영상 > 테마추천 >  테마추천 테마별 리스트")       
def TC592():
    
    rc, result = DEV1.UIWaitForText(u"테마추천", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 오브젝트가 나타났는지 확인
        return AT_NOT_FOUND
    
    #테마추천 클릭
    rc = DEV1.UIClickByText(u"테마추천")
    if rc != AT_SUCCESS:
        return rc
    
    #타이틀 확인
    rc, result = DEV1.UIWaitForName("tvPaperTitleTypeIconText", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 오브젝트가 나타났는지 확인
        return AT_NOT_FOUND

#(서버편성에 따라 보여짐)
#- 표시 정보 : 영상스틸컷 / 제목 / 재생시간 / 조회수
   #스틸컷
    rc, result = DEV1.UIGetObjectByTypeIndex("avwImageView", 9004)
    if rc != AT_SUCCESS:
        System.Finish(ExecutionResult.T_FAILED, rc)
    #재생시간 찾기    
    rc, result = DEV1.UIGetObjectByTypeIndex("avwStaticText", 9011)
    if rc != AT_SUCCESS:
        System.Finish(ExecutionResult.T_FAILED, rc)
        
    #제목 찾기   
    rc, result = DEV1.UIGetObjectByTypeIndex("avwStaticText", 9012)
    if rc != AT_SUCCESS:
        System.Finish(ExecutionResult.T_FAILED, rc)
     
    #조회수
    rc, result = DEV1.UIGetObjectByTypeIndex("avwImageView", 9013)
    if rc != AT_SUCCESS:
        System.Finish(ExecutionResult.T_FAILED, rc)
   
    System.Sleep(2000)   
    #- 영상 스틸컷 : tap 시 해당 상세 페이지로 이동
    """
    #스틸컷 클릭
    rc = DEV1.UIClickByTypeIndex('avwSubWindow', 9032)
    if rc != AT_SUCCESS:
        return rc
     
    data_char = u"데이터 요금안내"
    if  data_char == u"데이터 요금안내":
        rc = DEV1.UIClickByText(u"확인")
        if rc != AT_SUCCESS:
            return rc
    
    System.Sleep(4000) 
    
    
    DEV1.KeyPressByAlias('back')
    """

    
    return AT_SUCCESS

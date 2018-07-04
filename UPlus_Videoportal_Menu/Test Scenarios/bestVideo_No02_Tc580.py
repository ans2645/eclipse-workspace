# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    TC580()
    
@stepResult(descriptionMsg=u"대박영상 > 오늘의 대박 > 영상 스틸컷 / 재생시간 / 제목 / 조회수 / 공유 버튼 / 찜하기 버튼 기능 및 정보 확인")       
def TC580():
    
#- 상/ 하 flicking 시 리스트 스크롤 되며, 최 하단에 도달 시 추가 리스트가 있는 경우 자동으로 불러옴 (추가 로딩 30개씩)
    
    rc, result = DEV1.UIWaitForText(u"최신", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 텍스트가 나타났는지 확인
        return AT_NOT_FOUND
    
    #최신 클릭
    rc = DEV1.UIClickByText(u"최신")
    if rc != AT_SUCCESS:
        return rc
    
    
    #스틸컷
    rc, result = DEV1.UIGetObjectByTypeIndex("avwImageView", 9002)
    if rc != AT_SUCCESS:
        System.Finish(ExecutionResult.T_FAILED, rc)
    #재생시간 찾기    
    rc, result = DEV1.UIGetObjectByTypeIndex("avwStaticText", 9010)
    if rc != AT_SUCCESS:
        System.Finish(ExecutionResult.T_FAILED, rc)
        
    #하이라이트명 찾기   
    rc, result = DEV1.UIGetObjectByTypeIndex("avwStaticText", 9006)
    if rc != AT_SUCCESS:
        System.Finish(ExecutionResult.T_FAILED, rc)
     
    #공유하기
    rc, result = DEV1.UIGetObjectByTypeIndex("avwImageView", 9004)
    if rc != AT_SUCCESS:
        System.Finish(ExecutionResult.T_FAILED, rc)
    #찜
    rc, result = DEV1.UIGetObjectByTypeIndex("avwImageView", 9005)
    if rc != AT_SUCCESS:
        System.Finish(ExecutionResult.T_FAILED, rc)
        
    #조회수찾기
    rc, result = DEV1.UIGetObjectByTypeIndex("avwSubWindow", 9019)
    if rc != AT_SUCCESS:
        System.Finish(ExecutionResult.T_FAILED, rc)
        
    """for i in range(0,5):
        rc = DEV1.ScrollDown("avwSubWindow", 9004)
        if rc != AT_SUCCESS:
            System.Finish(ExecutionResult.T_FAILED, rc)
            
    for i in range(0,5):
        rc = DEV1.ScrollUp("avwSubWindow", 9004)
        if rc != AT_SUCCESS:
            System.Finish(ExecutionResult.T_FAILED, rc)
    """
        
        
#- 리스트 : tap 시 해당 url 로 이동"
    rc = DEV1.UIClickByTypeIndex('avwSubWindow', 9042)
    if rc != AT_SUCCESS:
        return rc
    
    data_char = u"데이터 요금안내"
    if  data_char == u"데이터 요금안내":
        rc = DEV1.UIClickByText(u"확인")
        if rc != AT_SUCCESS:
            return rc
    
    System.Sleep(15000)

    DEV1.KeyPressByAlias('back')
    
    return AT_SUCCESS

#13 + 8
    


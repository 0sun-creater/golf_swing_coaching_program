# Project : GOlF SWING COACHING PROGRAM
## Team name : ladybug


**Activity, Data, Network, layout folder from Android**

**GUI, icon, python from our program**

-------
### 작동 순서
     1. 안드로이드 어플에서 회원가입을 한다. 사용자 데이터는 DB에 저장된다.
     
     
     
     2. 시스템에서 로그인을 한다. (비회원 진행 불가능)
     
     3. 화면에 intro 영상과 함께 버튼을 눌러달라는 메세지가 깜빡거린다.
     
     4. 발로 버튼을 밟으면 5초의 카운트 다운 후 swing을 한다.
     
     5. 카메라 (정면, 측면) 두 대로 사용자를 촬영한다.
     
     6. 영상을 받아 OpenPose 데이터를 실시간으로 얻어낸다.
     
     7. 파이썬으로 분석한다.
        이때 시스템 화면에는 Loding ... 이 떠있다.
        
     8. 피드백 데이터를 다시 시스템에 돌려준다.
     
     9. 시스템에서는 세 개의 버튼이 뜬다.
        하나는 피드백 되어야 하는 부분을 영상에 마커 표시를 하여 보여준다.
        하나는 4구간으로 분할하여 피드백을 보여준다.
        하나는 프로 선수와 영상을 비교하여 보여준다. 골반 선, 척추 선, 헤드 위치 등이 영상에 그려진다.
        
        
        
     10. 선이 표시된 영상은 AWS 서버로 보내진다.
     
     11. AWS에서 영상과 이미지는 S3에 저장되고 아이디와 찍힌 날짜 등이 DB에 저장된다.
     
     
     
     12. 안드로이드에서 로그인 후 어플을 이용할 수 있다.
     
     13. 첫 화면에서는 인기글과 유튜브 추천 영상이 보여진다. 클릭 시 이동한다. 
         아래는 메뉴바가 있다.
         
     14. 두 번째 메뉴화면에서는 이전에 내가 친 영상들을 피드백과 함께 다시 볼 수 있다.
     
     15. 세 번째 메뉴화면에서는 커뮤니티가 구현되어있다. 
         공지사항과 사람들이 올린 게시글을 볼 수 있다. 댓글 기능 또한 추가
         
     16. 네 번째 메뉴화면에서는 회원정보 수정, 문의하기, 버전 확인, 회원 탈퇴, 로그아웃 이 가능하다.
    


----
### 사용한 라이브러리
      * OpenPose 
         오픈포즈의 라이센스가 스포츠에는 사용하지 못하도록 되어 있으므로 상용화하는 데에 번거로움이 있음
         
      * YOLO v3
         약 6000장의 골프채를 학습 시켜서 좋은 결과를 얻었으나, 분석하는 데에 쓰진 않았음

### 사용한 소프트웨어

      * Python
         - 분석 프로그램
         - 시스템 GUI
         
      * Android Studio
          - 유튜브 추천영상, 내 영상 다시보기
          - 커뮤니티, 인기글, 회원정보, 문의하기, 버전확인 
          
      * Unity
          - 시스템 GUI intro 영상 생성
          
      * AWS Server (EC2,C3 사용)
          - Python & DB 연동
          - Android & DB 연동
          
      * MySQL Workbench
          - 유저 정보, 지난 영상, 커뮤니티 저장용도
          
      * Photoshop
          - gif 파일 생성
          - background 이미지 생성

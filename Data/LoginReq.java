package com.example.ladybug.Data;

import com.google.gson.annotations.SerializedName;


//로그인 요청시 보낼 데이터
public class LoginReq {
    //" " 안의 이름은 객체를 직렬화 및 역직렬화 할 때 이름으로 사용됨
    //JSON에서 " "으로 표출됨
    @SerializedName("user_id")
    private String user_id;

    @SerializedName("user_pwd")
    private String user_pwd;

    public LoginReq(String user_id, String user_pwd){
        this.user_id = user_id;
        this.user_pwd = user_pwd;
    }
}



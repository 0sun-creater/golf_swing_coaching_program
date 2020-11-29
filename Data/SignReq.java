package com.example.ladybug.Data;

import com.google.gson.annotations.SerializedName;

//회원가입 요청시 보낼 데이터
public class SignReq {

    @SerializedName("user_id")
    private String user_id;

    @SerializedName("user_pwd")
    private String user_pwd;

    @SerializedName("gender")
    private int gender;

    @SerializedName("tall")
    private String tall;

    @SerializedName("weight")
    private int weight;


    public SignReq(String user_id, String user_pwd, String tall, int weight, int gender){
        this.user_id = user_id;
        this.user_pwd = user_pwd;
        this.tall = tall;
        this.weight = weight;
        this.gender = gender;
    }
}

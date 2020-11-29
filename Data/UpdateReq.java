package com.example.ladybug.Data;

import com.google.gson.annotations.SerializedName;


public class UpdateReq {
    //" " 안의 이름은 객체를 직렬화 및 역직렬화 할 때 이름으로 사용됨
    //JSON에서 " "으로 표출됨
    @SerializedName("user_pwd")
    private String user_pwd;

    @SerializedName("tall")
    private String tall;

    @SerializedName("weight")
    private int weight;

    @SerializedName("gender")
    private int gender;

    @SerializedName("user_id")
    private String user_id;

    public UpdateReq(String user_pwd, String tall, int weight, int gender, String user_id){
        this.user_pwd = user_pwd;
        this.tall = tall;
        this.weight = weight;
        this.gender = gender;
        this.user_id = user_id;
    }
}


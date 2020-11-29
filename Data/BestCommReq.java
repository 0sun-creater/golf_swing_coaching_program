package com.example.ladybug.Data;

import com.google.gson.annotations.SerializedName;

public class BestCommReq {
    @SerializedName("user_id")
    private String user_id;


    public BestCommReq(String user_id){
        this.user_id = user_id;
    }
}
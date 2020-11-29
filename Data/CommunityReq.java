package com.example.ladybug.Data;

import com.google.gson.annotations.SerializedName;

public class CommunityReq {
    @SerializedName("user_id")
    private String user_id;


    public CommunityReq(String user_id){
        this.user_id = user_id;
    }
}


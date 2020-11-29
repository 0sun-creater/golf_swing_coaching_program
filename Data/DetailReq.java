package com.example.ladybug.Data;

import com.google.gson.annotations.SerializedName;

public class DetailReq {
    @SerializedName("community_num")
    private int community_num;


    public DetailReq(int community_num){
        this.community_num = community_num;
    }
}

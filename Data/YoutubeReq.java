package com.example.ladybug.Data;

import com.google.gson.annotations.SerializedName;

public class YoutubeReq {

    @SerializedName("r_value1")
    private int r_value1;

    public YoutubeReq(int r_value1){
        this.r_value1 = r_value1;
    }
}

package com.example.ladybug.Data;

import com.google.gson.annotations.SerializedName;

public class YoutubeRes {

    @SerializedName("url1")
    private String url1;

    @SerializedName("code")
    private  int code;

    @SerializedName("message")
    private  String message;


    public int getCode() { return code; }

    public String getMessage(){ return message; }

    public String getUrl1() { return url1; }

}

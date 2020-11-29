package com.example.ladybug.Data;

import com.google.gson.annotations.SerializedName;

public class CommunityRes {

    @SerializedName("code")
    private int code;

    @SerializedName("message")
    private String message;

    @SerializedName("size")
    private int size;

    @SerializedName("title")
    private String[] title;

    @SerializedName("community_num")
    private String[] community_num;


    public int getCode(){ return code;}
    public String getMessage(){
        return message;
    }
    public int getSize() { return size; }
    public String[] getTitle() {return title;}
    public String[] getCommunity_num() {return community_num;}



}
package com.example.ladybug.Data;

import com.google.gson.annotations.SerializedName;

public class BestCommRes {
    @SerializedName("bestComm")
    private String bestComm;

    @SerializedName("bestCnt")
    private String bestCnt;

    @SerializedName("secondComm")
    private String secondComm;

    @SerializedName("secondCnt")
    private String secondCnt;

    @SerializedName("code")
    private int code;

    @SerializedName("message")
    private String message;

    public int getCode(){
        return code;
    }

    public String getMessage(){
        return message;
    }

    public String getBestComm() { return bestComm; }

    public String getBestCnt(){ return bestCnt; }

    public String getSecondComm() { return secondComm; }

    public String getSecondCnt() { return secondCnt; }

}

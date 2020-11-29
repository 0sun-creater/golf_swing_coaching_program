package com.example.ladybug.Data;

import com.google.gson.annotations.SerializedName;

public class ShowBestCommRes {
    @SerializedName("code")
    private int code;

    @SerializedName("message")
    private String message;

    @SerializedName("best_user_id")
    private String best_user_id;

    @SerializedName("best_content")
    private String best_content;

    @SerializedName("best_title")
    private String best_title;

    @SerializedName("second_user_id")
    private String second_user_id;

    @SerializedName("second_content")
    private String second_content;

    @SerializedName("second_title")
    private String second_title;

    public int getCode(){
        return code;
    }
    public String getMessage() { return message; }
    public String getBest_user_id() { return best_user_id; }
    public String getBest_content() { return best_content; }
    public String getBest_title() { return best_title; }
    public String getSecond_user_id() { return second_user_id; }
    public String getSecond_content() { return second_content; }
    public String getSecond_title() { return second_title; }
}

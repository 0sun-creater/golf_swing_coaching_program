package com.example.ladybug.Data;

import com.google.gson.annotations.SerializedName;

public class DetailRes {

    @SerializedName("code")
    private int code;

    @SerializedName("message")
    private String message;

    @SerializedName("size")
    private int size;

    @SerializedName("title")
    private String title;

    @SerializedName("content")
    private String content;

    @SerializedName("command")
    private String[] command;


    public int getCode(){ return code;}
    public String getMessage(){ return message; }
    public String getTitle() {return title;}
    public String getContent() {return content;}
    public String[] getCommand() {return command; }
    public int getSize() {return size;}



}
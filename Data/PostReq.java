package com.example.ladybug.Data;

import com.google.gson.annotations.SerializedName;

public class PostReq {
    @SerializedName("user_id")
    private String user_id;

    @SerializedName("title")
    private String title;

    @SerializedName("content")
    private String content;

    public PostReq(String user_id, String title, String content)
    {
        this.user_id = user_id;
        this.title=title;
        this.content=content;
    }
}

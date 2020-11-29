package com.example.ladybug.Data;

import com.google.gson.annotations.SerializedName;

// code, message, video URL, video Date, video Location 얻기
public class VideoRes {

    @SerializedName("code")
    private int code;

    @SerializedName("message")
    private String message;

    @SerializedName("video_name")
    private String[] video_name;

    @SerializedName("image_name")
    private String[] image_name;

    @SerializedName("video_date")
    private String[] video_date;

    @SerializedName("video_location")
    private String[] video_location;

    @SerializedName("size")
    private int size;

    public int getCode(){
        return code;
    }

    public String getMessage(){
        return message;
    }

    public String[] getVideo_name()  { return video_name; }

    public String[] getImage_name()  { return image_name; }

    public String[] getVideo_date()  { return video_date; }

    public String[] getVideo_location()  { return video_location; }

    public int getSize() { return size; }

}

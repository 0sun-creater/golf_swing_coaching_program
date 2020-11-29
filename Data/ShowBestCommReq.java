package com.example.ladybug.Data;

import com.google.gson.annotations.SerializedName;

public class ShowBestCommReq {

    @SerializedName("best_comm")
    private String best_comm;

    @SerializedName("second_comm")
    private String second_comm;


    public ShowBestCommReq(String best_comm, String second_comm){
        this.best_comm = best_comm;
        this.second_comm = second_comm;
    }
}

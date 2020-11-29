package com.example.ladybug.network;

import com.example.ladybug.Data.BestCommReq;
import com.example.ladybug.Data.BestCommRes;
import com.example.ladybug.Data.CommandReq;
import com.example.ladybug.Data.CommandRes;
import com.example.ladybug.Data.CommunityReq;
import com.example.ladybug.Data.CommunityRes;
import com.example.ladybug.Data.DeleteReq;
import com.example.ladybug.Data.DeleteRes;
import com.example.ladybug.Data.DetailReq;
import com.example.ladybug.Data.DetailRes;
import com.example.ladybug.Data.PostReq;
import com.example.ladybug.Data.PostRes;
import com.example.ladybug.Data.ShowBestCommReq;
import com.example.ladybug.Data.ShowBestCommRes;
import com.example.ladybug.Data.SignReq;
import com.example.ladybug.Data.SignRes;
import com.example.ladybug.Data.LoginReq;
import com.example.ladybug.Data.LoginRes;
import com.example.ladybug.Data.UpdateReq;
import com.example.ladybug.Data.UpdateRes;
import com.example.ladybug.Data.VideoRes;
import com.example.ladybug.Data.VideoReq;
import com.example.ladybug.Data.YoutubeReq;
import com.example.ladybug.Data.YoutubeRes;

import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.POST;


public interface ServiceApi {
    @POST("/user/login")
    Call<LoginRes> userLogin(@Body LoginReq Data);
    @POST("/user/sign")
    Call<SignRes> userSign(@Body SignReq Data);
    @POST("/user/video")
    Call<VideoRes> userVideo(@Body VideoReq Data);
    @POST("/user/delete")
    Call<DeleteRes> userDelete(@Body DeleteReq Data);
    @POST("/user/bestcomm")
    Call<BestCommRes> homeComm(@Body BestCommReq Data);
    @POST("/user/showbestcomm")
    Call<ShowBestCommRes> showHomeComm(@Body ShowBestCommReq Data);
    @POST("/user/showYoutube")
    Call<YoutubeRes> homeYoutube(@Body YoutubeReq Data);
    @POST("/user/community")
    Call<CommunityRes> userCommunity(@Body CommunityReq Data);
    @POST("/user/update_data")
    Call<UpdateRes> userUpdate(@Body UpdateReq Data);
    @POST("/user/detail")
    Call<DetailRes> userDetail(@Body DetailReq Data);
    @POST("/user/posting")
    Call<PostRes> userPosting(@Body PostReq Data);
    @POST("/user/command")
    Call<CommandRes> userCommand(@Body CommandReq Data);

}

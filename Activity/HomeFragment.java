package com.example.ladybug.Activity;

import android.content.Context;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;

import androidx.fragment.app.Fragment;

import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageButton;
import android.widget.TextView;
import android.widget.Toast;

import com.example.ladybug.Data.BestCommReq;
import com.example.ladybug.Data.BestCommRes;
import com.example.ladybug.Data.ShowBestCommReq;
import com.example.ladybug.Data.ShowBestCommRes;
import com.example.ladybug.Data.YoutubeReq;
import com.example.ladybug.Data.YoutubeRes;
import com.example.ladybug.R;
import com.example.ladybug.network.RetrofitClient;
import com.example.ladybug.network.ServiceApi;


import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

import static android.widget.Toast.LENGTH_LONG;

/*
 * A simple {@link Fragment} subclass.
 * Use the {@link HomeFragment#newInstance} factory method to
 * create an instance of this fragment.
 */


// 오늘의 인기글 DB 연결
public class HomeFragment extends Fragment {

    private TextView text_user_id1;
    private TextView text_user_id2;
    private TextView text_title1;
    private TextView text_title2;
    private TextView text_context1;
    private TextView text_context2;
    private ImageButton youtube_btn1;
    private ImageButton youtube_btn2;
    private Context context;
    private ServiceApi service;


    String get_p_id = ((LoginActivity)LoginActivity.context_main).p_id;

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        View v = inflater.inflate(R.layout.fragment_home, container, false);
        context = container.getContext();

        text_user_id1 =(TextView)v.findViewById(R.id.text_user_id);
        text_user_id2 =(TextView)v.findViewById(R.id.text_user_id2);
        text_title1 =(TextView)v.findViewById(R.id.text_title);
        text_title2 =(TextView)v.findViewById(R.id.text_title2);
        text_context1 =(TextView)v.findViewById(R.id.text_context);
        text_context2 =(TextView)v.findViewById(R.id.text_context2);
        youtube_btn1 = (ImageButton)v.findViewById(R.id.youtube_btn1);
        youtube_btn2=(ImageButton)v.findViewById(R.id.youtube_btn2);

        service = RetrofitClient.getClient().create(ServiceApi.class);


        searchPopComm(new BestCommReq(get_p_id));

        //int r_value1 = (int)Math.random() * 10 + 1;
        //int r_value2 = (int)Math.random() * 10 + 1;



        youtube_btn1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                showYoutube(new YoutubeReq(3));
            }
        });

        youtube_btn2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                showYoutube(new YoutubeReq(4));
            }
        });
        return v;
    }

    private void searchPopComm(BestCommReq Data){
        service.homeComm(Data).enqueue(new Callback<BestCommRes>() {
            @Override
            public void onResponse(Call<BestCommRes> call, Response<BestCommRes> response) {
                BestCommRes result = response.body();

                if (result.getCode() == 200){
                    int BestComm = Integer.parseInt(result.getBestComm());
                    int sencondComm = Integer.parseInt(result.getSecondComm());
                    // 여기서 댓글 수 적는거 넣어
                    showPopComm(new ShowBestCommReq(result.getBestComm(), result.getSecondComm()));
                }
                else
                {
                    Toast.makeText(context, "오류 발생 : 404", LENGTH_LONG).show();
                }
            }

            @Override
            public void onFailure(Call<BestCommRes> call, Throwable t) {
                String texts = "";
                texts=t.getMessage();
                Toast.makeText(context, texts, Toast.LENGTH_LONG).show();;
                Log.e("인기글 찾기 로딩 에러 발생", t.getMessage());
                t.printStackTrace();
            }
        });
    }

    private void showPopComm(ShowBestCommReq Data)
    {
        service.showHomeComm(Data).enqueue(new Callback<ShowBestCommRes>() {
            @Override
            public void onResponse(Call<ShowBestCommRes> call, Response<ShowBestCommRes> response) {
                ShowBestCommRes result = response.body();

                if (result.getCode() == 200){
                    text_user_id1.setText(result.getBest_user_id());
                    text_user_id2.setText(result.getSecond_user_id());

                    text_context1.setText(result.getBest_content());
                    text_context2.setText(result.getSecond_content());

                    text_title1.setText(result.getBest_title());
                    text_title2.setText(result.getSecond_title());
                }
                else
                {
                    // 여기가 문제
                    Toast.makeText(context, "오류 발생 : 404", LENGTH_LONG).show();
                }
            }

            @Override
            public void onFailure(Call<ShowBestCommRes> call, Throwable t) {
                String texts = "";
                texts=t.getMessage();
                Toast.makeText(context, texts, Toast.LENGTH_LONG).show();
                //Log.e("인기글 로딩 에러 발생", t.getMessage());
                Log.e(Data + "인기글 로딩 에러 발생", t.getMessage());
                t.printStackTrace();
            }
        });

    }

    private void showYoutube(YoutubeReq Data){

        service.homeYoutube(Data).enqueue(new Callback<YoutubeRes>() {
            @Override
            public void onResponse(Call<YoutubeRes> call, Response<YoutubeRes> response) {
                YoutubeRes result = response.body();
                if (result.getCode() == 200){
                    String youtube_url1 = result.getUrl1();

                    Intent intent = new Intent(getContext(), MainActivity.class);
                    intent.putExtra("key", youtube_url1);

                    startActivity(intent);
                }
                else
                {
                    Toast.makeText(context, "오류 발생 : 404", LENGTH_LONG).show();
                }
            }

            @Override
            public void onFailure(Call<YoutubeRes> call, Throwable t) {
                String texts = "";
                texts=t.getMessage();
                Toast.makeText(context, texts, Toast.LENGTH_LONG).show();
                Log.e("유튜브 로딩 에러 발생", t.getMessage());
                t.printStackTrace();
            }
        });
    }
}
package com.example.ladybug.Activity;

import android.content.Intent;
import android.graphics.Color;
import android.os.Bundle;

import androidx.constraintlayout.widget.ConstraintLayout;
import androidx.fragment.app.Fragment;

import androidx.appcompat.app.AppCompatActivity;

import android.view.Gravity;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageButton;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.TextView;
import android.widget.VideoView;
import android.widget.Toast;
import android.widget.MediaController;
import android.media.MediaPlayer;
import android.os.Bundle;
import android.util.Log;

import com.example.ladybug.Data.CommunityRes;
import com.example.ladybug.R;
import com.example.ladybug.network.RetrofitClient;
import com.example.ladybug.network.ServiceApi;


import com.example.ladybug.Data.VideoReq;
import com.example.ladybug.Data.VideoRes;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class VideoFragment extends Fragment {

    private ServiceApi service;

    private LinearLayout V_layout;

    private String id;
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        View v = inflater.inflate(R.layout.fragment_video, container, false);

        id = ((LoginActivity) LoginActivity.context_main).p_id;
        V_layout = (LinearLayout) v.findViewById(R.id.videolayout);

        service = RetrofitClient.getClient().create(ServiceApi.class);



        VideoDB(new VideoReq(id));

        return v;
    }

    private void VideoDB(VideoReq Data){
        service.userVideo(Data).enqueue(new Callback<VideoRes>() {
            @Override
            public void onResponse(Call<VideoRes> call, Response<VideoRes> response) {
                VideoRes result = response.body();

                LinearLayout.LayoutParams L_lp = new LinearLayout.LayoutParams(
                        ViewGroup.LayoutParams.MATCH_PARENT,
                        500);

                //L_lp.setMargins(0,0,0,5);

                LinearLayout.LayoutParams H_lp = new LinearLayout.LayoutParams(
                        ViewGroup.LayoutParams.MATCH_PARENT,
                        ViewGroup.LayoutParams.MATCH_PARENT);
                H_lp.setMargins(0,0,0,5);

                for(int i =0; i < result.getSize(); i++)
                {
                    LinearLayout H_layout = new LinearLayout(getContext());
                    H_layout.setOrientation(LinearLayout.HORIZONTAL);
                    H_layout.setLayoutParams(L_lp);

                    LinearLayout text_layout = new LinearLayout(getContext());
                    text_layout.setOrientation(LinearLayout.VERTICAL);
                    text_layout.setLayoutParams(H_lp);


                    ImageButton btn = new ImageButton(getContext());
                    Button text_btn = new Button(getContext());
                    Button text_location = new Button(getContext());

                    btn.setBackgroundResource(R.drawable.video_green);

                    text_btn.setBackgroundColor(Color.WHITE);
                    text_btn.setText(result.getVideo_date()[i] );
                    text_location.setBackgroundColor(Color.WHITE);
                    text_location.setText(result.getVideo_location()[i]);

                    int idx = i;
                    btn.setOnClickListener(new View.OnClickListener() {
                        @Override
                        public void onClick(View v) {
                            Intent intent = new Intent(v.getContext(), VideoActivity.class);
                            intent.putExtra("key", result.getVideo_name()[idx]);
                            startActivity(intent);
                        }
                    });

                    text_btn.setOnClickListener(new View.OnClickListener() {
                        @Override
                        public void onClick(View v){
                            Intent intent = new Intent(v.getContext(), VideoActivity.class);
                            intent.putExtra("key", result.getVideo_name()[idx]);
                            startActivity(intent);
                        }
                    });

                    text_location.setOnClickListener(new View.OnClickListener() {
                        @Override
                        public void onClick(View v){
                            Intent intent = new Intent(v.getContext(), VideoActivity.class);
                            intent.putExtra("key", result.getVideo_name()[idx]);
                            startActivity(intent);
                        }
                    });

                    V_layout.addView(H_layout);
                    H_layout.addView(btn);
                    H_layout.addView(text_layout);
                    text_layout.addView(text_btn);
                    text_layout.addView(text_location);

                } //for문 끝

            }


            @Override
            public void onFailure(Call<VideoRes> call, Throwable t) {
                String texts = "";
                texts=t.getMessage();

                Toast.makeText(getContext(), texts, Toast.LENGTH_LONG).show();;
                Log.e("비디오 불러오기 에러 발생", t.getMessage());
                t.printStackTrace();

            }
        });

    }


}
package com.example.ladybug.Activity;

import android.app.ActionBar;
import android.content.Intent;
import android.os.Bundle;

import androidx.fragment.app.Fragment;

import android.util.Log;
import android.view.Gravity;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.LinearLayout;
import android.widget.Toast;

import com.example.ladybug.Data.CommunityReq;
import com.example.ladybug.Data.CommunityRes;
import com.example.ladybug.R;
import com.example.ladybug.network.RetrofitClient;
import com.example.ladybug.network.ServiceApi;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;


//스크롤 뷰, DB 긁어와서 게시글 생성
//만들어야 될 화면
//1. 게시글 작성 화면
//2. 게시글 화면 (댓글 보이는 화면)
public class CommunityFragment extends Fragment implements View.OnClickListener {

    private ImageButton btn_plus;
    private ServiceApi service;
    private LinearLayout L_layout;
    private String id;
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        View v = inflater.inflate(R.layout.fragment_community, container, false);
        id = ((LoginActivity) LoginActivity.context_main).p_id;

        btn_plus = (ImageButton) v.findViewById(R.id.plus);
        btn_plus.setOnClickListener((View.OnClickListener) this);
        L_layout = (LinearLayout)v.findViewById(R.id.CommuLayout);

        service = RetrofitClient.getClient().create(ServiceApi.class);

        GetCommunityDB(new CommunityReq(id));



        return v;
    }

    @Override
    public void onClick(View v) {
        // implements your things
        switch (v.getId()) {
            case R.id.plus:
                Intent intent = new Intent(getContext(), NewPostActivity.class);
                startActivity(intent);
                break;
        }
    }

    private void GetCommunityDB(CommunityReq Data){
        service.userCommunity(Data).enqueue(new Callback<CommunityRes>() {
            @Override
            public void onResponse(Call<CommunityRes> call, Response<CommunityRes> response) {
                CommunityRes result = response.body();

                LinearLayout.LayoutParams lp = new LinearLayout.LayoutParams(
                        ViewGroup.LayoutParams.MATCH_PARENT,
                        100);
                lp.setMargins(0,0,0,10);

                for(int i =0; i < result.getSize(); i++)
                {
                    Button btn = new Button(getContext());
                    //Toast.makeText(getContext(), result.getTitle()[i], Toast.LENGTH_LONG).show();;
                    btn.setBackgroundResource(R.drawable.notice_board);
                    btn.setText(result.getTitle()[i]);
                    btn.setPadding(50,0,50,0);
                    btn.setLayoutParams(lp);
                    btn.setGravity(Gravity.LEFT|Gravity.CENTER_VERTICAL);
                    int idx = i;
                    btn.setOnClickListener(new View.OnClickListener() {
                        @Override
                        public void onClick(View v) {
                            Intent intent = new Intent(v.getContext(), DetailActivity.class);
                            intent.putExtra("key", result.getCommunity_num()[idx]);
                            startActivity(intent);
                        }
                    });

                    L_layout.addView((btn));
                }

            }

            @Override
            public void onFailure(Call<CommunityRes> call, Throwable t) {
                String texts = "";
                texts=t.getMessage();

                Toast.makeText(getContext(), texts, Toast.LENGTH_LONG).show();;
                Log.e("커뮤니티 에러 발생", t.getMessage());
                t.printStackTrace();
            }
        });

    }
}
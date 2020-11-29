package com.example.ladybug.Activity;
import androidx.annotation.NonNull;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.widget.EditText;
import android.widget.LinearLayout;
import android.widget.TextView;
import android.widget.Toast;

import com.example.ladybug.Data.DetailReq;
import com.example.ladybug.Data.DetailRes;
import com.example.ladybug.network.RetrofitClient;
import com.example.ladybug.network.ServiceApi;


import com.example.ladybug.R;
import com.example.ladybug.network.RetrofitClient;
import com.example.ladybug.network.ServiceApi;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;


public class DetailActivity extends AppCompatActivity {
    private TextView title;
    private TextView content;
    private LinearLayout layout;

    private ServiceApi service;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_detail);

        title = (TextView)findViewById(R.id.detail_title);
        content = (TextView) findViewById(R.id.detail_content);
        layout = (LinearLayout) findViewById(R.id.detail_laydout);

        service = RetrofitClient.getClient().create(ServiceApi.class);

        Intent intent = getIntent();
        String key = intent.getStringExtra("key");

        //Toast.makeText(DetailActivity.this, key, Toast.LENGTH_LONG).show();;

        int num = Integer.parseInt(key);
        GetDataDB(new DetailReq(num));
    }

    private void GetDataDB(DetailReq Data){
        service.userDetail(Data).enqueue(new Callback<DetailRes>() {
            @Override
            public void onResponse(Call<DetailRes> call, Response<DetailRes> response) {
                DetailRes result = response.body();

                title.setText(result.getTitle());
                content.setText(result.getContent());

                for(int i =0; i< result.getSize(); i++){
                    if( result.getCommand()[i] == " ") continue;
                    TextView tx = new TextView(DetailActivity.this);
                    tx.setText(result.getCommand()[i]);

                    layout.addView((tx));
                }

            }

            @Override
            public void onFailure(Call<DetailRes> call, Throwable t) {
                String texts = "";
                texts=t.getMessage();

                Toast.makeText(DetailActivity.this, texts, Toast.LENGTH_LONG).show();;
                Log.e("게시판 에러 발생", t.getMessage());
                t.printStackTrace();
            }
        });
    }
}
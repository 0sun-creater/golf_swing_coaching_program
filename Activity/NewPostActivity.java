package com.example.ladybug.Activity;
import androidx.annotation.NonNull;

import androidx.appcompat.app.AppCompatActivity;

import android.app.Service;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.EditText;
import android.widget.ImageButton;
import android.widget.Toast;

import com.example.ladybug.Data.CommandReq;
import com.example.ladybug.Data.CommandRes;
import com.example.ladybug.Data.LoginRes;
import com.example.ladybug.Data.PostReq;
import com.example.ladybug.Data.PostRes;
import com.example.ladybug.R;
import com.example.ladybug.network.RetrofitClient;
import com.example.ladybug.network.ServiceApi;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class NewPostActivity extends AppCompatActivity {

    private ImageButton post, cancel;
    private EditText title, content;
    private ServiceApi service;
    private String id;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_new_post);

        post = (ImageButton) findViewById(R.id.post_btn);
        cancel = (ImageButton) findViewById(R.id.post_cancel);
        title = (EditText) findViewById(R.id.title_post);
        content = (EditText) findViewById(R.id.content_post);

        service = RetrofitClient.getClient().create(ServiceApi.class);

        post.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                posting();
            }
        });

        cancel.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(getApplicationContext(), HomeActivity.class);
                startActivity(intent);
            }
        });
    }

    private void posting(){
        title.setError(null);
        content.setError(null);

        String title_ = title.getText().toString();
        String content_ = content.getText().toString();

        boolean flag = false;
        View focusView = null;

        if(title_.isEmpty()){
            title.setError("제목을 입력해주세요.");
            focusView = title;
            flag = true;
        }else if(!isTitleValid(title_)){
            title.setError("제목을 50자 이내로 입력해주세요.");
            focusView = title;
            flag = true;
        }

        if(content_.isEmpty()){
            content.setError("게시글 내용을 입력해주세요.");
            focusView = content;
            flag = true;
        }else if(!isContentValid(content_)){
            content.setError("내용을 255자 이내로 입력해주세요.");
            focusView = content;
            flag = true;
        }


        if(flag){
            focusView.requestFocus();
        }else{
            id = ((LoginActivity) LoginActivity.context_main).p_id;
            PostDB(new PostReq(id,title_,content_));
        }

    }
    private void PostDB(PostReq Data){
        service.userPosting(Data).enqueue(new Callback<PostRes>() {
            @Override
            public void onResponse(Call<PostRes> call, Response<PostRes> response) {
                PostRes result = response.body();

                if (result.getCode() == 200) {
                    CommandDB(new CommandReq(id));
                }

            }

            @Override
            public void onFailure(Call<PostRes> call, Throwable t) {
                String texts = "";
                texts=t.getMessage();

                Toast.makeText(NewPostActivity.this, texts, Toast.LENGTH_LONG).show();;
                Log.e("게시물 작성 에러 발생", t.getMessage());
                t.printStackTrace();
            }
        });
    }

    private void CommandDB(CommandReq Data){
        service.userCommand(Data).enqueue(new Callback<CommandRes>() {
            @Override
            public void onResponse(Call<CommandRes> call, Response<CommandRes> response) {
                CommandRes result = response.body();
                if(result.getCode() == 200){
                    Toast.makeText(NewPostActivity.this, "게시글 작성 완료", Toast.LENGTH_LONG).show();;
                    Intent intent2 = new Intent(getApplicationContext(), HomeActivity.class);
                    startActivity(intent2);
                    finish();
                }
            }

            @Override
            public void onFailure(Call<CommandRes> call, Throwable t) {
                String texts = "";
                texts=t.getMessage();

                Toast.makeText(NewPostActivity.this, texts, Toast.LENGTH_LONG).show();;
                Log.e("게시물 작성 에러 발생", t.getMessage());
                t.printStackTrace();
            }
        });
    }


    private boolean isTitleValid(String title_){
        return title_.length() <= 50;
    }
    private boolean isContentValid(String content_){
        return content_.length() <=255;
    }
}
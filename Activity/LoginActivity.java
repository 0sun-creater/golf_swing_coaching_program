package com.example.ladybug.Activity;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageButton;
import android.widget.Toast;

import com.example.ladybug.R;
import com.example.ladybug.Data.LoginReq;
import com.example.ladybug.Data.LoginRes;
import com.example.ladybug.network.ServiceApi;
import com.example.ladybug.network.RetrofitClient;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class LoginActivity extends AppCompatActivity {

    private EditText text_id;
    private EditText text_pwd;
    private ImageButton btn_login;
    private ImageButton btn_sign;
    private ServiceApi service;

    public static Context context_main;
    public String p_id;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        context_main=this;

        text_id = (EditText) findViewById(R.id.login_id);
        text_pwd = (EditText) findViewById(R.id.login_pwd);
        btn_login = (ImageButton) findViewById(R.id.btn_login);
        btn_sign = (ImageButton) findViewById(R.id.btn_sign);

        service = RetrofitClient.getClient().create(ServiceApi.class);



        //login 버튼 클릭시
        btn_login.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                attemptLogin();
            }
        });

        //sign up 버튼 클릭시
        btn_sign.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent2 = new Intent(getApplicationContext(), SignActivity.class);
                startActivity(intent2);
            }
        });

    }

    private void attemptLogin() {
        text_id.setError(null);
        text_pwd.setError(null);

        String id = text_id.getText().toString();
        String pwd = text_pwd.getText().toString();

        boolean cancel =false;
        View focusView = null;

        //비밀번호 유효성 검사
        if(pwd.isEmpty()){
            text_pwd.setError("비밀번호를 입력해주세요.");
            focusView = text_pwd;
            cancel = true;
        } else if (!isPwdValid(pwd)){
            text_pwd.setError("20자 이내로 입력해주세요");
            focusView = text_pwd;
            cancel = true;
        }


        //아이디 유효성 검사
        if(id.isEmpty()) {
            text_id.setError("아이디를 입력해주세요.");
            focusView = text_id;
            cancel = true;
        } else if (!isIDValid(id)) {
            text_id.setError("20자 이내로 입력해주세요.");
            focusView = text_id;
            cancel = true;
        }

        if(cancel){
            focusView.requestFocus();
        }else{
            p_id=id;

            startLogin(new LoginReq(id, pwd));
        }
    }

    private void startLogin(LoginReq Data){
        service.userLogin(Data).enqueue(new Callback<LoginRes>() {
            @Override
            public void onResponse(Call<LoginRes> call, Response<LoginRes> response) {
                LoginRes result = response.body();
                Toast.makeText(LoginActivity.this, result.getMessage(), Toast.LENGTH_LONG).show();;

                if (result.getCode() == 200){
                    //home 화면으로 넘어가기
                    Intent intent = new Intent(getApplicationContext(), HomeActivity.class);
                    startActivity(intent);
                    finish();
                }
            }

            @Override
            public void onFailure(Call<LoginRes> call, Throwable t) {
                String texts = "";
                texts=t.getMessage();

                Toast.makeText(LoginActivity.this, texts, Toast.LENGTH_LONG).show();;
                Log.e("로그인 에러 발생", t.getMessage());
                t.printStackTrace();
                //showProgress(false);
            }
        });
    }

    private boolean isIDValid(String id_) {
        return id_.length() <= 20;
    }

    private boolean isPwdValid(String password) {
        return password.length() <= 20;
    }

    //private void showProgress(boolean show) {
    // progressView.setVisibility(show ? View.VISIBLE : View.GONE);
    //}
}
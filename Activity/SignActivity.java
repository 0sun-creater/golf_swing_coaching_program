package com.example.ladybug.Activity;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageButton;
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.TextView;
import android.widget.Toast;

import com.example.ladybug.Data.SignReq;
import com.example.ladybug.Data.SignRes;
import com.example.ladybug.R;
import com.example.ladybug.network.RetrofitClient;
import com.example.ladybug.network.ServiceApi;


import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;


public class SignActivity extends AppCompatActivity {

    private EditText text_id,text_pwd,text_tall;
    private TextView text_weight,text_gender;
    private ImageButton btn_sign;
    private RadioButton boy, girl, small, medium, large;
    private RadioGroup weight_group, gender_group;

    private ServiceApi service;


    private int gender = 0;
    private int weight = 0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_sign);

        text_id = (EditText) findViewById(R.id.et_id);
        text_pwd = (EditText) findViewById(R.id.et_pwd);
        text_tall = (EditText) findViewById(R.id.et_tall);
        text_weight = (TextView) findViewById(R.id.et_weight);
        text_gender = (TextView) findViewById(R.id.et_gender);
        btn_sign = (ImageButton) findViewById(R.id.btn_finish);
        boy = (RadioButton) findViewById(R.id.rb_boy);
        girl = (RadioButton) findViewById(R.id.rb_girl);
        small = (RadioButton) findViewById(R.id.rb_small);
        medium = (RadioButton) findViewById(R.id.rb_medium);
        large= (RadioButton) findViewById(R.id.rb_large);

        weight_group = (RadioGroup) findViewById(R.id.radioGroup_weight);
        gender_group = (RadioGroup) findViewById(R.id.radioGroup_gender);

        service = RetrofitClient.getClient().create(ServiceApi.class);



        weight_group.setOnCheckedChangeListener(new RadioGroup.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(RadioGroup group, int checkedId) {
                switch (checkedId) {
                    case R.id.rb_small:
                        weight = 1;
                        break;
                    case R.id.rb_medium:
                        weight = 2;
                        break;
                    case R.id.rb_large:
                        weight = 3;
                        break;
                }
            }
        });
        gender_group.setOnCheckedChangeListener(new RadioGroup.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(RadioGroup group, int checkedId) {
                switch (checkedId) {
                    case R.id.rb_boy:
                        gender =1;
                        break;
                    case R.id.rb_girl:
                        gender =2;
                        break;
                }
            }
        });

        //가입완료 버튼 클릭시
        btn_sign.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                sign_up();
            }
        });

    }

    private void id_check(){

    }

    private void sign_up(){
        text_id.setError(null);
        text_pwd.setError(null);
        text_tall.setError(null);
        text_weight.setError(null);
        text_gender.setError(null);


        String user_id = text_id.getText().toString();
        String user_pwd = text_pwd.getText().toString();
        String tall_ = text_tall.getText().toString();

        boolean cancel =false;
        View focusView = null;

        //비밀번호 유효성 검사
        if(user_pwd.isEmpty()){
            text_pwd.setError("비밀번호를 입력해주세요.");
            focusView = text_pwd;
            cancel = true;
        } else if (!isPwdValid(user_pwd)){
            text_pwd.setError("20자 이내로 입력해주세요");
            focusView = text_pwd;
            cancel = true;
        }


        //아이디 유효성 검사
        if(user_id.isEmpty()) {
            text_id.setError("아이디를 입력해주세요.");
            focusView = text_id;
            cancel = true;
        } else if (!isIDValid(user_id)) {
            text_id.setError("20자 이내로 입력해주세요.");
            focusView = text_id;
            cancel = true;
        }

        int tall = isTallValid(tall_);
        //키 유효성 검사
        if(tall_.isEmpty()) {
            text_tall.setError("키를 입력해주세요.");
            focusView = text_tall;
            cancel = true;
        } else if (tall==0) {
            text_tall.setError("숫자만 입력해주세요.");
            focusView = text_tall;
            cancel = true;
        }

        //라디오 버튼 유효성 검사
        if(weight == 0){
            text_weight.setError("체형을 선택해주세요.");
            focusView = text_weight;
            cancel = true;
        }
        if(gender == 0){
            text_gender.setError("성별을 선택해주세요.");
            focusView = text_gender;
            cancel = true;
        }

        if(cancel){
            focusView.requestFocus();
        }else{
            startSign_up(new SignReq(user_id, user_pwd, tall_, weight, gender));
        }
    }

    private void startSign_up(SignReq Data) {
        service.userSign(Data).enqueue(new Callback<SignRes>() {
            @Override
            public void onResponse(Call<SignRes> call, Response<SignRes> response) {
                SignRes result = response.body();
                Toast.makeText(SignActivity.this, result.getMessage(), Toast.LENGTH_LONG).show();

                if (result.getCode() == 200) {
                    finish();
                }
            }

            @Override
            public void onFailure(Call<SignRes> call, Throwable t){
                Toast.makeText(SignActivity.this, "회원가입 에러 발생",Toast.LENGTH_LONG).show();;
                Log.e("회원가입 에러 발생", t.getMessage());
                t.printStackTrace();

            }

        });
    }

    private int isTallValid(String tall_){
        try{
            int tall__ = Integer.parseInt(tall_);
            return tall__;
        }catch (Exception e){
            return 0;
        }
    }

    private boolean isIDValid(String id_) {
        return id_.length() <= 20;
    }

    private boolean isPwdValid(String password) {
        return password.length() <= 20;
    }

}

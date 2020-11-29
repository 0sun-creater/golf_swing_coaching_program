package com.example.ladybug.Activity;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.EditText;
import android.widget.ImageButton;
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.TextView;
import android.widget.Toast;

import com.example.ladybug.Data.UpdateReq;
import com.example.ladybug.Data.UpdateRes;
import com.example.ladybug.R;
import com.example.ladybug.network.RetrofitClient;
import com.example.ladybug.network.ServiceApi;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class UpdateActivity extends AppCompatActivity {
    private ImageButton btn_cancel, btn_update;
    private EditText text_newpwd,text_checkpwd,text_tall;
    private TextView text_weight,text_gender;
    private RadioButton boy, girl, small, medium, large;
    private RadioGroup weight_group, gender_group;


    private ServiceApi service;

    private int gender = 0;
    private int weight = 0;

    private String id;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_update);

        text_newpwd = (EditText) findViewById(R.id.et_newpwd);
        text_checkpwd = (EditText) findViewById(R.id.et_pwdcheck);
        text_tall = (EditText) findViewById(R.id.et_tall);
        text_weight = (TextView) findViewById(R.id.et_weight);
        text_gender = (TextView) findViewById(R.id.et_gender);
        btn_cancel = (ImageButton) findViewById(R.id.btn_cancel);
        btn_update = (ImageButton) findViewById(R.id.btn_update);
        boy = (RadioButton) findViewById(R.id.rb_boy);
        girl = (RadioButton) findViewById(R.id.rb_girl);
        small = (RadioButton) findViewById(R.id.rb_small);
        medium = (RadioButton) findViewById(R.id.rb_medium);
        large= (RadioButton) findViewById(R.id.rb_large);

        weight_group = (RadioGroup) findViewById(R.id.radioGroup_weight);
        gender_group = (RadioGroup) findViewById(R.id.radioGroup_gender);

        service = RetrofitClient.getClient().create(ServiceApi.class);

        id = ((LoginActivity) LoginActivity.context_main).p_id;

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


        //변경하기 버튼 클릭시
        btn_update.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                update();
            }
        });

        //취소 버튼 클릭시
        btn_cancel.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent =  new Intent(getApplicationContext(), HomeActivity.class);
                startActivity(intent);
                finish();
            }
        });
    }


    private void update(){
        text_newpwd.setError(null);
        text_checkpwd.setError(null);
        text_tall.setError(null);
        text_weight.setError(null);
        text_gender.setError(null);


        String pwd = text_newpwd.getText().toString();
        String pwd_check = text_checkpwd.getText().toString();
        String tall = text_tall.getText().toString();

        boolean cancel =false;
        View focusView = null;

        //비밀번호 유효성 검사
        if(pwd.isEmpty()){
            text_newpwd.setError("새 비밀번호를 입력해주세요.");
            focusView = text_newpwd;
            cancel = true;
        } else if (!isPwdValid(pwd)){
            text_newpwd.setError("20자 이내로 입력해주세요");
            focusView = text_newpwd;
            cancel = true;
        } else if (pwd_check.isEmpty()) {
            text_checkpwd.setError("새 비밀번호를 다시 입력해주세요");
            focusView = text_checkpwd;
            cancel = true;
        } else if(!isPwdCheck(pwd, pwd_check)) {
            text_checkpwd.setError("새 비밀번호와 똑같이 입력해주세요");
            focusView = text_checkpwd;
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
            startUpdate(new UpdateReq(pwd, tall, weight, gender, id));
        }
    }

    private void startUpdate(UpdateReq Data) {
        service.userUpdate(Data).enqueue(new Callback<UpdateRes>() {
            @Override
            public void onResponse(Call<UpdateRes> call, Response<UpdateRes> response) {
                UpdateRes result = response.body();
                Toast.makeText(UpdateActivity.this, result.getMessage(), Toast.LENGTH_LONG).show();;

                if (result.getCode() == 200){
                    Intent intent = new Intent(getApplicationContext(), HomeActivity.class);
                    startActivity(intent);
                    finish();
                }
            }

            @Override
            public void onFailure(Call<UpdateRes> call, Throwable t) {
                String texts = "";
                texts=t.getMessage();

                Toast.makeText(UpdateActivity.this, texts, Toast.LENGTH_LONG).show();;
                Log.e("회원수정 에러 발생", t.getMessage());
                t.printStackTrace();
            }
        });

    }

    private boolean isPwdValid(String password) {
        return password.length() <= 20;
    }

    private boolean isPwdCheck(String pwd, String check){
        if (pwd.equals(check)) return true;
        else return false;
    }
}
package com.example.ladybug.Activity;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;

import androidx.fragment.app.Fragment;

import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageButton;
import android.widget.TextView;
import android.widget.Toast;

import com.example.ladybug.Data.DeleteReq;
import com.example.ladybug.Data.DeleteRes;
import com.example.ladybug.R;
import com.example.ladybug.network.RetrofitClient;
import com.example.ladybug.network.ServiceApi;

import org.w3c.dom.Text;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;


//버튼 누르면 다른 액티비티로 연결
//만들어야 될 화면
//1. 회원정보 수정 >> activity 생성 >> 회원 id 변경 (중복확인), 비밀번호 변경, 체형 변경  >> DB update SQL 날리기
//2. 앱정보 >> 그냥 아래에 "version" 만 띄워주는거도 나쁘지 않을듯
//3. 문의하기 >> activity 생성 >> 문의유형 고르고, textbox, 문의 보내기 버튼
//4. 회원탈퇴 >> 아래에 "탈퇴되었습니다." >> DB delete SQL 날리기
//5. 로그아웃 >> 아래에 "로그아웃 되었습니다." >> Login 화면으로 돌아가기
public class MyPageFragment extends Fragment implements View.OnClickListener {
    private ImageButton btn_update;
    private ImageButton btn_version;
    private ImageButton btn_ask;
    private ImageButton btn_bye;
    private ImageButton btn_logout;

    private TextView id_text;
    private ServiceApi service;

    private String id;

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        View v = inflater.inflate(R.layout.fragment_my_page, container, false);
        btn_update = (ImageButton) v.findViewById(R.id.imageB_update);
        btn_version = (ImageButton) v.findViewById(R.id.imageB_version);
        btn_ask = (ImageButton) v.findViewById(R.id.imageB_ask);
        btn_bye = (ImageButton) v.findViewById(R.id.imageB_bye);
        btn_logout = (ImageButton) v.findViewById(R.id.imageB_logout);

        btn_update.setOnClickListener((View.OnClickListener) this);
        btn_version.setOnClickListener((View.OnClickListener) this);
        btn_ask.setOnClickListener((View.OnClickListener) this);
        btn_bye.setOnClickListener((View.OnClickListener) this);
        btn_logout.setOnClickListener((View.OnClickListener) this);

        id_text = (TextView) v.findViewById(R.id.user_id_mypage);

        id = ((LoginActivity) LoginActivity.context_main).p_id;

        id_text.setText(id+"님");

        service = RetrofitClient.getClient().create(ServiceApi.class);


        // Inflate the layout for this fragment
        return v;

    }

    @Override
    public void onClick(View v) {
        // implements your things
        switch (v.getId()) {
            case R.id.imageB_update:
                Intent intent = new Intent(getContext(), UpdateActivity.class);
                startActivity(intent);
                break;

            case R.id.imageB_version:
                Toast.makeText(getContext(), "version 1.0.3", Toast.LENGTH_LONG).show();
                break;

            case R.id.imageB_ask:
                Intent intent2 = new Intent(getContext(), AskActivity.class);
                startActivity(intent2);
                break;

            case R.id.imageB_bye:
                deleteID(new DeleteReq(id));
                break;

            case R.id.imageB_logout:
                Toast.makeText(getContext(), "로그아웃 되었습니다.", Toast.LENGTH_LONG).show();

                Intent intent4 = new Intent(getContext(), LoginActivity.class);
                startActivity(intent4);
                break;
        }
    }

    private void deleteID(DeleteReq Data) {
        service.userDelete(Data).enqueue(new Callback<DeleteRes>() {
            @Override
            public void onResponse(Call<DeleteRes> call, Response<DeleteRes> response) {
                DeleteRes result = response.body();
                Toast.makeText(getContext(), result.getMessage(), Toast.LENGTH_LONG).show();;
                if (result.getCode() == 200){
                    //home 화면으로 넘어가기
                    Intent intent3 = new Intent(getContext(), LoginActivity.class);
                    startActivity(intent3);
                }
            }

            @Override
            public void onFailure(Call<DeleteRes> call, Throwable t) {
                String texts = "";
                texts = t.getMessage();

                Toast.makeText(getContext(), texts, Toast.LENGTH_LONG).show();;
                Log.e("회원탈퇴 에러 발생", t.getMessage());
                t.printStackTrace();
            }
        });
    }
}
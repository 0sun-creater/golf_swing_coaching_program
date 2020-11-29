package com.example.ladybug.network;

import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;


public class RetrofitClient {
    private final static String BASE_URL = "EC2 주소";
    private static Retrofit retrofit = null;

    private RetrofitClient() {
    }

    public static Retrofit getClient() {
        if (retrofit == null) {
            retrofit = new Retrofit.Builder()
                    .baseUrl(BASE_URL) // 요청을 보낼 base url을 설정한다.
                    .addConverterFactory(GsonConverterFactory.create()) // JSON 파싱을 위한 GsonConverterFactory를 추가한다.
                    .build();
        }

        return retrofit;
    }
}



/*
  위에서 정의한 ServiceApi 인터페이스의 구현체를 만들기 위해 Retrofit 클래스를 사용해야 한다.

  서비스 객체를 초기화 및 생성하는 기본적인 코드는 아래와 같다.

  // Retrofit 객체 초기화
  Retrofit retrofit = new Retrofit.Builder()
      .baseUrl("base url 주소")
      .build();

  // ServiceApi 객체 생성
  ServiceApi service = retrofit.create(ServiceApi.class);
*/

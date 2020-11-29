package com.example.ladybug.Activity;

import android.content.Context;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.ImageButton;
import android.widget.Toast;
import android.widget.VideoView;

import androidx.appcompat.app.AppCompatActivity;

import com.amazonaws.auth.CognitoCachingCredentialsProvider;
import com.amazonaws.mobileconnectors.s3.transferutility.TransferListener;
import com.amazonaws.mobileconnectors.s3.transferutility.TransferNetworkLossHandler;
import com.amazonaws.mobileconnectors.s3.transferutility.TransferObserver;
import com.amazonaws.mobileconnectors.s3.transferutility.TransferState;
import com.amazonaws.mobileconnectors.s3.transferutility.TransferUtility;
import com.amazonaws.regions.Region;
import com.amazonaws.regions.Regions;
import com.amazonaws.services.s3.AmazonS3Client;
import com.example.ladybug.R;
import com.example.ladybug.network.RetrofitClient;
import com.example.ladybug.network.ServiceApi;

import java.io.File;

import static android.widget.Toast.LENGTH_LONG;

public class VideoActivity extends AppCompatActivity {

    private VideoView videoView;
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_video);

        videoView = (VideoView) findViewById(R.id.videoView);

        Intent intent = getIntent();
        String key = intent.getStringExtra("key");

        String getPath = AwsConnector(key);
        //show(getPath, key);
    }


    public String AwsConnector(String video_name){ // 비디오 재생
        CognitoCachingCredentialsProvider credentialsProvider = new CognitoCachingCredentialsProvider(
                this,
                "", // 자격 증명 풀 ID
                Regions.AP_NORTHEAST_2 // 리전
        );

        TransferNetworkLossHandler.getInstance(this);

        AmazonS3Client _s3Client = new AmazonS3Client(credentialsProvider, Region.getRegion(Regions.AP_NORTHEAST_2));

        TransferUtility transferUtility = TransferUtility.builder().
                context(this).
                defaultBucket(""). //버킷 이름
                s3Client(_s3Client).
                build();

        File resDir = this.getDir("video_storage", Context.MODE_PRIVATE);
        if(!resDir.exists())
        {
            resDir.mkdirs();
        }
        TransferObserver downloadObserver = transferUtility.download(video_name, new File(resDir.getPath() + "/" + video_name));
        downloadObserver.setTransferListener(new TransferListener() {
            @Override
            public void onStateChanged(int id, TransferState state) {
                if (state == TransferState.COMPLETED) {
                    try{
                        show(resDir.getPath(), video_name);
                    }catch(Exception e)
                    {
                        Toast.makeText(VideoActivity.this, e.getMessage(), LENGTH_LONG).show();
                    }
                }
            }
            @Override
            public void onProgressChanged(int id, long bytesCurrent, long bytesTotal) {
            }
            @Override
            public void onError(int id, Exception ex) {
                Toast.makeText(VideoActivity.this, ex.getMessage(), LENGTH_LONG).show();
            }
        });
        return resDir.getPath();
    }


    public void show(String path, String video_name)
    {
        Uri uri = Uri.parse(path + "/" + video_name);
        videoView.setVideoURI(uri);
        videoView.start();
    }

}

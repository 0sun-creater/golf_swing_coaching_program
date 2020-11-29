package com.example.ladybug.Activity;
import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentManager;
import androidx.fragment.app.FragmentTransaction;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.MenuItem;

import com.google.android.material.bottomnavigation.BottomNavigationView;

import com.example.ladybug.R;

public class HomeActivity extends AppCompatActivity {
    private Fragment MyPageFragment;
    private Fragment VideoFragment;
    private Fragment CommunityFragment;
    private Fragment HomeFragment;

    private void replaceFragment(Fragment fragment){
        FragmentManager fragmentManager = getSupportFragmentManager();
        FragmentTransaction fragmentTransaction = fragmentManager.beginTransaction();
        fragmentTransaction.replace(R.id.main_layout, fragment).commit();
    }

    private BottomNavigationView.OnNavigationItemSelectedListener mOnNavigationItemSelectedListener
        = new BottomNavigationView.OnNavigationItemSelectedListener() {

            @Override
            public boolean onNavigationItemSelected(@NonNull MenuItem item) {
                switch (item.getItemId()) {
                    case R.id.navigation_home:
                        replaceFragment(HomeFragment);
                        //replaceFragment(HafniumFragment);
                        return true;
                    case R.id.navigation_video:
                        replaceFragment(VideoFragment);
                        return true;
                    case R.id.navigation_community:
                        replaceFragment(CommunityFragment);
                        return true;
                    case R.id.navigation_my_page:
                        replaceFragment(MyPageFragment);
                        return true;
                }
                return false;
            }
        };


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_home);

        BottomNavigationView navView = findViewById(R.id.navigation_view);
        navView.setOnNavigationItemSelectedListener(mOnNavigationItemSelectedListener);

        //HomeFragment = new HafniumFragment();
        HomeFragment = new HomeFragment();
        CommunityFragment = new CommunityFragment();
        VideoFragment = new VideoFragment();
        MyPageFragment = new MyPageFragment();

        replaceFragment(HomeFragment);
    }
}
package com.example.user.arm_service;

import android.support.v4.app.Fragment;
import android.os.Bundle;
import android.os.Message;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import java.time.Instant;

/**
 * Created by User on 26.09.2018.
 */

public class SettingClass extends Fragment {
    public SettingClass(){

    }
    public static SettingClass newInstance(){
        return new SettingClass();
    }
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState){
        return inflater.inflate(R.layout.fragment_setting, container, false);
    }
}
